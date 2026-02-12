#!/usr/bin/env python3
"""
Replace Oswald with Bamboy font across all pages.
"""

import os
from pathlib import Path

PAGES = [
    "index.html",
    "index-unplugs.html",
    "decibel-guide.html",
    "how-hearing-works.html",
    "noise-induced-hearing-loss.html",
    "temporary-vs-permanent.html",
    "85-decibel-rule.html",
    "tinnitus-prevention.html",
    "safe-listening-guidelines.html",
    "headphone-safety.html",
    "concert-hearing-safety.html",
    "festival-survival.html",
    "dj-hearing-protection.html",
    "musician-hearing-guide.html",
    "kids-hearing-protection.html",
    "exposure-calculator.html",
    "hearing-test.html",
    "tinnitus-simulator.html",
]

# @font-face declaration to inject
FONT_FACE = '''
        /* Bamboy Font */
        @font-face {
            font-family: 'Bamboy';
            src: url('fonts/Bamboy-Regular.woff2') format('woff2'),
                 url('fonts/Bamboy-Regular.woff') format('woff');
            font-weight: 400;
            font-style: normal;
            font-display: swap;
        }
        @font-face {
            font-family: 'Bamboy';
            src: url('fonts/Bamboy-Condensed.woff2') format('woff2'),
                 url('fonts/Bamboy-Condensed.woff') format('woff');
            font-weight: 600;
            font-style: normal;
            font-display: swap;
        }
'''

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Remove Oswald from Google Fonts import
    content = content.replace(
        "https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap",
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
    )
    content = content.replace(
        "https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800;900&display=swap",
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap"
    )
    
    # Inject @font-face after opening <style> tag if not already present
    if "@font-face" not in content and "<style>" in content:
        content = content.replace("<style>", "<style>" + FONT_FACE, 1)
    
    # Replace Oswald references with Bamboy
    content = content.replace("'Oswald'", "'Bamboy'")
    content = content.replace('"Oswald"', "'Bamboy'")
    content = content.replace("--font-display: 'Oswald', sans-serif", "--font-display: 'Bamboy', sans-serif")
    content = content.replace("font-family: Oswald", "font-family: 'Bamboy'")
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    script_dir = Path(__file__).parent
    updated = 0
    
    for page in PAGES:
        filepath = script_dir / page
        if filepath.exists():
            if update_file(filepath):
                print(f"✅ {page}")
                updated += 1
            else:
                print(f"⏭️  {page} (no changes needed)")
        else:
            print(f"❌ {page} (not found)")
    
    print(f"\n✅ Updated: {updated} pages with Bamboy font")

if __name__ == "__main__":
    main()
