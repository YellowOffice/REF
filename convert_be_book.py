import os
import sys
import re
import urllib.request
import urllib.parse
import warnings
from bs4 import BeautifulSoup, NavigableString, XMLParsedAsHTMLWarning
import concurrent.futures

# Mute BeautifulSoup XMLParsedAsHTMLWarning warning
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

# Configuration
BASE_URL = "https://www.haiku-os.org/legacy-docs/bebook/"
WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(WORKSPACE_DIR, "legacy-bebook-md")

# Ensure folder exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Kit Mapping
BE_KIT_MAP = {
    "TheApplicationKit.html": "application_kit",
    "TheDeviceKit.html": "device_kit",
    "TheGameKit.html": "game_kit",
    "TheInputServer.html": "input_server",
    "TheInterfaceKit.html": "interface_kit",
    "TheKernelKit.html": "kernel_kit",
    "TheMailKit.html": "mail_kit",
    "TheMediaKit.html": "media_kit",
    "TheMidiKit.html": "midi_kit",
    "TheNetworkKit.html": "network_kit",
    "TheOpenGLKit.html": "opengl_kit",
    "TheStorageKit.html": "storage_kit",
    "TheSupportKit.html": "support_kit",
    "TheTranslationKit.html": "translation_kit"
}

def build_frontmatter(metadata_list, title_text, current_kit):
    """Return a YAML frontmatter block string for a BeBook API page."""
    doc_type = "topic"
    if title_text and title_text[0] == 'B' and len(title_text) > 1 and title_text[1].isupper():
        doc_type = "class"
    elif any(word in title_text for word in ["Functions", "Constants", "Types", "Macros"]):
        doc_type = "globals"

    # Extract parent classes from "Derived From:" metadata item
    inherits = []
    for item in metadata_list:
        if "Derived From:" in item:
            derived_text = re.sub(r'\*\*Derived From:\*\*\s*', '', item).strip()
            links = re.findall(r'\[([^\]]+)\]\([^)]+\)', derived_text)
            if links:
                inherits = [l.strip() for l in links if l.strip()]
            else:
                inherits = [p.strip() for p in re.split(r'[,;]', derived_text) if p.strip() and len(p.strip()) < 50]
            break

    lines = ["---"]
    lines.append(f"name: {title_text}")
    lines.append(f"type: {doc_type}")
    lines.append(f"kit: {current_kit}")
    if inherits:
        lines.append("inherits:")
        for p in inherits:
            lines.append(f"  - {p}")
    lines.append("source: legacy-bebook")
    lines.append("---\n")
    return "\n".join(lines) + "\n"

def get_html(url):
    """Fetch HTML page from web (one-time crawl, no cache)."""
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        raise

def get_main_content(soup):
    """Isolate the DocBook main content container by discarding header/footers."""
    body = soup.find('body')
    if not body:
        return soup

    # Filter direct child divs
    children = [c for c in body.contents if c.name == 'div']
    content_divs = []
    for c in children:
        c_id = c.get('id', '')
        if c_id not in ['header', 'footer', 'licenseFooter']:
            content_divs.append(c)

    if len(content_divs) == 1:
        return content_divs[0]
    elif len(content_divs) > 1:
        for c in content_divs:
            c_class = c.get('class', [])
            if isinstance(c_class, str):
                c_class = [c_class]
            if any(cls in ['section', 'part', 'chapter', 'book', 'refentry'] for cls in c_class):
                return c
        return content_divs[0]
    return body

