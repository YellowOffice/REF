import os
import sys
import re
import json
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup, NavigableString
import concurrent.futures
import difflib

# Configuration
BASE_URL = "https://www.haiku-os.org/docs/api/"
WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(WORKSPACE_DIR, "haiku-book-md")
CACHE_DIR = os.path.join(OUTPUT_DIR, ".cache_html")
METADATA_FILE = os.path.join(OUTPUT_DIR, "metadata.json")

# Ensure folders exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)

# Kit mapping
KIT_MAP = {
    "group__support.html": "support_kit",
    "group__app.html": "application_kit",
    "group__interface.html": "interface_kit",
    "group__storage.html": "storage_kit",
    "group__device.html": "device_kit",
    "group__game.html": "game_kit",
    "group__locale.html": "locale_kit",
    "group__mail.html": "mail_kit",
    "group__media.html": "media_kit",
    "group__midi2.html": "midi_2_kit",
    "group__network.html": "network_kit",
    "group__translation.html": "translation_kit",
    "group__netservices.html": "netservices_kit",
    "group__libroot.html": "libroot"
}

def get_html(url, force_network=False):
    """Fetch HTML page, utilizing local cache if available."""
    parsed = urllib.parse.urlparse(url)
    filename = os.path.basename(parsed.path)
    if not filename:
        filename = "index.html"
    
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

def parse_signature(proto_div):
    """Extract and format C++ function signature from Doxygen's memproto."""
    table = proto_div.find('table', class_='memname')
    if not table:
        return proto_div.get_text().strip()
    
    lines = []
    for row in table.find_all('tr'):
        cells = [c.get_text().strip() for c in row.find_all(['td', 'th'])]
        cells = [c.replace('\xa0', ' ') for c in cells]
        cells = [c for c in cells if c]
        if cells:
            lines.append(" ".join(cells))
            
    sig = " ".join(lines)
    # Cleanup signature whitespace
    sig = re.sub(r'\s*\(\s*', '(', sig)
    sig = re.sub(r'\s*\)\s*', ')', sig)
    sig = re.sub(r'\s*,\s*', ', ', sig)
    sig = re.sub(r'\s+const\b', ' const', sig)
    return sig

