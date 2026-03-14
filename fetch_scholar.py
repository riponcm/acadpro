"""
Google Scholar → data.json Updater
===================================
Fetches your publications from Google Scholar and updates data.json.
Merges with existing manual entries — never deletes your custom data.

Requirements:
    pip install scholarly

Usage:
    python fetch_scholar.py                          # uses scholarId from data.json
    python fetch_scholar.py --scholar-id "ABC123"    # specify directly

What it does:
    1. Reads your current data.json
    2. Fetches publications from Google Scholar
    3. For EXISTING papers: updates citation count only
    4. For NEW papers: adds them with Scholar data (you fill in image/thumbnail later)
    5. Saves updated data.json (backs up original as data.backup.json)
"""

import json
import sys
import os
import shutil
import argparse
from datetime import datetime

try:
    from scholarly import scholarly
except ImportError:
    print("Install scholarly first:")
    print("  pip install scholarly")
    sys.exit(1)


DATA_FILE = "data.json"
BACKUP_FILE = "data.backup.json"
PLACEHOLDER_IMAGE = "https://images.unsplash.com/photo-1532094349884-543bc11b234d?w=600&h=300&fit=crop"
PLACEHOLDER_THUMB = "https://images.unsplash.com/photo-1532094349884-543bc11b234d?w=200&h=200&fit=crop"


def load_data():
    """Load existing data.json."""
    if not os.path.exists(DATA_FILE):
        print(f"Error: {DATA_FILE} not found.")
        sys.exit(1)
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    """Backup and save data.json."""
    if os.path.exists(DATA_FILE):
        shutil.copy2(DATA_FILE, BACKUP_FILE)
        print(f"  Backed up to {BACKUP_FILE}")
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  Saved {DATA_FILE}")


def normalize_title(title):
    """Normalize title for matching."""
    return title.lower().strip().rstrip(".")


def guess_type(venue):
    """Guess publication type from venue name."""
    v = venue.lower()
    if any(k in v for k in ["journal", "transactions", "letters", "review"]):
        return "journal"
    if any(k in v for k in ["workshop", "w/"]):
        return "workshop"
    return "conference"


def format_bibtex(pub):
    """Generate a simple BibTeX entry."""
    authors = pub.get("bib", {}).get("author", "Unknown")
    title = pub.get("bib", {}).get("title", "Untitled")
    year = pub.get("bib", {}).get("pub_year", "????")
    venue = pub.get("bib", {}).get("venue", "")
    citation = pub.get("bib", {}).get("citation", "")

    key = authors.split(" ")[0].lower() + str(year)
    bib_type = "article" if "journal" in (venue + citation).lower() else "inproceedings"

    return f"@{bib_type}{{{key},title={{{title}}},author={{{authors}}},year={{{year}}}}}"


def fetch_scholar_publications(scholar_id):
    """Fetch publications from Google Scholar."""
    print(f"\nFetching publications for Scholar ID: {scholar_id}")
    print("  (This may take 30-60 seconds due to rate limiting...)\n")

    try:
        author = scholarly.search_author_id(scholar_id)
        author = scholarly.fill(author, sections=["publications"])
    except Exception as e:
        print(f"Error fetching author: {e}")
        print("Possible causes:")
        print("  - Invalid Scholar ID")
        print("  - Google Scholar is blocking requests (try again later)")
        print("  - No internet connection")
        sys.exit(1)

    publications = []
    total = len(author.get("publications", []))
    print(f"  Found {total} publications. Fetching details...\n")

    for i, pub in enumerate(author.get("publications", []), 1):
        try:
            filled = scholarly.fill(pub)
        except Exception:
            filled = pub

        bib = filled.get("bib", {})
        title = bib.get("title", "Untitled")
        authors = bib.get("author", "Unknown")
        year_str = str(bib.get("pub_year", ""))
        year = int(year_str) if year_str.isdigit() else 0
        venue = bib.get("venue", bib.get("journal", bib.get("booktitle", "")))
        citations = filled.get("num_citations", 0)
        abstract = bib.get("abstract", "")
        pub_url = filled.get("pub_url", "#")

        print(f"  [{i}/{total}] {title[:60]}... ({citations} citations)")

        publications.append({
            "title": title,
            "authors": authors,
            "year": year,
            "venue": venue,
            "citations": citations,
            "description": abstract[:200] + ("..." if len(abstract) > 200 else ""),
            "bibtex": format_bibtex(filled),
            "type": guess_type(venue),
            "pub_url": pub_url
        })

    return publications