def html_to_markdown_rec(element, current_kit, file_to_folder):
    """Recursively converts BeBook XHTML elements to clean Markdown."""
    if element is None:
        return ""
    if isinstance(element, NavigableString):
        return element.string

    tag = element.name

    if tag == 'p':
        return "".join(html_to_markdown_rec(child, current_kit, file_to_folder) for child in element.children) + "\n\n"

    elif tag in ['h1', 'h2']:
        content = "".join(html_to_markdown_rec(child, current_kit, file_to_folder) for child in element.children).strip()
        return f"# {content}\n\n"

    elif tag == 'h3':
        content = "".join(html_to_markdown_rec(child, current_kit, file_to_folder) for child in element.children).strip()
        return f"## {content}\n\n"

    elif tag == 'h4':
        content = "".join(html_to_markdown_rec(child, current_kit, file_to_folder) for child in element.children).strip()
        return f"### {content}\n\n"

    elif tag in ['b', 'strong']:
        content = "".join(html_to_markdown_rec(child, current_kit, file_to_folder) for child in element.children)
        return f"**{content}**" if content.strip() else ""

    elif tag in ['i', 'em', 'var']:
        content = "".join(html_to_markdown_rec(child, current_kit, file_to_folder) for child in element.children)
        return f"*{content}*" if content.strip() else ""

    elif tag in ['code', 'tt']:
        return f"`{element.get_text()}`"

    elif tag == 'pre':
        code_text = element.get_text()
        return f"\n```cpp\n{code_text.strip()}\n```\n\n"

    elif tag == 'a':
        href = element.get('href', '')
        content = "".join(html_to_markdown_rec(child, current_kit, file_to_folder) for child in element.children).strip()
        if not content:
            return ""

        if href.startswith('http://') or href.startswith('https://') or href.startswith('mailto:'):
            return f"[{content}]({href})"

        # Internal relative link
        parsed_href = urllib.parse.urlparse(href)
        filename = os.path.basename(parsed_href.path)
        anchor = parsed_href.fragment
        anchor_suffix = f"#{anchor}" if anchor else ""

        if filename in file_to_folder:
            target_folder = file_to_folder[filename]
            md_name = filename[:-5] + ".md"
            if current_kit == target_folder:
                path = f"{md_name}{anchor_suffix}"
            else:
                path = f"../{target_folder}/{md_name}{anchor_suffix}"
            return f"[{content}]({path})"

        elif filename.endswith('.html'):
            return f"[{content}]({filename[:-5]}.md{anchor_suffix})"

        if href.startswith('#'):
            return f"[{content}]({href})"

        return f"[{content}]({href})"

    elif tag == 'br':
        return "\n"

    elif tag == 'ul':
        return "".join(html_to_markdown_rec(child, current_kit, file_to_folder) for child in element.children) + "\n"

    elif tag == 'ol':
        items = []
        idx = 1
        for child in element.children:
            if child.name == 'li':
                content = "".join(html_to_markdown_rec(c, current_kit, file_to_folder) for c in child.children).strip()
                items.append(f"{idx}. {content}\n")
                idx += 1
            else:
                items.append(html_to_markdown_rec(child, current_kit, file_to_folder))
        return "".join(items) + "\n"

    elif tag == 'li':
        content = "".join(html_to_markdown_rec(child, current_kit, file_to_folder) for child in element.children).strip()
        return f"* {content}\n"

    elif tag == 'table':
        md_rows = []
        headers = []
        for tr in element.find_all('tr'):
            ths = tr.find_all('th')
            if ths:
                headers = [html_to_markdown_rec(th, current_kit, file_to_folder).replace('\n', ' ').strip() for th in ths]
            else:
                tds = tr.find_all('td')
                if tds:
                    row_cells = [html_to_markdown_rec(td, current_kit, file_to_folder).replace('\n', ' ').strip() for td in tds]
                    md_rows.append(row_cells)
        if not headers and md_rows:
            headers = [f"Col {i+1}" for i in range(len(md_rows[0]))]
        if headers:
            divider = [":---" for _ in headers]
            header_line = "| " + " | ".join(headers) + " |"
            divider_line = "| " + " | ".join(divider) + " |"
            rows_lines = ["| " + " | ".join(r) + " |" for r in md_rows]
            return "\n" + header_line + "\n" + divider_line + "\n" + "\n".join(rows_lines) + "\n\n"

    elif tag == 'blockquote':
        content = "".join(html_to_markdown_rec(child, current_kit, file_to_folder) for child in element.children).strip()
        lines = content.split('\n')
        return "\n" + "\n".join(f"> {line}" for line in lines) + "\n\n"

    return "".join(html_to_markdown_rec(child, current_kit, file_to_folder) for child in element.children)

