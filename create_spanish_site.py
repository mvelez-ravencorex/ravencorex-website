#!/usr/bin/env python3
"""
Script to create Spanish version of RavencoreX website
Copies all HTML pages to /ar with Spanish translations
Maintains asset references to original location
"""

import os
import re
import json
import shutil
from pathlib import Path

# Configuration
BASE_DIR = Path(__file__).parent
AR_DIR = BASE_DIR / "ar"
PAGES = [
    "index.html",
    "about-us.html",
    "cloud-solutions-devops.html",
    "data-analytics-business-intelligence.html",
    "ecommerce-development-optimization.html",
    "web-design.html",
    "contact-page.html"
]

# Load translations
with open(BASE_DIR / "translations.json", "r", encoding="utf-8") as f:
    TRANSLATIONS = json.load(f)

# URL mappings
URL_MAP = {
    "index.html": "index.html",
    "about-us.html": "about-us.html",
    "cloud-solutions-devops.html": "cloud-solutions-devops.html",
    "data-analytics-business-intelligence.html": "data-analytics-business-intelligence.html",
    "ecommerce-development-optimization.html": "ecommerce-development-optimization.html",
    "web-design.html": "web-design.html",
    "contact-page.html": "contact-page.html"
}

def create_ar_directory():
    """Create /ar directory if it doesn't exist"""
    AR_DIR.mkdir(exist_ok=True)
    print(f"✅ Created directory: {AR_DIR}")

def update_asset_paths(content):
    """
    Keep all asset paths exactly as they are in English version
    DO NOT change any paths - they should remain identical
    """
    # No changes to asset paths - return content as-is
    return content

def update_internal_links(content):
    """
    Keep all internal links pointing to the same page names
    Links will work within /ar/ directory (e.g., /ar/about-us.html)
    """
    # Internal navigation links stay the same (relative within /ar/)
    # No changes needed - pages in /ar/ link to other pages in /ar/ by default
    return content

def translate_meta_tags(content, page_name):
    """Translate meta tags and add hreflang"""
    page_trans = TRANSLATIONS["pages"][page_name]

    # Update lang attribute
    content = re.sub(r'<html([^>]*?)>', r'<html\1 lang="es">', content)

    # Update title
    content = re.sub(
        r'<title>.*?</title>',
        f'<title>{page_trans["title"]}</title>',
        content,
        flags=re.DOTALL
    )

    # Update meta description
    content = re.sub(
        r'<meta content=".*?" name="description">',
        f'<meta content="{page_trans["description"]}" name="description">',
        content
    )

    # Update OG tags
    content = re.sub(
        r'property="og:url" content="https://ravencorex.com/([^"]*)"',
        rf'property="og:url" content="https://ravencorex.com/ar/\1"',
        content
    )

    # Add og:locale
    if 'og:locale' not in content:
        content = re.sub(
            r'(<meta property="og:type"[^>]*>)',
            r'\1\n  <meta property="og:locale" content="es_AR">',
            content
        )

    # Update canonical
    content = re.sub(
        r'<link rel="canonical" href="https://ravencorex.com/([^"]*)"',
        rf'<link rel="canonical" href="https://ravencorex.com/ar/\1"',
        content
    )

    # Add hreflang tags
    en_url = f"https://ravencorex.com/{page_name}"
    ar_url = f"https://ravencorex.com/ar/{page_name}"

    hreflang_tags = f'''  <link rel="alternate" hreflang="en" href="{en_url}">
  <link rel="alternate" hreflang="es" href="{ar_url}">
  <link rel="alternate" hreflang="x-default" href="{en_url}">'''

    # Insert hreflang after canonical
    content = re.sub(
        r'(<link rel="canonical"[^>]*>)',
        rf'\1\n{hreflang_tags}',
        content
    )

    return content