def html_to_markdown_rec(element, current_kit, class_to_kit, special_topics):
    """Recursively convert HTML element to clean Markdown representation."""
    if element is None:
        return ""
    if isinstance(element, NavigableString):
        s = element.string
        # Skip stray "fragment" text nodes that Doxygen leaves adjacent to code block divs
        if s and s.strip() == 'fragment':
            return ""
        return s

    tag = element.name
    
    # Ignore Doxygen code tooltip blocks
    if tag == 'div' and 'ttc' in element.get('class', []):
        return ""
        
    # Handle block elements
    if tag == 'p':
        return "".join(html_to_markdown_rec(child, current_kit, class_to_kit, special_topics) for child in element.children) + "\n\n"
        
    elif tag in ['b', 'strong']:
        content = "".join(html_to_markdown_rec(child, current_kit, class_to_kit, special_topics) for child in element.children)
        return f"**{content}**" if content.strip() else ""
        
    elif tag in ['i', 'em']:
        content = "".join(html_to_markdown_rec(child, current_kit, class_to_kit, special_topics) for child in element.children)
        return f"*{content}*" if content.strip() else ""
        
    elif tag in ['code', 'tt']:
        return f"`{element.get_text()}`"
        
    elif tag == 'a':
        href = element.get('href', '')
        content = "".join(html_to_markdown_rec(child, current_kit, class_to_kit, special_topics) for child in element.children).strip()
        if not content:
            return ""
            
        if href.startswith('http://') or href.startswith('https://') or href.startswith('mailto:'):
            return f"[{content}]({href})"
            
        # Internal relative link
        filename, _, anchor = href.partition('#')
        anchor_suffix = f"#{anchor}" if anchor else ""
        
        if filename in class_to_kit:
            target_kit = class_to_kit[filename]
            if current_kit == target_kit:
                path = f"{filename[:-5]}.md{anchor_suffix}"
            else:
                path = f"../{target_kit}/{filename[:-5]}.md{anchor_suffix}"
            return f"[{content}]({path})"
            
        elif filename in special_topics:
            if current_kit == "special_topics":
                path = f"{filename[:-5]}.md{anchor_suffix}"
            else:
                path = f"../special_topics/{filename[:-5]}.md{anchor_suffix}"
            return f"[{content}]({path})"
            
        elif filename.endswith('.html'):
            # Fallback for generic relative HTML link
            return f"[{content}]({filename[:-5]}.md{anchor_suffix})"
            
        # Local anchor link
        if href.startswith('#'):
            return f"[{content}]({href})"
            
        return f"[{content}]({href})"
        
    elif tag == 'br':
        return "\n"
        
    elif tag == 'ul':
        return "".join(html_to_markdown_rec(child, current_kit, class_to_kit, special_topics) for child in element.children) + "\n"
        
    elif tag == 'ol':
        # Handled in li context or raw sequence
        items = []
        idx = 1
        for child in element.children:
            if child.name == 'li':
                content = "".join(html_to_markdown_rec(c, current_kit, class_to_kit, special_topics) for c in child.children).strip()
                items.append(f"{idx}. {content}\n")
                idx += 1
            else:
                items.append(html_to_markdown_rec(child, current_kit, class_to_kit, special_topics))
        return "".join(items) + "\n"
        
    elif tag == 'li':
        content = "".join(html_to_markdown_rec(child, current_kit, class_to_kit, special_topics) for child in element.children).strip()
        return f"* {content}\n"
        
    elif tag == 'div' and 'fragment' in element.get('class', []):
        code_text = element.get_text()
        return f"\n```cpp\n{code_text.strip()}\n```\n\n"
        
    elif tag == 'table' and 'params' in element.get('class', []):
        rows = []
        for tr in element.find_all('tr'):
            paramname_td = tr.find('td', class_='paramname')
            if paramname_td:
                desc_td = paramname_td.find_next_sibling('td')
                name = paramname_td.get_text().strip()
                desc = html_to_markdown_rec(desc_td, current_kit, class_to_kit, special_topics) if desc_td else ''
                desc = desc.replace('\n', ' ').strip()
                rows.append(f"| `{name}` | {desc} |")
        if rows:
            return "\n| Parameter | Description |\n| :--- | :--- |\n" + "\n".join(rows) + "\n\n"
        return ''
        
    elif tag == 'dl':
        cls = element.get('class', [])
        if isinstance(cls, str):
            cls = [cls]
        
        is_alert = False
        alert_type = None
        
        if 'section' in cls or any(c.startswith('section') for c in cls):
            for c in cls:
                if c == 'warning':
                    alert_type = 'WARNING'
                    is_alert = True
                elif c == 'note':
                    alert_type = 'NOTE'
                    is_alert = True
                elif c in ['attention', 'important']:
                    alert_type = 'IMPORTANT'
                    is_alert = True
                elif c == 'return':
                    dd = element.find('dd')
                    dd_text = html_to_markdown_rec(dd, current_kit, class_to_kit, special_topics) if dd else ''
                    return f"\n**Returns:** {dd_text.strip()}\n\n"
                elif c == 'since':
                    dd = element.find('dd')
                    dd_text = html_to_markdown_rec(dd, current_kit, class_to_kit, special_topics) if dd else ''
                    return f"\n**Since:** {dd_text.strip()}\n\n"
                elif c == 'see':
                    dd = element.find('dd')
                    dd_text = html_to_markdown_rec(dd, current_kit, class_to_kit, special_topics) if dd else ''
                    return f"\n**See also:** {dd_text.strip()}\n\n"
                    
        if is_alert and alert_type:
            dd = element.find('dd')
            dd_text = html_to_markdown_rec(dd, current_kit, class_to_kit, special_topics) if dd else ''
            lines = dd_text.strip().split('\n')
            formatted_lines = [f"> {line}" for line in lines]
            return f"\n> [!{alert_type}]\n" + "\n".join(formatted_lines) + "\n\n"
            
    elif tag == 'table':
        md_rows = []
        headers = []
        for tr in element.find_all('tr'):
            ths = tr.find_all('th')
            if ths:
                headers = [html_to_markdown_rec(th, current_kit, class_to_kit, special_topics).replace('\n', ' ').strip() for th in ths]
            else:
                tds = tr.find_all('td')
                if tds:
                    row_cells = [html_to_markdown_rec(td, current_kit, class_to_kit, special_topics).replace('\n', ' ').strip() for td in tds]
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
        content = "".join(html_to_markdown_rec(child, current_kit, class_to_kit, special_topics) for child in element.children).strip()
        lines = content.split('\n')
        return "\n" + "\n".join(f"> {line}" for line in lines) + "\n\n"
        
    # Default: process children recursively
    return "".join(html_to_markdown_rec(child, current_kit, class_to_kit, special_topics) for child in element.children)

