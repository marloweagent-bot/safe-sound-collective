#!/usr/bin/env python3
"""
Rebrand Hearing Guide to Safe Sound Guide for safesoundcollective.org
"""

import re
from pathlib import Path

ROOT_PAGES = [
    "index.html",
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

# UTM parameters for Unplugs links
UTM = "?utm_source=safesound&utm_medium=guide&utm_campaign=ssc"

def rebrand(content):
    """Apply all rebranding changes."""
    
    # Title/branding changes
    content = content.replace("Hearing Protection Superguide", "Safe Sound Guide")
    content = content.replace("Hearing Guide", "Safe Sound Guide")
    content = content.replace("Unplugs Learn", "Safe Sound Guide")
    content = content.replace("UNPLUGS LEARN", "SAFE SOUND GUIDE")
    
    # Update page titles
    content = re.sub(
        r'<title>([^|<]+)\| Unplugs</title>',
        r'<title>\1| Safe Sound Guide</title>',
        content
    )
    content = re.sub(
        r'<title>Hearing Protection Superguide[^<]*</title>',
        '<title>Safe Sound Guide | The Complete Hearing Protection Resource</title>',
        content
    )
    
    # Update header logo link to SSC root
    content = content.replace(
        'href="https://unplugshearing.com" class="header-logo"',
        'href="/" class="header-logo"'
    )
    content = content.replace(
        'href="index.html" class="header-logo"',
        'href="/" class="header-logo"'
    )
    
    # Update canonical URLs to safesoundcollective.org
    content = re.sub(
        r'href="https://learn\.unplugshearing\.com/([^"]*)"',
        r'href="https://safesoundcollective.org/\1"',
        content
    )
    
    # Add UTM to Unplugs product links
    content = re.sub(
        r'href="(https://unplugshearing\.com[^"]*)"',
        lambda m: f'href="{m.group(1)}{UTM}"' if UTM not in m.group(1) and '?' not in m.group(1) else f'href="{m.group(1)}&utm_source=safesound&utm_medium=guide&utm_campaign=ssc"' if '?' in m.group(1) and 'utm_source' not in m.group(1) else m.group(0),
        content
    )
    
    # Fix double UTM issue
    content = re.sub(r'\?utm_source=safesound[^"]*\?utm_source=', '?utm_source=', content)
    
    # Update footer - find and replace
    old_footer = 'Built by audiologists, for everyone.'
    new_footer = 'A Safe Sound Collective resource. Powered by <a href="https://unplugshearing.com' + UTM + '" style="color: var(--accent);">Unplugs</a>.'
    content = content.replace(old_footer, new_footer)
    
    # Also update simple footer text
    content = content.replace(
        '© 2026 Unplugs Hearing. All rights reserved.',
        '© 2026 Safe Sound Collective. Free educational resource.'
    )
    
    return content

def main():
    script_dir = Path(__file__).parent
    updated = 0
    
    for page in ROOT_PAGES:
        filepath = script_dir / page
        if not filepath.exists():
            print(f"❌ {page} (not found)")
            continue
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        content = rebrand(content)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ {page}")
            updated += 1
        else:
            print(f"⏭️  {page}")
    
    print(f"\n✅ Rebranded {updated} pages to Safe Sound Guide")

if __name__ == "__main__":
    main()