def translate_navigation(content):
    """Translate navigation menu"""
    nav_trans = TRANSLATIONS["nav"]

    for en, es in nav_trans.items():
        # Update nav links text - capture the class attribute and replace text
        content = re.sub(
            rf'(class="navbar1_link[^"]*")>{en}</a>',
            rf'\1>{es}</a>',
            content
        )
        # Also update footer links
        content = re.sub(
            rf'(class="footer1_link[^"]*")>{en}</a>',
            rf'\1>{es}</a>',
            content
        )
        # Update buttons (handle HTML entity for apostrophe)
        en_html = en.replace("'", "&#x27;")
        content = re.sub(
            rf'(class="button[^"]*")>{en_html}</a>',
            rf'\1>{es}</a>',
            content
        )
        content = re.sub(
            rf'(class="button[^"]*")>{en}</a>',
            rf'\1>{es}</a>',
            content
        )

    return content

def add_language_selector(content, page_name):
    """Replace Argentina flag with USA flag in Spanish pages"""
    # Language selector for Spanish pages (links to English)
    en_url = f"../{page_name}"

    # USA flag selector
    usa_selector = f'''<div class="language-selector" style="display: inline-flex; align-items: center; margin-left: 0.5rem;">
            <a href="{en_url}" class="language-link" aria-label="Switch to English" title="Switch to English" style="display: inline-flex; align-items: center; padding: 0.25rem; text-decoration: none; transition: opacity 0.3s ease;">
              <svg width="24" height="24" viewBox="0 0 640 480" xmlns="http://www.w3.org/2000/svg" style="border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.2);">
                <path fill="#bd3d44" d="M0 0h640v480H0"/>
                <path stroke="#fff" stroke-width="37" d="M0 55.3h640M0 129h640M0 203h640M0 277h640M0 351h640M0 425h640"/>
                <path fill="#192f5d" d="M0 0h364.8v258.5H0"/>
                <g fill="#fff">
                  <g id="us-star">
                    <path d="m182.4 47 2.1 6.5h6.8l-5.5 4 2.1 6.5-5.5-4-5.5 4 2.1-6.5-5.5-4h6.8z"/>
                  </g>
                  <use href="#us-star" x="30.9"/>
                  <use href="#us-star" x="61.8"/>
                  <use href="#us-star" x="92.7"/>
                  <use href="#us-star" x="123.6"/>
                  <use href="#us-star" x="154.5"/>
                </g>
              </svg>
            </a>
          </div>'''

    # Replace the Argentina flag selector with USA flag selector
    # Pattern matches the entire Argentina flag language-selector div
    content = re.sub(
        r'<div class="language-selector"[^>]*?>.*?<a href="ar/[^"]*?".*?</svg>\s*</a>\s*</div>',
        usa_selector,
        content,
        flags=re.DOTALL
    )

    return content

def process_page(page_name):
    """Process a single page: copy, translate, update paths"""
    print(f"\n📄 Processing {page_name}...")

    # Read original page
    source_file = BASE_DIR / page_name
    with open(source_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update asset paths to point to parent directory
    content = update_asset_paths(content)

    # 2. Translate meta tags and add hreflang
    content = translate_meta_tags(content, page_name)

    # 3. Update internal links
    content = update_internal_links(content)

    # 4. Add language selector
    content = add_language_selector(content, page_name)

    # 5. Translate navigation
    content = translate_navigation(content)

    # Write to /ar directory
    dest_file = AR_DIR / page_name
    with open(dest_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  ✅ Created: ar/{page_name}")
    print(f"     - Asset paths updated to ../")
    print(f"     - Meta tags translated")
    print(f"     - hreflang tags added")
    print(f"     - Language selector added")

def main():
    """Main execution function"""
    print("🚀 Starting Spanish site creation...\n")
    print("=" * 60)

    # Create /ar directory
    create_ar_directory()

    # Process each page
    for page in PAGES:
        try:
            process_page(page)
        except Exception as e:
            print(f"  ❌ Error processing {page}: {e}")

    print("\n" + "=" * 60)
    print("\n✅ Spanish site creation complete!")
    print(f"\n📁 Location: {AR_DIR}")
    print(f"📊 Pages created: {len(PAGES)}")
    print("\n⚠️  Next steps:")
    print("   1. Add hreflang tags to English pages")
    print("   2. Add language selector to English pages")
    print("   3. Update sitemap.xml")
    print("   4. Translate page content (H1, paragraphs, buttons, etc.)")

if __name__ == "__main__":
    main()