def merge_publications(existing, fetched, highlight_author):
    """Merge fetched publications into existing list."""
    # Index existing by normalized title
    existing_map = {}
    for pub in existing:
        key = normalize_title(pub["title"])
        existing_map[key] = pub

    updated_count = 0
    added_count = 0

    for fp in fetched:
        key = normalize_title(fp["title"])

        if key in existing_map:
            # UPDATE: only update citation count (and URLs if they were placeholders)
            old_count = existing_map[key].get("citations", 0)
            new_count = fp["citations"]
            if new_count != old_count:
                existing_map[key]["citations"] = new_count
                print(f"  Updated citations: {fp['title'][:50]}... ({old_count} → {new_count})")
                updated_count += 1
                
            if existing_map[key].get("url", "#") == "#" and fp["pub_url"] != "#":
                existing_map[key]["url"] = fp["pub_url"]
            if existing_map[key].get("pdfUrl", "#") == "#" and fp["pub_url"] != "#":
                existing_map[key]["pdfUrl"] = fp["pub_url"]
        else:
            # NEW: add with placeholder images
            new_pub = {
                "title": fp["title"],
                "authors": fp["authors"],
                "highlightAuthor": highlight_author,
                "venue": fp["venue"],
                "year": fp["year"],
                "type": fp["type"],
                "image": PLACEHOLDER_IMAGE,
                "thumbnail": PLACEHOLDER_THUMB,
                "description": fp["description"],
                "pdfUrl": fp.get("pub_url", "#"),
                "url": fp.get("pub_url", "#"),
                "citations": fp["citations"],
                "bibtex": fp["bibtex"],
            }
            existing.append(new_pub)
            print(f"  Added new: {fp['title'][:60]}...")
            added_count += 1

    print(f"\n  Summary: {updated_count} updated, {added_count} new, {len(existing)} total")
    return existing


def main():
    parser = argparse.ArgumentParser(description="Update data.json from Google Scholar")
    parser.add_argument("--scholar-id", help="Google Scholar author ID (e.g., 'dkNRBCEAAAAJ')")
    args = parser.parse_args()

    # Load data
    data = load_data()

    # Get Scholar ID
    scholar_id = args.scholar_id
    if not scholar_id:
        scholar_id = data.get("settings", {}).get("scholarId", "")
    if not scholar_id:
        print("No Scholar ID provided.")
        print("Options:")
        print('  1. Add "scholarId" to settings in data.json')
        print("  2. Run: python fetch_scholar.py --scholar-id YOUR_ID")
        print("\nYour Scholar ID is in your Google Scholar profile URL:")
        print("  https://scholar.google.com/citations?user=YOUR_ID")
        sys.exit(1)

    # Save Scholar ID to settings
    if "settings" not in data:
        data["settings"] = {}
    data["settings"]["scholarId"] = scholar_id

    # Fetch
    fetched = fetch_scholar_publications(scholar_id)

    # Get highlight author name
    highlight = data["publications"][0]["highlightAuthor"] if data.get("publications") else ""
    if not highlight:
        highlight = data.get("profile", {}).get("name", "")

    # Merge
    print("\nMerging with existing publications...")
    data["publications"] = merge_publications(data["publications"], fetched, highlight)

    # Sort by year
    data["publications"].sort(key=lambda p: p.get("year", 0), reverse=True)

    # Save
    print("\nSaving...")
    save_data(data)

    print(f"\nDone! Updated at {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("\nNext steps:")
    print("  - Review data.json for any new entries")
    print("  - Replace placeholder images for new papers")
    print("  - Add PDF URLs for new papers")
    print("  - Push to GitHub: git add data.json && git commit -m 'Update publications' && git push")


if __name__ == "__main__":
    main()
