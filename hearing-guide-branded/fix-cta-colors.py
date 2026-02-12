#!/usr/bin/env python3
"""
Fix text colors on green CTA backgrounds - use dark grey instead of white.
"""

import re
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

def fix_cta_colors(content):
    """Fix CTA section colors to use dark text on green backgrounds."""
    
    # Fix CTA banner h3 - should be dark on green
    content = re.sub(
        r'(\.cta-banner[^}]*\.cta-content h3[^}]*?)color:\s*#222;',
        r'\1color: #222222;',
        content
    )
    
    # Fix CTA section h3
    content = re.sub(
        r'(\.cta-section h3\s*\{[^}]*?)color:\s*[^;]+;',
        r'\1color: #222222;',
        content
    )
    
    # Fix CTA section p
    content = re.sub(
        r'(\.cta-section p\s*\{[^}]*?)color:\s*[^;]+;',
        r'\1color: #333333;',
        content
    )
    
    # Fix CTA content h3 (in cta-banner)
    content = re.sub(
        r'(\.cta-content h3\s*\{[^}]*?)color:\s*[^;]+;',
        r'\1color: #222222;',
        content
    )
    
    # Fix CTA content p (in cta-banner)
    content = re.sub(
        r'(\.cta-content p\s*\{[^}]*?)color:\s*[^;]+;',
        r'\1color: #333333;',
        content
    )
    
    # Fix featured-badge text (green bg, should be dark)
    content = re.sub(
        r'(\.featured-badge\s*\{[^}]*?)color:\s*white;',
        r'\1color: #222222;',
        content
    )
    content = re.sub(
        r'(\.featured-badge\s*\{[^}]*?)color:\s*#fff;',
        r'\1color: #222222;',
        content
    )
    
    # Restore body text colors that might have been wrongly changed
    content = re.sub(
        r'(--text-primary:\s*)#222222',
        r'\1#FFFFFF',
        content
    )
    content = re.sub(
        r'(--text:\s*)#222222',
        r'\1#FFFFFF',
        content
    )
    
    # Fix body color if it was changed
    content = re.sub(
        r'(body\s*\{[^}]*?)color:\s*#222222;',
        r'\1color: var(--text-primary);',
        content
    )
    
    return content

def main():
    script_dir = Path(__file__).parent
    updated = 0
    
    for page in PAGES:
        filepath = script_dir / page
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            content = fix_cta_colors(content)
            
            if content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ {page}")
                updated += 1
            else:
                print(f"⏭️  {page}")
    
    print(f"\n✅ Fixed CTA colors in {updated} pages")

if __name__ == "__main__":
    main()
