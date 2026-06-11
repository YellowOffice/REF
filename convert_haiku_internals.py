import os
import sys
import re
import json
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup, NavigableString
import concurrent.futures
import difflib
import threading

# Configuration
BASE_URL = "https://pulkomandy.tk/drop/haiku_internals/"
WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(WORKSPACE_DIR, "haiku-internals-md")
CACHE_DIR = os.path.join(OUTPUT_DIR, ".cache_html")
METADATA_FILE = os.path.join(OUTPUT_DIR, "metadata.json")
IMAGES_DIR = os.path.join(OUTPUT_DIR, "_images")
EXCLUDED_FILES = {"search.html", "genindex.html"}

# Ensure folders exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

download_lock = threading.Lock()

def get_html(url, force_network=False):
    """Fetch HTML page, utilizing local cache if available."""
    parsed = urllib.parse.urlparse(url)
    rel_path = parsed.path.replace('/drop/haiku_internals/', '').strip('/')
    if not rel_path or rel_path == 'index.html':
        filename = "index.html"
    else:
        filename = rel_path.replace('/', '_')
        
    cache_path = os.path.join(CACHE_DIR, filename)
    
    if not force_network and os.path.exists(cache_path):
        with open(cache_path, "r", encoding="utf-8") as f:
            return f.read()
            
    # Fetch from web
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
        with open(cache_path, "w", encoding="utf-8") as f:
            f.write(html)
        return html
    except Exception as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        raise

def download_image(img_url, local_img_path, force=False):
    """Download remote image if not already cached locally (thread-safe)."""
    with download_lock:
        if not force and os.path.exists(local_img_path):
            return
            
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(img_url, headers=headers)
        try:
            with urllib.request.urlopen(req) as response:
                img_data = response.read()
            os.makedirs(os.path.dirname(local_img_path), exist_ok=True)
            with open(local_img_path, "wb") as f:
                f.write(img_data)
            print(f"Downloaded image: {img_url} -> {local_img_path}")
        except Exception as e:
            print(f"Error downloading image {img_url}: {e}", file=sys.stderr)

