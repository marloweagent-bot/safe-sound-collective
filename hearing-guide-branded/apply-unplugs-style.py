#!/usr/bin/env python3
"""
Batch apply Unplugs design system to all Hearing Guide pages.
"""

import os
import re
from pathlib import Path

# Pages to update (all HTML except index-unplugs which is already styled)
PAGES = [
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

# Old color mappings to new
COLOR_REPLACEMENTS = {
    # Backgrounds
    "#0F172A": "#222222",
    "#0f172a": "#222222",
    "#1E293B": "#2A2A2A",
    "#1e293b": "#2A2A2A",
    "#334155": "#333333",
    
    # Accent colors (purple to green)
    "#6366F1": "#29EF78",
    "#6366f1": "#29EF78",
    "#4F46E5": "#22D969",
    "#4f46e5": "#22D969",
    "#7C3AED": "#29EF78",
    "#7c3aed": "#29EF78",
    
    # Cyan accent to green
    "#22D3EE": "#29EF78",
    "#22d3ee": "#29EF78",
    
    # Text colors
    "#F8FAFC": "#FFFFFF",
    "#f8fafc": "#FFFFFF",
    "#94A3B8": "#909090",
    "#94a3b8": "#909090",
    
    # Border
    "rgba(255,255,255,0.1)": "rgba(255,255,255,0.08)",
}

# CSS variable replacements
CSS_VAR_REPLACEMENTS = {
    "--primary: #6366F1": "--primary: #29EF78",
    "--primary-dark: #4F46E5": "--primary-dark: #22D969",
    "--secondary: #0F172A": "--secondary: #222222",
    "--accent: #22D3EE": "--accent: #29EF78",
    "--text: #F8FAFC": "--text: #FFFFFF",
    "--text-muted: #94A3B8": "--text-muted: #909090",
    "--card: #1E293B": "--card: #2A2A2A",
    "--card-hover: #334155": "--card-hover: #333333",
}

# Font replacement
FONT_REPLACEMENT = (
    "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap",
    "https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap"
)

# Button style updates (rounded to pill)
BUTTON_STYLE_UPDATES = [
    ("border-radius: 8px", "border-radius: 100px"),
    ("border-radius: 12px", "border-radius: 100px"),
]

def update_file(filepath):
    """Update a single HTML file with Unplugs styling."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Replace colors
    for old, new in COLOR_REPLACEMENTS.items():
        content = content.replace(old, new)
    
    # Replace CSS variables
    for old, new in CSS_VAR_REPLACEMENTS.items():
        content = content.replace(old, new)
    
    # Replace font import
    content = content.replace(FONT_REPLACEMENT[0], FONT_REPLACEMENT[1])
    
    # Update button styles for CTA buttons (be selective)
    # Only update buttons that are clearly CTAs
    content = re.sub(
        r'(\.cta-button[^}]*?)border-radius:\s*\d+px',
        r'\1border-radius: 100px',
        content
    )
    content = re.sub(
        r'(\.featured-cta[^}]*?)border-radius:\s*\d+px',
        r'\1border-radius: 100px',
        content
    )
    content = re.sub(
        r'(\.header-cta[^}]*?)border-radius:\s*\d+px',
        r'\1border-radius: 100px',
        content
    )
    
    # Add Oswald font-family to headings if not present
    if "'Oswald'" not in content and "Oswald" in content:
        # Font is imported but not used - add to h1, h2
        content = re.sub(
            r'(\.hero h1\s*\{[^}]*?)font-family:[^;]+;',
            r"\1font-family: 'Oswald', sans-serif;",
            content
        )
    
    # Update hero badge style (purple to green background)
    content = re.sub(
        r'(\.hero-badge\s*\{[^}]*?)background:\s*rgba\(99,102,241,[^)]+\)',
        r'\1background: rgba(41, 239, 120, 0.15)',
        content
    )
    content = re.sub(
        r'(\.hero-badge\s*\{[^}]*?)border:\s*1px solid rgba\(99,102,241,[^)]+\)',
        r'\1border: 1px solid rgba(41, 239, 120, 0.3)',
        content
    )
    
    # Update section badge
    content = re.sub(
        r'(\.section-badge\s*\{[^}]*?)background:\s*rgba\(34,211,238,[^)]+\)',
        r'\1background: rgba(41, 239, 120, 0.15)',
        content
    )
    
    # Update article tag
    content = re.sub(
        r'(\.article-tag\s*\{[^}]*?)background:\s*rgba\(99,102,241,[^)]+\)',
        r'\1background: rgba(41, 239, 120, 0.15)',
        content
    )
    
    # Update CTA banner gradient
    content = re.sub(
        r'(\.cta-banner\s*\{[^}]*?)background:\s*linear-gradient\(135deg,\s*var\(--primary\)[^)]+\)',
        r'\1background: var(--accent)',
        content
    )
    content = re.sub(
        r'(\.cta-banner\s*\{[^}]*?)background:\s*linear-gradient\(135deg,\s*#6366F1[^)]+\)',
        r'\1background: #29EF78',
        content,
        flags=re.IGNORECASE
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    script_dir = Path(__file__).parent
    
    updated = 0
    skipped = 0
    
    for page in PAGES:
        filepath = script_dir / page
        if filepath.exists():
            if update_file(filepath):
                print(f"✅ {page}")
                updated += 1
            else:
                print(f"⏭️  {page} (no changes)")
                skipped += 1
        else:
            print(f"❌ {page} (not found)")
    
    print(f"\n✅ Updated: {updated}")
    print(f"⏭️  Skipped: {skipped}")


if __name__ == "__main__":
    main()