def extract_class_metadata(soup, current_kit, file_to_folder):
    """Parses and strips class metadata table and returns it formatted."""
    metadata = []
    
    # Locate metadata table containing 'Derived From:' or 'Declared In:'
    for table in soup.find_all('table'):
        text = table.get_text()
        if "Derived From:" in text or "Declared In:" in text:
            for tr in table.find_all('tr'):
                tds = tr.find_all('td')
                if len(tds) == 2:
                    key = tds[0].get_text().strip()
                    val_md = html_to_markdown_rec(tds[1], current_kit, file_to_folder).strip()
                    val_md = val_md.replace('\n', ' ')
                    val_md = re.sub(r'\s+', ' ', val_md)
                    if key and val_md:
                        metadata.append(f"**{key}** {val_md}")
            table.decompose()
            break
            
    # Remove redundant table of contents
    for toc in soup.find_all('div', class_='toc'):
        toc.decompose()
        
    class_overview_link = ""
    for a in soup.find_all('a', class_='overview'):
        href = a.get('href', '')
        text = a.get_text().strip()
        parsed_href = urllib.parse.urlparse(href)
        filename = os.path.basename(parsed_href.path)
        if filename in file_to_folder:
            target_folder = file_to_folder[filename]
            md_name = filename[:-5] + ".md"
            if current_kit == target_folder:
                path = md_name
            else:
                path = f"../{target_folder}/{md_name}"
            class_overview_link = f"[{text}]({path})"
        a.decompose()
        
    return metadata, class_overview_link