def extract_brief(textblock):
    """Return the first sentence of a Doxygen textblock element as a plain string."""
    if not textblock:
        return ""
    first_p = textblock.find('p')
    if not first_p:
        return ""
    text = first_p.get_text().strip()
    match = re.search(r'^(.+?[.!?])(?:\s|$)', text)
    if match:
        return match.group(1).rstrip('.')
    return text[:120].strip()

def extract_inherits(soup):
    """Return list of parent class names found in memberdecls 'inherited from' headings."""
    inherits = []
    seen = set()
    for table in soup.find_all('table', class_='memberdecls'):
        for el in table.find_all(class_='groupheader'):
            text = el.get_text()
            m = re.search(r'inherited from (\w+)', text, re.IGNORECASE)
            if m:
                parent = m.group(1)
                if parent not in seen:
                    seen.add(parent)
                    inherits.append(parent)
    return inherits

def build_frontmatter(soup, title_text, kit):
    """Return a YAML frontmatter block string for a Haiku Book API page."""
    if " Class" in title_text:
        doc_type = "class"
        name = title_text.replace(" Class", "").strip()
    elif " Struct" in title_text:
        doc_type = "struct"
        name = title_text.replace(" Struct", "").strip()
    elif " Union" in title_text:
        doc_type = "union"
        name = title_text.replace(" Union", "").strip()
    else:
        doc_type = "topic"
        name = title_text

    brief = extract_brief(soup.find('div', class_='textblock'))
    inherits = extract_inherits(soup)

    lines = ["---"]
    lines.append(f"name: {name}")
    lines.append(f"type: {doc_type}")
    lines.append(f"kit: {kit}")
    if brief:
        lines.append(f'brief: "{brief.replace(chr(34), chr(92) + chr(34))}"')
    if inherits:
        lines.append("inherits:")
        for p in inherits:
            lines.append(f"  - {p}")
    lines.append("source: haiku-book")
    lines.append("---\n")
    return "\n".join(lines) + "\n"

def parse_frontmatter(content):
    """Extract scalar YAML frontmatter values from a markdown string (no external deps)."""
    if not content.startswith("---"):
        return {}
    end = content.find("\n---\n", 4)
    if end == -1:
        return {}
    result = {}
    for line in content[4:end].split("\n"):
        if ":" in line and not line.startswith(" "):
            key, _, val = line.partition(":")
            result[key.strip()] = val.strip().strip('"')
    return result

