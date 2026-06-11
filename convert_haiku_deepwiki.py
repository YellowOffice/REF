import os
import sys
import re
import json
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import concurrent.futures
import difflib

# Configuration
BASE_URL = "https://deepwiki.com/haiku/haiku"
WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(WORKSPACE_DIR, "haiku-deepwiki-md")
CACHE_DIR = os.path.join(OUTPUT_DIR, ".cache_html")
METADATA_FILE = os.path.join(OUTPUT_DIR, "metadata.json")

# Ensure folders exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)

def get_html(url, force_network=False):
    """Fetch HTML page, utilizing local cache if available."""
    parsed = urllib.parse.urlparse(url)
    # The path will be like /haiku/haiku/slug
    # Let's derive a safe filename
    path_parts = parsed.path.strip("/").split("/")
    if len(path_parts) <= 2:
        filename = "index.html"
    else:
        filename = f"{path_parts[-1]}.html"
        
    cache_path = os.path.join(CACHE_DIR, filename)
    
    if not force_network and os.path.exists(cache_path):
        with open(cache_path, "r", encoding="utf-8") as f:
            return f.read()
            
    # Fetch from web with browser-like user agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
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

def extract_payloads_from_html(html):
    """Extract preloaded Markdown payloads from Next.js self.__next_f.push scripts."""
    soup = BeautifulSoup(html, 'lxml')
    push_payloads = []
    
    for script in soup.find_all('script'):
        content = script.get_text()
        if "self.__next_f.push" in content:
            idx = 0
            while True:
                pos = content.find("self.__next_f.push(", idx)
                if pos == -1:
                    break
                
                start_paren = pos + len("self.__next_f.push(")
                paren_count = 1
                curr = start_paren
                while curr < len(content) and paren_count > 0:
                    if content[curr] == '(':
                        paren_count += 1
                    elif content[curr] == ')':
                        paren_count -= 1
                    curr += 1
                
                if paren_count == 0:
                    arg_str = content[start_paren:curr-1].strip()
                    idx = curr
                    payload = None
                    
                    # Try parsing arg_str as a JSON list [1, "content"]
                    try:
                        arr = json.loads(arg_str)
                        if isinstance(arr, list) and len(arr) == 2 and arr[0] == 1:
                            payload = arr[1]
                    except Exception:
                        # Fallback parsing if JSON load fails directly
                        try:
                            comma_idx = arg_str.find(",")
                            if comma_idx != -1:
                                val_str = arg_str[comma_idx+1:].strip()
                                if val_str.endswith(']'):
                                    val_str = val_str[:-1].strip()
                                payload = json.loads(val_str)
                        except Exception:
                            pass
                    
                    if payload and isinstance(payload, str) and payload.strip().startswith("# "):
                        push_payloads.append(payload)
                else:
                    idx = start_paren
    return push_payloads