def convert_bebook_html(html, filename, current_kit, file_to_folder):
    """Converts BeBook page HTML to structured Markdown."""
    soup = BeautifulSoup(html, 'lxml')

    # 1. Parse and extract metadata / overview links
    metadata, class_overview = extract_class_metadata(soup, current_kit, file_to_folder)

    # 2. Extract title (needed for both frontmatter and heading)
    title_el = soup.find('title')
    title_text = title_el.get_text().strip() if title_el else filename[:-5]
    title_text = title_text.replace("The Be Book - Classes And Methods - ", "").replace("The Be Book - ", "").strip()

    # 3. Extract main content
    content_area = get_main_content(soup)

    # 4. Convert body to Markdown
    md_body = html_to_markdown_rec(content_area, current_kit, file_to_folder)

    md = []
    md.append(build_frontmatter(metadata, title_text, current_kit))

    if not md_body.lstrip().startswith('#'):
        md.append(f"# {title_text}\n\n")

    if metadata:
        md.append("\n".join(metadata) + "\n\n")
    if class_overview:
        md.append(f"{class_overview}\n\n")

    md.append(md_body.strip() + "\n\n")
    md.append(f"Generated from the [legacy BeBook API docs]({BASE_URL}{filename}).\n")
    return "".join(md), title_text

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Convert BeBook documentation to Markdown.")
    parser.add_argument("--single", type=str, help="Convert a single file and print it.")
    args = parser.parse_args()

    if args.single:
        print(f"Single file mode: {args.single}")
        try:
            html = get_html(urllib.parse.urljoin(BASE_URL, args.single))
            md, _ = convert_bebook_html(html, args.single, "test_kit", {})
            print(md[:3000])
            print("... (truncated) ...")
        except Exception as e:
            print("Error:", e)
        return

    # 1. Fetch main index page
    print("Fetching BeBook index page...")
    index_html = get_html(urllib.parse.urljoin(BASE_URL, "index.html"))
    soup = BeautifulSoup(index_html, 'lxml')

    special_topics = set()
    kits_to_scan = []

    # Identify special topics and kits from the index page
    special_topic_candidates = [
        "LegalNotice.html", "TheBeBook_Introduction.html", "SystemOverview.html", 
        "ClassesAndMethod.html", "ClassIndex.html"
    ]
    for candidate in special_topic_candidates:
        special_topics.add(candidate)

    for a in soup.find_all('a'):
        href = a.get('href', '')
        if href and not href.startswith('http') and not href.startswith('#'):
            clean_href = href.split('#')[0]
            if clean_href in BE_KIT_MAP:
                if clean_href not in kits_to_scan:
                    kits_to_scan.append(clean_href)
            elif clean_href.endswith('.html') and clean_href != "index.html":
                special_topics.add(clean_href)

    print(f"Found {len(kits_to_scan)} Kits and {len(special_topics)} special topics candidates.")

    # 2. Map kit classes and helper files by scanning kit landing pages
    file_to_folder = {}
    
    for filename in special_topics:
        file_to_folder[filename] = "special_topics"
    for kit_file, folder in BE_KIT_MAP.items():
        file_to_folder[kit_file] = folder

    def scan_kit(kit_file):
        folder = BE_KIT_MAP[kit_file]
        url = urllib.parse.urljoin(BASE_URL, kit_file)
        try:
            kit_html = get_html(url)
            kit_soup = BeautifulSoup(kit_html, 'lxml')
            files = []
            for a in kit_soup.find_all('a'):
                href = a.get('href', '')
                if href and not href.startswith('http') and not href.startswith('#'):
                    clean_href = href.split('#')[0]
                    if clean_href not in ["index.html", "LegalNotice.html", "ClassesAndMethod.html", "ClassIndex.html"]:
                        files.append(clean_href)
            return folder, set(files)
        except Exception as e:
            print(f"Error scanning kit page {kit_file}: {e}")
            return folder, set()

    print("Scanning Kit class list pages in parallel...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(scan_kit, f) for f in kits_to_scan]
        for future in concurrent.futures.as_completed(futures):
            folder, files = future.result()
            for filename in files:
                file_to_folder[filename] = folder

    # Map overview files to the correct kit directory
    for filename in list(special_topics):
        if filename.endswith('_Overview.html'):
            base_kit_name = filename.replace('_Overview.html', '.html')
            if base_kit_name in BE_KIT_MAP:
                folder = BE_KIT_MAP[base_kit_name]
                file_to_folder[filename] = folder
                special_topics.discard(filename)

    print(f"Total mapped BeBook files: {len(file_to_folder)}")

    # 3. Process and convert all mapped targets in parallel
    targets = [(filename, folder) for filename, folder in file_to_folder.items()]
    print(f"Converting {len(targets)} pages to Markdown...")

    written_count = 0

    index_entries = []

    def process_target(filename, folder):
        url = urllib.parse.urljoin(BASE_URL, filename)
        try:
            html = get_html(url)
            md_content, title_text = convert_bebook_html(html, filename, folder, file_to_folder)

            md_name = filename[:-5] + ".md"
            rel_path = os.path.join(folder, md_name).replace('\\', '/')
            full_path = os.path.join(OUTPUT_DIR, folder, md_name)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)

            with open(full_path, "w", encoding="utf-8") as f:
                f.write(md_content)
            return filename, folder, True, title_text, rel_path
        except Exception as e:
            print(f"Error converting {filename}: {e}", file=sys.stderr)
            return filename, folder, False, "", ""

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(process_target, name, folder) for name, folder in targets]
        for future in concurrent.futures.as_completed(futures):
            name, folder, success, title_text, rel_path = future.result()
            if success:
                written_count += 1
                if title_text:
                    index_entries.append({'name': title_text, 'kit': folder, 'path': rel_path})

    print(f"\nSuccessfully generated {written_count} Markdown files in `legacy-bebook-md/`.")

    # Write INDEX.md
    if index_entries:
        index_lines = [
            "# Legacy BeBook API Index\n\n",
            "| Name | Kit | File |\n",
            "| :--- | :--- | :--- |\n",
        ]
        for entry in sorted(index_entries, key=lambda x: x.get('name', '').lower()):
            name = entry['name']
            kit = entry['kit']
            path = entry['path']
            index_lines.append(f"| [{name}]({path}) | {kit} | {path} |\n")
        index_path = os.path.join(OUTPUT_DIR, "INDEX.md")
        with open(index_path, 'w', encoding='utf-8') as f:
            f.writelines(index_lines)
        print(f"Generated INDEX.md with {len(index_entries)} entries.")

if __name__ == "__main__":
    main()