def convert_class_or_topic_html(html, filename, current_kit, class_to_kit, special_topics):
    """Converts a class or topic Doxygen page HTML to Markdown string."""
    soup = BeautifulSoup(html, 'lxml')
    
    # Remove all Doxygen tooltip definition blocks to avoid polluting code fragments and descriptions
    for ttc in soup.find_all('div', class_='ttc'):
        ttc.decompose()
    
    # 1. Title
    title_el = soup.find('title')
    title_text = title_el.get_text() if title_el else filename[:-5]
    if "Class Reference" in title_text:
        title_text = title_text.replace("Class Reference", "").replace("The Haiku Book:", "").strip() + " Class"
    elif "Struct Reference" in title_text:
        title_text = title_text.replace("Struct Reference", "").replace("The Haiku Book:", "").strip() + " Struct"
    else:
        title_text = title_text.replace("The Haiku Book:", "").strip()
        
    md = []
    md.append(build_frontmatter(soup, title_text, current_kit))
    md.append(f"# {title_text}\n")

    contents_div = soup.find('div', class_='contents')
    if not contents_div:
        # Fallback to body
        contents_div = soup.find('body')
        
    if not contents_div:
        return f"# {title_text}\n\nCould not extract contents."

    # Breadcrumbs / groups
    ingroups_div = soup.find('div', class_='ingroups')
    if ingroups_div:
        group_links = []
        for a in ingroups_div.find_all('a'):
            g_href = a.get('href', '')
            g_text = a.get_text().strip()
            g_filename = g_href.split('#')[0]
            clean_g_filename = g_filename[:-5]
            if g_filename in KIT_MAP:
                target_kit = KIT_MAP[g_filename]
                path = f"../{target_kit}/{clean_g_filename}.md"
                group_links.append(f"[{g_text}]({path})")
            else:
                group_links.append(f"[{g_text}]({g_filename[:-5]}.md)")
        if group_links:
            md.append("**Kit/Group:** " + " | ".join(group_links) + "\n\n")

    # Detailed Description
    textblock = contents_div.find('div', class_='textblock')
    if textblock:
        desc_md = html_to_markdown_rec(textblock, current_kit, class_to_kit, special_topics)
        md.append("## Description\n\n" + desc_md.strip() + "\n\n")
        
    # Member tables (Declarations) - summary listing
    memberdecls = contents_div.find_all('table', class_='memberdecls')
    if memberdecls:
        md.append("## Member List\n\n")
        for table in memberdecls:
            current_section = "Members"
            rows = table.find_all('tr', recursive=False)
            if not rows:
                tbody = table.find('tbody', recursive=False)
                if tbody:
                    rows = tbody.find_all('tr', recursive=False)
                else:
                    rows = table.find_all('tr')
            
            i = 0
            while i < len(rows):
                tr = rows[i]
                r_class = tr.get('class', [])
                if isinstance(r_class, str):
                    r_class = [r_class]
                    
                if 'heading' in r_class or tr.find('h2', class_='groupheader'):
                    h2_el = tr.find(['h2', 'td'])
                    current_section = h2_el.get_text().strip() if h2_el else "Members"
                    current_section = re.sub(r'\s*\[\s*\d+\s*/\s*\d+\s*\]\s*', '', current_section)
                    md.append(f"### {current_section}\n\n")
                    i += 1
                elif 'memitem' in r_class or any(c.startswith('memitem') for c in r_class):
                    left_td = tr.find('td', class_='memItemLeft')
                    right_td = tr.find('td', class_='memItemRight')
                    
                    type_txt = ""
                    if left_td:
                        type_txt = left_td.get_text().replace('\xa0', ' ').strip()
                        type_txt = re.sub(r'\s+', ' ', type_txt)
                        
                    name_txt = ""
                    if right_td:
                        a_el = right_td.find('a')
                        if a_el:
                            href = a_el.get('href', '')
                            anchor = f"#{href.split('#')[-1]}" if '#' in href else f"#{a_el.get_text().strip()}"
                            full_right_text = right_td.get_text().strip().replace('\xa0', ' ')
                            link_text = a_el.get_text().strip()
                            escaped_link_text = re.escape(link_text)
                            name_txt = re.sub(escaped_link_text, f"[{link_text}]({anchor})", full_right_text, count=1)
                        else:
                            name_txt = right_td.get_text().strip().replace('\xa0', ' ')
                    
                    brief_txt = ""
                    if i + 1 < len(rows):
                        next_tr = rows[i+1]
                        next_class = next_tr.get('class', [])
                        if isinstance(next_class, str):
                            next_class = [next_class]
                        if 'memdesc' in next_class or any(c.startswith('memdesc') for c in next_class):
                            desc_td = next_tr.find('td', class_='mdescRight')
                            if desc_td:
                                brief_txt = desc_td.get_text().strip().replace('\xa0', ' ')
                                brief_txt = re.sub(r'\s*More\.\.\.\s*$', '', brief_txt).strip()
                            i += 1
                            
                    type_prefix = f"`{type_txt}` " if type_txt else ""
                    brief_suffix = f" — {brief_txt}" if brief_txt else ""
                    md.append(f"* {type_prefix}{name_txt}{brief_suffix}\n")
                    i += 1
                else:
                    i += 1
            md.append("\n")

    # Detailed Member documentation
    memitems = contents_div.find_all('div', class_='memitem')
    if memitems:
        md.append("## Detailed Member Documentation\n\n")
        for item in memitems:
            proto = item.find('div', class_='memproto')
            doc = item.find('div', class_='memdoc')
            
            # Find the header title anchor name if any
            h2 = item.find_previous_sibling('h2', class_='memtitle')
            anchor_name = ""
            if h2:
                # Doxygen headers have title like "Unlock()"
                h2_text = h2.get_text().strip()
                # Remove permalink marker if present
                h2_text = h2_text.replace('◆', '').replace('⚓', '').strip()
                # Clean up overload suffix
                h2_text = re.sub(r'\s*\[\s*\d+\s*/\s*\d+\s*\]\s*', '', h2_text)
                anchor_name = h2_text
                md.append(f"### `{anchor_name}`\n\n")
            else:
                # Generate a generic header
                md.append("### Member Detail\n\n")
                
            if proto:
                sig = parse_signature(proto)
                md.append(f"```cpp\n{sig}\n```\n\n")
                
            if doc:
                doc_md = html_to_markdown_rec(doc, current_kit, class_to_kit, special_topics)
                md.append(doc_md.strip() + "\n\n")
                
            md.append("---\n\n")

    # If both textblock and memitems are missing, convert the whole contents recursively
    if not textblock and not memitems:
        raw_body_md = html_to_markdown_rec(contents_div, current_kit, class_to_kit, special_topics)
        md.append(raw_body_md.strip() + "\n\n")

    # Add footer
    md.append("Generated from the [Haiku Book API docs]({}{}).\n".format(BASE_URL, filename))
    
    return "".join(md)

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Convert Haiku Doxygen HTML documentation to Markdown.")
    parser.add_argument("--force", action="store_true", help="Force rebuild of documentation regardless of timestamp.")
    parser.add_argument("--single", type=str, help="Process only a single HTML file (e.g. classBLocker.html) and print it.")
    parser.add_argument("--dry-run", action="store_true", help="Run the parser but do not write any Markdown files.")
    parser.add_argument("--kit", type=str, help="Process only a specific kit group ID (e.g. group__support).")
    args = parser.parse_args()

    # If single file mode
    if args.single:
        # Load and parse single file
        print(f"Single file mode: {args.single}")
        try:
            # Let's map target kit mock
            html = get_html(urllib.parse.urljoin(BASE_URL, args.single))
            md_content = convert_class_or_topic_html(html, args.single, "test_kit", {}, {})
            print(md_content[:3000])
            print("... (truncated) ...")
        except Exception as e:
            print("Error processing single file:", e)
        return

    # 1. Fetch main page and get timestamp
    print("Fetching Haiku Book main page...")
    main_html = get_html(BASE_URL, force_network=True)
    
    # Search for Doxygen footer generation timestamp
    timestamp_match = re.search(r'Generated on\s+([A-Za-z0-9\s:]+?)\s+by\s+<a href="http://www.doxygen.org/index.html">Doxygen</a>', main_html)
    timestamp = timestamp_match.group(1).strip() if timestamp_match else "Unknown Date"
    print(f"Remote Documentation Generation Date: {timestamp}")

    # Check stored metadata
    metadata = {}
    if os.path.exists(METADATA_FILE):
        try:
            with open(METADATA_FILE, "r", encoding="utf-8") as f:
                metadata = json.load(f)
        except Exception:
            pass

    stored_timestamp = metadata.get("timestamp")
    print(f"Stored Documentation Date: {stored_timestamp}")

    if not args.force and stored_timestamp == timestamp:
        print("Haiku Book is up to date. No changes to apply.")
        return

    # 2. Discover Kits & Special Topics from main page
    print("Parsing index page for Kits and Topics...")
    soup = BeautifulSoup(main_html, 'lxml')
    kits = []
    special_topics = set()
    
    # Special topics on main page to extract
    special_topic_filenames = [
        "apidoc.html", "credits.html", "compatibility.html", 
        "layout_intro.html", "keyboard.html", "json.html", 
        "drivers.html", "midi1.html"
    ]
    for filename in special_topic_filenames:
        special_topics.add(filename)

    for a in soup.find_all('a'):
        href = a.get('href', '')
        text = a.get_text().strip()
        if href.startswith('group__') and href.endswith('.html'):
            clean_href = href.split('#')[0]
            kits.append((clean_href, text))

    print(f"Found {len(kits)} Kits and {len(special_topics)} Special Topics.")

    # If a specific kit is filtered
    if args.kit:
        kits = [(href, text) for href, text in kits if href.startswith(args.kit)]
        print(f"Filtered to Kit: {kits}")

    # 3. Scan kit pages to map classes/structs to kits
    print("Crawling Kit pages to locate classes...")
    class_to_kit = {}
    kit_contents = {} # kit_name -> list of files inside it
    
    # We fetch kit pages in parallel
    def fetch_kit_details(kit_href, kit_title):
        url = urllib.parse.urljoin(BASE_URL, kit_href)
        try:
            k_html = get_html(url)
            k_soup = BeautifulSoup(k_html, 'lxml')
            files = []
            for a in k_soup.find_all('a'):
                href = a.get('href', '')
                if href.endswith('.html') and (href.startswith('class') or href.startswith('struct') or href.startswith('union') or 'globals' in href):
                    clean_href = href.split('#')[0]
                    # Exclude the group/kit page itself
                    if clean_href != kit_href:
                        files.append(clean_href)
            return kit_href, kit_title, set(files)
        except Exception as e:
            print(f"Error fetching kit details for {kit_title}: {e}")
            return kit_href, kit_title, set()

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(fetch_kit_details, href, title) for href, title in kits]
        for future in concurrent.futures.as_completed(futures):
            href, title, files = future.result()
            kit_dir = KIT_MAP.get(href, "unknown_kit")
            if kit_dir not in kit_contents:
                kit_contents[kit_dir] = []
            
            for filename in files:
                # Initialize class-to-kit mapping
                # In case a class is in multiple kits, we map it to the first one we find
                # later, when we download the class page itself, we will check if it has a specific ingroup and update
                if filename not in class_to_kit:
                    class_to_kit[filename] = kit_dir

    print(f"Total mapped classes/structs/globals: {len(class_to_kit)}")

    # 4. Fetch and Parse all classes/topics in parallel
    all_targets = [] # list of (filename, type, target_dir)
    
    for filename in special_topics:
        all_targets.append((filename, "topic", "special_topics"))
        
    for filename, kit_dir in class_to_kit.items():
        all_targets.append((filename, "class_or_globals", kit_dir))

    # A dictionary to track output paths and their generated contents
    markdown_outputs = {} # relative_path -> content

    def process_target(filename, file_type, default_dir):
        url = urllib.parse.urljoin(BASE_URL, filename)
        try:
            html = get_html(url)
            
            # Determine actual kit if there's an ingroups header in Doxygen page
            actual_dir = default_dir
            if file_type == "class_or_globals":
                # Quickly inspect HTML for ingroups
                # E.g. <div class="ingroups"><a class="el" href="group__support.html">
                soup = BeautifulSoup(html, 'lxml')
                ingroups = soup.find('div', class_='ingroups')
                if ingroups:
                    for a in ingroups.find_all('a'):
                        g_href = a.get('href', '').split('#')[0]
                        if g_href in KIT_MAP:
                            actual_dir = KIT_MAP[g_href]
                            break
            
            # Parse HTML to Markdown
            md_content = convert_class_or_topic_html(html, filename, actual_dir, class_to_kit, special_topics)
            
            # Form clean markdown filename
            md_filename = filename[:-5] + ".md" # replace .html with .md
            # E.g. classBLocker.html -> BLocker.md
            if md_filename.startswith("class"):
                md_filename = md_filename[5:]
            elif md_filename.startswith("struct"):
                md_filename = md_filename[6:]
            elif md_filename.startswith("union"):
                md_filename = md_filename[5:]
            elif md_filename.startswith("group__") and md_filename.endswith("__globals"):
                # E.g. group__support__globals.md -> globals.md
                md_filename = "globals.md"
                
            rel_path = os.path.join(actual_dir, md_filename)
            meta = parse_frontmatter(md_content)
            meta['path'] = rel_path.replace('\\', '/')
            return rel_path, md_content, meta
        except Exception as e:
            print(f"Error processing {filename}: {e}", file=sys.stderr)
            return None

    failures = 0
    index_entries = []
    print(f"Processing and parsing {len(all_targets)} documentation pages...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(process_target, filename, file_type, default_dir) for filename, file_type, default_dir in all_targets]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                rel_path, content, meta = result
                markdown_outputs[rel_path] = content
                if meta:
                    index_entries.append(meta)
            else:
                failures += 1

    # 5. Write outputs differentially and compute diffs
    print(f"Generating Markdown files...")
    written_count = 0
    updated_count = 0
    unchanged_count = 0
    
    updated_files = []

    # Map outputs to files
    for rel_path, content in markdown_outputs.items():
        full_path = os.path.join(OUTPUT_DIR, rel_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        # Check if file exists and has same content
        if os.path.exists(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
                old_content = f.read()
            
            if old_content == content:
                unchanged_count += 1
                continue
                
            # Content changed
            updated_count += 1
            updated_files.append(rel_path)
            
            # Generate diff snippet for log
            diff = difflib.unified_diff(
                old_content.splitlines(), 
                content.splitlines(), 
                fromfile=f"a/{rel_path}", 
                tofile=f"b/{rel_path}",
                lineterm=""
            )
            diff_text = "\n".join(list(diff)[:15]) # limit to first 15 lines of diff
            
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
            # New file
            written_count += 1
            if not args.dry_run:
                with open(full_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"CREATED: {rel_path}")
            else:
                print(f"DRY-RUN CREATED: {rel_path}")

    # Remove any extra md files in the target directories that are no longer part of our documentation
    # (Exclude metadata.json and other files)
    if failures == 0 and len(all_targets) > 0:
        active_relative_paths = set(p.replace('\\', '/') for p in markdown_outputs.keys())
        for root, dirs, files in os.walk(OUTPUT_DIR):
            # Skip cache folder
            if ".cache_html" in root:
                continue
            for file in files:
                if file.endswith(".md") and file != "INDEX.md":
                    full_file_path = os.path.join(root, file)
                    rel_file_path = os.path.relpath(full_file_path, OUTPUT_DIR).replace('\\', '/')
                    if rel_file_path not in active_relative_paths:
                        print(f"DELETED: {rel_file_path} (no longer in remote documentation)")
                        if not args.dry_run:
                            os.remove(full_file_path)
    else:
        if failures > 0:
            print(f"Skipping obsolete file cleanup because {failures} page(s) failed to download.")
        else:
            print("Skipping obsolete file cleanup because no documentation pages were discovered.")

    print("\nSummary:")
    print(f"  Created: {written_count}")
    print(f"  Updated: {updated_count}")
    print(f"  Unchanged: {unchanged_count}")
    
    # 6. Write INDEX.md — flat lookup table for all classes/topics
    if index_entries and not args.dry_run:
        index_lines = [
            "# Haiku Book API Index\n\n",
            f"Generated from Haiku documentation dated {timestamp}.\n\n",
            "| Name | Type | Kit | Brief |\n",
            "| :--- | :--- | :--- | :--- |\n",
        ]
        for entry in sorted(index_entries, key=lambda x: x.get('name', '').lower()):
            name = entry.get('name', '?')
            etype = entry.get('type', '?')
            kit = entry.get('kit', '?')
            brief = entry.get('brief', '')
            path = entry.get('path', '')
            index_lines.append(f"| [{name}]({path}) | {etype} | {kit} | {brief} |\n")
        index_path = os.path.join(OUTPUT_DIR, "INDEX.md")
        with open(index_path, 'w', encoding='utf-8') as f:
            f.writelines(index_lines)
        print(f"Generated INDEX.md with {len(index_entries)} entries.")

    # 7. Save metadata
    if not args.dry_run:
        metadata = {
            "timestamp": timestamp,
            "files": list(active_relative_paths)
        }
        with open(METADATA_FILE, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)
        print(f"Updated metadata timestamp: {timestamp}")

if __name__ == "__main__":
    main()