def html_to_markdown_rec(element, page_filename, list_depth=0, list_type=None, list_index=1):
    """Recursively convert Sphinx HTML element to clean Markdown representation."""
    if element is None:
        return ""
    if isinstance(element, NavigableString):
        return element.string
        
    tag = element.name
    
    # Handle block elements
    if tag == 'p':
        content = "".join(html_to_markdown_rec(child, page_filename, list_depth, list_type, list_index) for child in element.children)
        return content + "\n\n"
        
    elif tag in ['b', 'strong']:
        content = "".join(html_to_markdown_rec(child, page_filename, list_depth, list_type, list_index) for child in element.children)
        return f"**{content}**" if content.strip() else ""
        
    elif tag in ['i', 'em']:
        content = "".join(html_to_markdown_rec(child, page_filename, list_depth, list_type, list_index) for child in element.children)
        return f"*{content}*" if content.strip() else ""
        
    elif tag in ['code', 'tt']:
        return f"`{element.get_text()}`"
        
    elif tag == 'span' and 'pre' in element.get('class', []):
        parent = element.parent
        if parent and parent.name in ['code', 'tt']:
            return "".join(html_to_markdown_rec(child, page_filename, list_depth, list_type, list_index) for child in element.children)
        return f"`{element.get_text()}`"
        
    elif tag == 'a':
        href = element.get('href', '')
        content = "".join(html_to_markdown_rec(child, page_filename, list_depth, list_type, list_index) for child in element.children).strip()
        if not content:
            return ""
            
        if href.startswith('http://') or href.startswith('https://') or href.startswith('mailto:'):
            return f"[{content}]({href})"
            
        if href.startswith('#'):
            return f"[{content}]({href})"
            
        # Relative link conversion
        parsed_href = urllib.parse.urlparse(href)
        path = parsed_href.path
        query = parsed_href.query
        fragment = parsed_href.fragment
        
        if path.endswith('.html'):
            filename = os.path.basename(path)
            if filename == 'index.html':
                path = path[:-10] + 'README.md'
            else:
                path = path[:-5] + '.md'
        elif path == '' and fragment:
            return f"[{content}](#{fragment})"
            
        new_href = path
        if query:
            new_href += f"?{query}"
        if fragment:
            new_href += f"#{fragment}"
            
        return f"[{content}]({new_href})"
        
    elif tag == 'br':
        return "\n"
        
    elif tag == 'ul':
        next_depth = list_depth + 1 if list_type is not None else list_depth
        items = []
        for child in element.children:
            if child.name == 'li':
                items.append(html_to_markdown_rec(child, page_filename, list_depth=next_depth, list_type='ul'))
            else:
                items.append(html_to_markdown_rec(child, page_filename, list_depth=list_depth, list_type=list_type))
        return "".join(items)
        
    elif tag == 'ol':
        next_depth = list_depth + 1 if list_type is not None else list_depth
        items = []
        idx = 1
        for child in element.children:
            if child.name == 'li':
                items.append(html_to_markdown_rec(child, page_filename, list_depth=next_depth, list_type='ol', list_index=idx))
                idx += 1
            else:
                items.append(html_to_markdown_rec(child, page_filename, list_depth=list_depth, list_type=list_type))
        return "".join(items)
        
    elif tag == 'li':
        indent = "  " * list_depth
        bullet = "* " if list_type == 'ul' else f"{list_index}. "
        bullet_len = len(bullet)
        
        block_tags = {'ul', 'ol', 'table', 'blockquote', 'pre', 'p', 'div'}
        parts = []
        current_inline = []
        
        def flush_inline():
            if current_inline:
                text = "".join(current_inline).strip()
                text = re.sub(r'\s+', ' ', text)
                if text:
                    current_inline.clear()
                    return text
            current_inline.clear()
            return ""
            
        first_p_as_inline = True
        for child in element.children:
            if isinstance(child, NavigableString):
                current_inline.append(child.string)
            elif child.name == 'p' and first_p_as_inline:
                first_p_as_inline = False
                for grand_child in child.children:
                    if isinstance(grand_child, NavigableString):
                        current_inline.append(grand_child.string)
                    else:
                        current_inline.append(html_to_markdown_rec(grand_child, page_filename, list_depth, list_type))
            elif child.name not in block_tags:
                current_inline.append(html_to_markdown_rec(child, page_filename, list_depth, list_type))
            else:
                first_p_as_inline = False
                inline_text = flush_inline()
                if inline_text:
                    parts.append(('inline', inline_text))
                    
                if child.name in ['ul', 'ol']:
                    block_md = html_to_markdown_rec(child, page_filename, list_depth=list_depth + 1, list_type=child.name)
                    parts.append(('list', block_md))
                else:
                    block_md = html_to_markdown_rec(child, page_filename, list_depth=list_depth, list_type=list_type)
                    parts.append(('block', block_md))
                    
        inline_text = flush_inline()
        if inline_text:
            parts.append(('inline', inline_text))
            
        res = []
        first_inline_seen = False
        for p_type, text in parts:
            if p_type == 'inline':
                if not first_inline_seen:
                    res.append(f"{indent}{bullet}{text}\n")
                    first_inline_seen = True
                else:
                    res.append(f"{indent}{' ' * bullet_len}{text}\n\n")
            elif p_type == 'list':
                res.append(text)
            elif p_type == 'block':
                lines = text.strip('\n').split('\n')
                indented_lines = []
                for line in lines:
                    if line.strip():
                        indented_lines.append(f"{indent}{' ' * bullet_len}{line}")
                    else:
                        indented_lines.append("")
                res.append("\n".join(indented_lines) + "\n\n")
                
        if not first_inline_seen and res:
            return f"{indent}{bullet}\n" + "".join(res)
            
        return "".join(res)
        
    elif tag == 'pre':
        # Find syntax language from Sphinx highlight container
        lang = 'text'
        parent = element.parent
        if parent and parent.name == 'div' and parent.get('class'):
            classes = parent.get('class')
            for c in classes:
                if c.startswith('highlight-'):
                    lang = c.replace('highlight-', '')
                    break
        code_text = element.get_text()
        return f"\n```{lang}\n{code_text.rstrip()}\n```\n\n"
        
    elif tag == 'table':
        # Check if this is a field-list table (admonition table)
        classes = element.get('class', [])
        if 'field-list' in classes:
            list_items = []
            for tr in element.find_all('tr'):
                name_th = tr.find('th', class_='field-name')
                body_td = tr.find('td', class_='field-body')
                if name_th and body_td:
                    name = html_to_markdown_rec(name_th, page_filename, list_depth, list_type).strip().rstrip(':')
                    body = html_to_markdown_rec(body_td, page_filename, list_depth, list_type).strip()
                    body = re.sub(r'\s+', ' ', body)
                    list_items.append(f"* **{name}:** {body}\n")
            return "\n" + "".join(list_items) + "\n"
            
        # Normal data table
        rows = []
        headers = []
        
        thead = element.find('thead')
        if thead:
            tr = thead.find('tr')
            if tr:
                headers = [html_to_markdown_rec(th, page_filename, list_depth, list_type).strip() for th in tr.find_all(['th', 'td'])]
        else:
            first_tr = element.find('tr')
            if first_tr and first_tr.find('th'):
                headers = [html_to_markdown_rec(th, page_filename, list_depth, list_type).strip() for th in first_tr.find_all('th')]
                
        tbody = element.find('tbody') or element
        for tr in tbody.find_all('tr', recursive=False if tbody != element else True):
            if headers and tr == element.find('tr') and tr.find('th'):
                continue
            cells = [html_to_markdown_rec(td, page_filename, list_depth, list_type).strip().replace('\n', ' ') for td in tr.find_all(['td', 'th'])]
            if cells:
                rows.append(cells)
                
        if not rows:
            return ""
            
        if not headers:
            headers = [f"Col {i+1}" for i in range(len(rows[0]))]
            
        # Determine column widths
        col_widths = [len(h) for h in headers]
        for r in rows:
            for idx, cell in enumerate(r):
                if idx < len(col_widths):
                    col_widths[idx] = max(col_widths[idx], len(cell))
                    
        header_line = "| " + " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers)) + " |"
        divider_line = "| " + " | ".join("-" * col_widths[i] for i in range(len(headers))) + " |"
        row_lines = []
        for r in rows:
            padded_row = r + [""] * (len(headers) - len(r))
            row_line = "| " + " | ".join(cell.ljust(col_widths[i]) for i, cell in enumerate(padded_row[:len(headers)])) + " |"
            row_lines.append(row_line)
            
        return "\n" + header_line + "\n" + divider_line + "\n" + "\n".join(row_lines) + "\n\n"
        
    elif tag == 'div' and 'admonition' in element.get('class', []):
        classes = element.get('class', [])
        alert_type = 'NOTE'
        if 'warning' in classes:
            alert_type = 'WARNING'
        elif 'caution' in classes:
            alert_type = 'CAUTION'
        elif 'important' in classes:
            alert_type = 'IMPORTANT'
        elif 'tip' in classes:
            alert_type = 'TIP'
            
        title_p = element.find('p', class_='admonition-title')
        if title_p:
            title_p.decompose()
            
        body_md = "".join(html_to_markdown_rec(child, page_filename, list_depth, list_type) for child in element.children).strip()
        lines = body_md.split('\n')
        formatted_lines = [f"> {line}" for line in lines]
        return f"\n> [!{alert_type}]\n" + "\n".join(formatted_lines) + "\n\n"
        
    elif tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        level = int(tag[1])
        for link in element.find_all('a', class_='headerlink'):
            link.decompose()
        title_text = "".join(html_to_markdown_rec(child, page_filename, list_depth, list_type) for child in element.children).strip()
        title_text = re.sub(r'\s+', ' ', title_text)
        return f"\n" + ("#" * level) + f" {title_text}\n\n"
        
    elif tag == 'img':
        src = element.get('src', '')
        alt = element.get('alt', 'Image')
        if src:
            img_url = urllib.parse.urljoin(urllib.parse.urljoin(BASE_URL, page_filename), src)
            local_img_path = os.path.normpath(os.path.join(OUTPUT_DIR, os.path.dirname(page_filename), src))
            download_image(img_url, local_img_path)
            return f"![{alt}]({src})"
        return ""
        
    elif tag == 'hr':
        return "\n---\n\n"
        
    elif tag == 'blockquote':
        content = "".join(html_to_markdown_rec(child, page_filename, list_depth, list_type) for child in element.children).strip()
        lines = content.split('\n')
        return "\n" + "\n".join(f"> {line}" for line in lines) + "\n\n"
        
    return "".join(html_to_markdown_rec(child, page_filename, list_depth, list_type) for child in element.children)

