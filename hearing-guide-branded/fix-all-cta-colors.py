#!/usr/bin/env python3
"""
Fix all CTA/green-background text colors to use dark grey.
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

def fix_colors(content):
    """Fix text colors on green backgrounds."""
    
    # Add explicit color rules for protection-cta elements
    # Find .protection-cta h2 and add color if not present
    if '.protection-cta h2 {' in content:
        content = re.sub(
            r'(\.protection-cta h2\s*\{[^}]*?)(\})',
            lambda m: m.group(1) + (' color: #222222;' if 'color:' not in m.group(1) else '') + m.group(2),
            content
        )
        # Update existing color
        content = re.sub(
            r'(\.protection-cta h2\s*\{[^}]*?)color:\s*[^;]+;',
            r'\1color: #222222;',
            content
        )
    
    # Fix protection-cta p
    if '.protection-cta p {' in content:
        content = re.sub(
            r'(\.protection-cta p\s*\{[^}]*?)opacity:\s*[^;]+;',
            r'\1color: #333333;',
            content
        )
        # Add color if missing
        content = re.sub(
            r'(\.protection-cta p\s*\{)([^}]*?)(\})',
            lambda m: m.group(1) + m.group(2) + (' color: #333333;' if 'color:' not in m.group(2) else '') + m.group(3),
            content
        )
    
    # Fix CTA section h3 (used in some pages)
    content = re.sub(
        r'(\.cta-section h3\s*\{[^}]*?)color:\s*[^;]+;',
        r'\1color: #222222;',
        content
    )
    
    # Fix CTA content h3
    content = re.sub(
        r'(\.cta-content h3\s*\{[^}]*?)color:\s*[^;]+;',
        r'\1color: #222222;',
        content
    )
    
    # Fix CTA content p
    content = re.sub(
        r'(\.cta-content p\s*\{[^}]*?)color:\s*[^;]+;',
        r'\1color: #333333;',
        content
    )
    content = re.sub(
        r'(\.cta-content p\s*\{[^}]*?)opacity:\s*[^;]+;',
        r'\1color: #333333;',
        content
    )
    
    # Fix .cta-btn on green (should have dark text) - but this one uses white bg so skip
    # Fix any .btn-primary text color
    content = re.sub(
        r'(\.btn-primary\s*\{[^}]*?)color:\s*white;',
        r'\1color: #222222;',
        content
    )
    
    # Fix featured-badge
    content = re.sub(
        r'(\.featured-badge\s*\{[^}]*?)color:\s*white;',
        r'\1color: #222222;',
        content
    )
    
    # Fix hero-stat-value if green bg
    # Actually hero-stat-value is green TEXT on dark bg, that's fine
    
    return content

def main():
    script_dir = Path(__file__).parent
    updated = 0
    
    for page in PAGES:
        filepath = script_dir / page
        if not filepath.exists():
            print(f"❌ {page} (not found)")
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        content = fix_colors(content)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ {page}")
            updated += 1
        else:
            print(f"⏭️  {page}")
    
    print(f"\n✅ Fixed {updated} pages")

if __name__ == "__main__":
    main()
