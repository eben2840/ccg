#!/usr/bin/env python3
import os
import re

html_files = [
    ('index.html', 'index.html'),
    ('about-us.html', 'about-us.html'),
    ('insight.html', 'insight.html'),
    ('careers.html', 'careers.html'),
    ('contact.html', 'contact.html'),
]

for filename, page_name in html_files:
    filepath = f'html/{filename}'
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Add active class to matching page in mobile menu
    pattern = f'<a href="{page_name}" class="d-flex align-items-center gap-2 p-3 text-dark text-decoration-none">'
    replacement = f'<a href="{page_name}" class="d-flex align-items-center gap-2 p-3 text-dark text-decoration-none active">'
    
    content = content.replace(pattern, replacement)
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"✓ Updated {filename}")

print("\nDone!")