def normalize_title(title):
    """Normalize a title for matching, removing formatting and special characters."""
    if title.startswith("#"):
        title = title.lstrip("#").strip()
    title = title.lower()
    title = re.sub(r'[^a-z0-9]', '', title)
    return title

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Convert Haiku DeepWiki documentation to Markdown.")
    parser.add_argument("--force", action="store_true", help="Force rebuild of documentation regardless of ETag.")
    parser.add_argument("--single", type=str, help="Process only a single slug (e.g. 1-overview-of-haiku-os) and print it.")
    parser.add_argument("--dry-run", action="store_true", help="Run the script but do not write any files.")
    args = parser.parse_args()

    # Single slug mode
    if args.single:
        print(f"Single slug mode: {args.single}")
        try:
            url = f"{BASE_URL}/{args.single}"
            html = get_html(url)
            payloads = extract_payloads_from_html(html)
            
            # Find matching payload
            norm_target = normalize_title(args.single)
            matched_payload = None
            for p in payloads:
                first_line = p.strip().split("\n")[0]
                if normalize_title(first_line) == norm_target or norm_target in normalize_title(first_line) or normalize_title(first_line) in norm_target:
                    matched_payload = p
                    break
            
            if matched_payload:
                print("--- CONVERTED MARKDOWN PREVIEW ---")
                print(matched_payload[:4000])
                if len(matched_payload) > 4000:
                    print("... (truncated) ...")
            else:
                print(f"Could not find matching payload for slug '{args.single}' in fetched payloads.")
                if payloads:
                    print("Available payloads H1s:")
                    for p in payloads:
                        print("  ", repr(p.strip().split("\n")[0]))
        except Exception as e:
            print("Error processing single slug:", e)
        return

    # Check ETag via HEAD request
    print("Checking Haiku DeepWiki main page ETag...")
    etag = ""
    try:
        req = urllib.request.Request(BASE_URL, headers={'User-Agent': 'Mozilla/5.0'}, method='HEAD')
        with urllib.request.urlopen(req) as response:
            etag = response.info().get("ETag", "").strip('"')
    except Exception as e:
        print(f"HEAD request failed: {e}. Falling back to ETag verification during page fetch.")

    # Read stored metadata
    metadata = {}
    if os.path.exists(METADATA_FILE):
        try:
            with open(METADATA_FILE, "r", encoding="utf-8") as f:
                metadata = json.load(f)
        except Exception:
            pass

    stored_etag = metadata.get("etag")
    print(f"Remote ETag: {etag}")
    print(f"Stored ETag: {stored_etag}")

    if not args.force and etag and stored_etag == etag:
        print("Haiku DeepWiki documentation is up to date. No changes to apply.")
        return

    # Fetch main index page
    print("Fetching DeepWiki main index page...")
    main_html = get_html(BASE_URL, force_network=True)
    
    # If we couldn't get ETag via HEAD, read it from the GET response headers
    if not etag:
        try:
            # Re-read headers from cache or mock if caching is used
            # But since we did force_network=True, we can fetch headers if we do it inline
            # For simplicity, we just extract from the actual HTTP response inside get_html
            # Let's make get_html return etag or cache it. We'll query again if needed or use the body's Etag if we can get it.
            pass
        except Exception:
            pass

    # Crawl main page HTML to get sidebar links in order
    print("Crawling index page for sidebar links...")
    soup = BeautifulSoup(main_html, 'lxml')
    sidebar_links = [] # list of (slug, title)
    
    for a in soup.find_all('a'):
        href = a.get('href', '')
        if href.startswith('/haiku/haiku/'):
            slug = href.split('/')[-1]
            title = a.get_text().strip()
            # De-duplicate while preserving order
            if (slug, title) not in sidebar_links:
                sidebar_links.append((slug, title))

    # Identify duplicates (e.g. Navigation guides pointing to main sections)
    seen_slugs = set()
    unique_links = []
    for slug, title in sidebar_links:
        if slug not in seen_slugs:
            seen_slugs.add(slug)
            unique_links.append((slug, title))
        else:
            print(f"Skipping duplicate menu link: {slug} -> {title}")

    print(f"Discovered {len(unique_links)} unique documentation pages.")

    # Extract all preloaded payloads from index HTML
    print("Extracting preloaded payloads from index page...")
    preloaded_payloads = extract_payloads_from_html(main_html)
    print(f"Found {len(preloaded_payloads)} preloaded Markdown payloads.")

    # Map payloads to slugs by H1 title
    slug_to_markdown = {}
    remaining_links = []

    for slug, title in unique_links:
        norm_title = normalize_title(title)
        matched_payload = None
        
        for p in preloaded_payloads:
            first_line = p.strip().split("\n")[0]
            norm_first_line = normalize_title(first_line)
            # Match if normalized titles are identical or substrings of each other
            if norm_title == norm_first_line or norm_title in norm_first_line or norm_first_line in norm_title:
                matched_payload = p
                break
                
        if matched_payload:
            slug_to_markdown[slug] = matched_payload
        else:
            remaining_links.append((slug, title))

    print(f"Successfully matched {len(slug_to_markdown)} pages from preloaded payload.")

    # Fallback: fetch individual subpages for any unmatched links
    if remaining_links:
        print(f"Falling back to fetch {len(remaining_links)} unmatched pages individually...")
        
        def fetch_fallback(slug, title):
            url = f"{BASE_URL}/{slug}"
            try:
                print(f"Fetching fallback for: {slug}...")
                sub_html = get_html(url, force_network=True)
                payloads = extract_payloads_from_html(sub_html)
                norm_title = normalize_title(title)
                for p in payloads:
                    first_line = p.strip().split("\n")[0]
                    norm_first_line = normalize_title(first_line)
                    if norm_title == norm_first_line or norm_title in norm_first_line or norm_first_line in norm_title:
                        return slug, p
                # If title match failed, return the first H1 payload as fallback
                if payloads:
                    return slug, payloads[0]
            except Exception as e:
                print(f"Failed to fetch fallback for {slug}: {e}", file=sys.stderr)
            return slug, None

        failures = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(fetch_fallback, slug, title) for slug, title in remaining_links]
            for future in concurrent.futures.as_completed(futures):
                slug, markdown_text = future.result()
                if markdown_text:
                    slug_to_markdown[slug] = markdown_text
                else:
                    failures += 1

        if failures > 0:
            print(f"Warning: {failures} pages failed to download or parse.", file=sys.stderr)

    # Write files differentially
    print("Writing Markdown files...")
    written = 0
    updated = 0
    unchanged = 0
    active_paths = set()

    # Determine index page content (overview page)
    overview_slug = unique_links[0][0] if unique_links else ""
    overview_content = slug_to_markdown.get(overview_slug, "")

    for slug, title in unique_links:
        content = slug_to_markdown.get(slug)
        if not content:
            print(f"Skipping {slug} (no content found)")
            continue

        filename = f"{slug}.md"
        full_path = os.path.join(OUTPUT_DIR, filename)
        active_paths.add(filename)

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
                fromfile=f"a/{filename}",
                tofile=f"b/{filename}",
                lineterm=""
            )
            diff_text = "\n".join(list(diff)[:15])

            if not args.dry_run:
                with open(full_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"UPDATED: {filename}")
                if diff_text:
                    print("DIFF PREVIEW:\n" + diff_text + "\n" + "-"*40)
            else:
                print(f"DRY-RUN UPDATED: {filename}")
                if diff_text:
                    print("DIFF PREVIEW:\n" + diff_text + "\n" + "-"*40)
        else:
            written += 1
            if not args.dry_run:
                with open(full_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"CREATED: {filename}")
            else:
                print(f"DRY-RUN CREATED: {filename}")

    # Generate README.md containing the overview content + Table of Contents
    readme_path = os.path.join(OUTPUT_DIR, "README.md")
    active_paths.add("README.md")

    toc_lines = ["\n## Documentation Index\n", "Here is the complete list of chapters and articles available in this reference:\n"]
    for slug, title in unique_links:
        toc_lines.append(f"- [{title}]({slug}.md)")
    toc_text = "\n".join(toc_lines) + "\n"

    # README content is overview content + TOC index
    readme_content = overview_content.strip() + "\n\n" + toc_text

    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            old_readme = f.read()
        if old_readme != readme_content:
            if not args.dry_run:
                with open(readme_path, "w", encoding="utf-8") as f:
                    f.write(readme_content)
                print("UPDATED: README.md")
            else:
                print("DRY-RUN UPDATED: README.md")
        else:
            unchanged += 1
    else:
        written += 1
        if not args.dry_run:
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(readme_content)
            print("CREATED: README.md")
        else:
            print("DRY-RUN CREATED: README.md")

    # Clean up obsolete markdown files
    for file in os.listdir(OUTPUT_DIR):
        if file.endswith(".md"):
            if file not in active_paths:
                print(f"DELETED: {file} (no longer in remote documentation)")
                if not args.dry_run:
                    os.remove(os.path.join(OUTPUT_DIR, file))

    print(f"\nSummary:")
    print(f"  Created: {written}")
    print(f"  Updated: {updated}")
    print(f"  Unchanged: {unchanged}")

    # Save metadata
    if not args.dry_run:
        # Refetch headers to get the fresh ETag if we fetched index with GET
        # In get_html we fetch index page. Let's make a HEAD check to get the final ETag.
        final_etag = etag
        if not final_etag:
            try:
                req = urllib.request.Request(BASE_URL, headers={'User-Agent': 'Mozilla/5.0'}, method='HEAD')
                with urllib.request.urlopen(req) as response:
                    final_etag = response.info().get("ETag", "").strip('"')
            except Exception:
                pass
                
        metadata = {
            "etag": final_etag if final_etag else stored_etag,
            "files": list(active_paths)
        }
        with open(METADATA_FILE, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)
        print("Updated metadata.")

if __name__ == '__main__':
    main()
