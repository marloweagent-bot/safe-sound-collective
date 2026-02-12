#!/usr/bin/env python3
import os
import re
import glob

replacements = [
    # Header logo
    (r'<span class="header-logo-icon">🔊</span>\s*\n?\s*Hearing Guide', 
     '<span class="header-logo-icon">🔊</span>\n                Safe Sound Guide'),
    # Footer logo
    (r'<div class="logo-icon">🔊</div>\s*\n?\s*Hearing Guide',
     '<div class="logo-icon">🔊</div>\n                    Safe Sound Guide'),
    # Title tags - preserve page name, change suffix
    (r'\| Hearing Guide</title>', '| Safe Sound Guide</title>'),
    # og:title tags
    (r'\| Hearing Guide">', '| Safe Sound Guide">'),
    # Hero heading (index page)
    (r'<h1>The <span class="gradient">Hearing Protection</span> Superguide</h1>',
     '<h1>The <span class="gradient">Safe Sound</span> Guide</h1>'),
    # Footer copyright
    (r'© 2026 Hearing Protection Superguide\.',
     '© 2026 Safe Sound Guide.'),
    # "Part of the" references
    (r'Part of the <a href="index.html">Hearing Protection Superguide</a>',
     'Part of the <a href="index.html">Safe Sound Guide</a>'),
    # Index title specifically
    (r'<title>Hearing Protection Superguide \|',
     '<title>Safe Sound Guide |'),
]

html_files = glob.glob('*.html')
for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
    
    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"✓ Updated: {filepath}")
    else:
        print(f"  No changes: {filepath}")

print("\nDone!")