def convert_sphinx_html(html, filename):
    """Convert Sphinx documentation HTML to Markdown string."""
    soup = BeautifulSoup(html, 'lxml')
    
    # Extract title
    title_el = soup.find('title')
    title_text = title_el.get_text() if title_el else filename
    title_text = title_text.replace("— Haiku internals  documentation", "").strip()
    
    # Locate main content wrapper
    content_div = soup.find('div', class_='content')
    if not content_div:
        content_div = soup.find('body')
        
    if not content_div:
        return f"# {title_text}\n\nCould not extract content."
        
    # Remove navigation links / topnav if they leaked into the content
    for topnav in content_div.find_all('div', class_='topnav'):
        topnav.decompose()
    for bottomnav in content_div.find_all('div', class_='bottomnav'):
        bottomnav.decompose()
        
    # Parse recursive content
    md_body = html_to_markdown_rec(content_div, filename)
    
    # Cleanup extra whitespace or double spacing
    md_body = re.sub(r'\n{3,}', '\n\n', md_body)
    
    # Ensure a single clean heading if not present
    header = ""
    if not md_body.strip().startswith("# "):
        header = f"# {title_text}\n\n"
        
    footer = f"\n\nGenerated from the [original source documentation]({urllib.parse.urljoin(BASE_URL, filename)}).\n"
    
    return header + md_body.strip() + footer

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Convert Haiku Internals Sphinx HTML documentation to Markdown.")
    parser.add_argument("--force", action="store_true", help="Force rebuild of documentation regardless of timestamp.")
    parser.add_argument("--single", type=str, help="Process only a single HTML file (e.g. build/configure.html) and print it.")
    parser.add_argument("--dry-run", action="store_true", help="Run the parser but do not write any Markdown files.")
    args = parser.parse_args()
    
    # Single file mode
    if args.single:
        print(f"Single file mode: {args.single}")
        try:
            html = get_html(urllib.parse.urljoin(BASE_URL, args.single))
            md_content = convert_sphinx_html(html, args.single)
            print("--- CONVERTED MARKDOWN PREVIEW ---")
            print(md_content[:4000])
            if len(md_content) > 4000:
                print("... (truncated) ...")
        except Exception as e:
            print("Error processing single file:", e)
        return
        
    # Fetch headers of main index page
    print("Fetching Haiku Internals main page headers...")
    try:
        req = urllib.request.Request(BASE_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            info = response.info()
            last_modified = info.get("Last-Modified", "Unknown Date")
            etag = info.get("ETag", "").strip('"')
    except Exception as e:
        print(f"Error fetching main page: {e}")
        last_modified = "Unknown Date"
        etag = ""
        
    print(f"Remote Last-Modified: {last_modified}")
    print(f"Remote ETag: {etag}")
    
    # Check stored metadata
    metadata = {}
    if os.path.exists(METADATA_FILE):
        try:
            with open(METADATA_FILE, "r", encoding="utf-8") as f:
                metadata = json.load(f)
        except Exception:
            pass
            
    stored_modified = metadata.get("last_modified")
    stored_etag = metadata.get("etag")
    print(f"Stored Last-Modified: {stored_modified}")
    print(f"Stored ETag: {stored_etag}")
    
    if not args.force and stored_modified == last_modified and stored_etag == etag:
        print("Haiku Internals documentation is up to date. No changes to apply.")
        return
        
    # Fetch main index page to discover links
    print("Crawling index page for links...")
    main_html = get_html(BASE_URL, force_network=True)
    soup = BeautifulSoup(main_html, 'lxml')
    
    internal_pages = set()
    for a in soup.find_all('a'):
        href = a.get('href', '')
        if href and not href.startswith('http') and not href.startswith('#'):
            clean_href = href.split('#')[0]
            if clean_href.endswith('.html') and clean_href not in EXCLUDED_FILES:
                internal_pages.add(clean_href)
                
    # Also add index.html itself
    internal_pages.add("index.html")
    print(f"Discovered {len(internal_pages)} documentation pages.")
    
    # Crawl and parse in parallel
    markdown_outputs = {} # relative_path -> content
    
    def process_target(filename):
        url = urllib.parse.urljoin(BASE_URL, filename)
        try:
            html = get_html(url)
            md_content = convert_sphinx_html(html, filename)
            
            # Map filename: index.html -> README.md, else file.html -> file.md
            if filename == 'index.html':
                out_filename = 'README.md'
            elif filename.endswith('/index.html'):
                out_filename = filename[:-10] + 'README.md'
            else:
                out_filename = filename[:-5] + '.md'
                
            return out_filename, md_content
        except Exception as e:
            print(f"Error processing {filename}: {e}", file=sys.stderr)
            return None
            
    failures = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(process_target, fn) for fn in internal_pages]
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            if res:
                out_fn, content = res
                markdown_outputs[out_fn] = content
            else:
                failures += 1
                
    # Write differentially
    print("Writing markdown files...")
    written = 0
    updated = 0
    unchanged = 0
    
    active_paths = set(markdown_outputs.keys())
    
    for rel_path, content in markdown_outputs.items():
        full_path = os.path.join(OUTPUT_DIR, rel_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        if os.path.exists(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
                old_content = f.read()
            if old_content == content:
                unchanged += 1
                continue
                
            updated += 1
            
            diff = difflib.unified_diff(
                old_content.splitlines(),
                content.splitlines(),
                fromfile=f"a/{rel_path}",
                tofile=f"b/{rel_path}",
                lineterm=""
            )
            diff_text = "\n".join(list(diff)[:15])
            
            if not args.dry_run:
                with open(full_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"UPDATED: {rel_path}")
                if diff_text:
                    print("DIFF PREVIEW:\n" + diff_text + "\n" + "-"*40)
            else:
                print(f"DRY-RUN UPDATED: {rel_path}")
                if diff_text:
                    print("DIFF PREVIEW:\n" + diff_text + "\n" + "-"*40)
        else:
            written += 1
            if not args.dry_run:
                with open(full_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"CREATED: {rel_path}")
            else:
                print(f"DRY-RUN CREATED: {rel_path}")
                
    # Clean up old markdown files no longer in active crawl
    if failures == 0 and len(internal_pages) > 0:
        for root, dirs, files in os.walk(OUTPUT_DIR):
            if ".cache_html" in root:
                continue
            for file in files:
                if file == 'metadata.json':
                    continue
                full_file_path = os.path.join(root, file)
                rel_file_path = os.path.relpath(full_file_path, OUTPUT_DIR).replace('\\', '/')
                
                # Skip checking/deleting cached images
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
                    continue
                    
                if file.endswith('.md'):
                    if rel_file_path not in active_paths:
                        print(f"DELETED: {rel_file_path} (no longer in remote documentation)")
                        if not args.dry_run:
                            os.remove(full_file_path)
    else:
        if failures > 0:
            print(f"Skipping obsolete file cleanup because {failures} page(s) failed to download.")
        else:
            print("Skipping obsolete file cleanup because no documentation pages were discovered.")
                        
    print(f"\nSummary:")
    print(f"  Created: {written}")
    print(f"  Updated: {updated}")
    print(f"  Unchanged: {unchanged}")
    
    # Save metadata
    if not args.dry_run:
        metadata = {
            "last_modified": last_modified,
            "etag": etag,
            "files": list(active_paths)
        }
        with open(METADATA_FILE, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)
        print("Updated metadata.")

if __name__ == '__main__':
    main()
