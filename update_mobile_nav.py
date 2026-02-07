#!/usr/bin/env python3
import os
import glob
import re

# New mobile navigation HTML
new_mobile_nav = '''<!-- Mobile Menu Button -->
        <div class="d-flex align-items-center gap-4 d-lg-none">
          <button class="btn p-2 d-flex align-items-center justify-content-center bg-white rounded-circle" 
                  type="button" 
                  data-bs-toggle="offcanvas" 
                  data-bs-target="#mobileNav" 
                  aria-controls="mobileNav">
            <iconify-icon icon="solar:hamburger-menu-line-duotone" class="fs-8 text-dark"></iconify-icon>
          </button>
        </div>
      </div>
    </div>
  </header>

  <!-- Off-canvas Mobile Navigation -->
  <div class="offcanvas offcanvas-end" tabindex="-1" id="mobileNav" aria-labelledby="mobileNavLabel">
    <div class="offcanvas-header border-bottom">
      <h5 class="offcanvas-title fw-bold" id="mobileNavLabel">Menu</h5>
      <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
    </div>
    <div class="offcanvas-body p-0">
      <ul class="list-unstyled mb-0">
        <li class="border-bottom">
          <a href="index.html" class="d-flex align-items-center gap-2 p-3 text-dark text-decoration-none">
            <img src="../assets/images/svgs/secondary-leaf.svg" alt="" width="20" height="20" class="animate-spin">
            <span class="fw-semibold">Home</span>
          </a>
        </li>
        <li class="border-bottom">
          <a href="about-us.html" class="d-flex align-items-center gap-2 p-3 text-dark text-decoration-none">
            <img src="../assets/images/svgs/secondary-leaf.svg" alt="" width="20" height="20" class="animate-spin">
            <span class="fw-semibold">About</span>
          </a>
        </li>
        <li class="border-bottom">
          <a href="insight.html" class="d-flex align-items-center gap-2 p-3 text-dark text-decoration-none">
            <img src="../assets/images/svgs/secondary-leaf.svg" alt="" width="20" height="20" class="animate-spin">
            <span class="fw-semibold">Insights</span>
          </a>
        </li>
        
        <!-- Industries Accordion -->
        <li class="border-bottom">
          <a class="d-flex align-items-center justify-content-between p-3 text-dark text-decoration-none" 
             data-bs-toggle="collapse" 
             href="#industriesMenu" 
             role="button" 
             aria-expanded="false">
            <div class="d-flex align-items-center gap-2">
              <img src="../assets/images/svgs/secondary-leaf.svg" alt="" width="20" height="20" class="animate-spin">
              <span class="fw-semibold">Industries</span>
            </div>
            <iconify-icon icon="lucide:chevron-down" class="fs-6"></iconify-icon>
          </a>
          <div class="collapse" id="industriesMenu">
            <ul class="list-unstyled bg-light">
              <li><a class="d-block px-4 py-2 text-dark text-decoration-none" href="agriculture.html">Agriculture</a></li>
              <li><a class="d-block px-4 py-2 text-dark text-decoration-none" href="consumer-packaged-goods.html">Consumer Packaged Goods</a></li>
              <li><a class="d-block px-4 py-2 text-dark text-decoration-none" href="education.html">Education</a></li>
              <li><a class="d-block px-4 py-2 text-dark text-decoration-none" href="engineering-construction.html">Engineering, Construction & Building Materials</a></li>
              <li><a class="d-block px-4 py-2 text-dark text-decoration-none" href="financial-services.html">Financial Services</a></li>
              <li><a class="d-block px-4 py-2 text-dark text-decoration-none" href="healthcare.html">Healthcare</a></li>
              <li><a class="d-block px-4 py-2 text-dark text-decoration-none" href="Infrastructure.html">Infrastructure</a></li>
              <li><a class="d-block px-4 py-2 text-dark text-decoration-none" href="logistics.html">Logistics</a></li>
              <li><a class="d-block px-4 py-2 text-dark text-decoration-none" href="p&p.html">P&P</a></li>
            </ul>
          </div>
        </li>
        
        <!-- Services Accordion -->
        <li class="border-bottom">
          <a class="d-flex align-items-center justify-content-between p-3 text-dark text-decoration-none" 
             data-bs-toggle="collapse" 
             href="#servicesMenu" 
             role="button" 
             aria-expanded="false">
            <div class="d-flex align-items-center gap-2">
              <img src="../assets/images/svgs/secondary-leaf.svg" alt="" width="20" height="20" class="animate-spin">
              <span class="fw-semibold">Services</span>
            </div>
            <iconify-icon icon="lucide:chevron-down" class="fs-6"></iconify-icon>
          </a>
          <div class="collapse" id="servicesMenu">
            <ul class="list-unstyled bg-light">
              <li><a class="d-block px-4 py-2 text-dark text-decoration-none" href="audit.html">Audits</a></li>
              <li><a class="d-block px-4 py-2 text-dark text-decoration-none" href="strategy-corporate-finance.html">Strategy & Corporate Finance</a></li>
              <li><a class="d-block px-4 py-2 text-dark text-decoration-none" href="risk-resilience.html">Risk & Resilience</a></li>
              <li><a class="d-block px-4 py-2 text-dark text-decoration-none" href="business-transformation.html">Business Transformation</a></li>
              <li><a class="d-block px-4 py-2 text-dark text-decoration-none" href="ai-implementation.html">AI Implementation</a></li>
              <li><a class="d-block px-4 py-2 text-dark text-decoration-none" href="people-organizational-performance.html">People & Organizational Performance</a></li>
              <li><a class="d-block px-4 py-2 text-dark text-decoration-none" href="technology.html">Technology</a></li>
              <li><a class="d-block px-4 py-2 text-dark text-decoration-none" href="sustainability.html">Sustainability</a></li>
              <li><a class="d-block px-4 py-2 text-dark text-decoration-none" href="implementation.html">Implementation</a></li>
              <li><a class="d-block px-4 py-2 text-dark text-decoration-none" href="operations.html">Operations</a></li>
            </ul>
          </div>
        </li>
        
        <li class="border-bottom">
          <a href="careers.html" class="d-flex align-items-center gap-2 p-3 text-dark text-decoration-none">
            <img src="../assets/images/svgs/secondary-leaf.svg" alt="" width="20" height="20" class="animate-spin">
            <span class="fw-semibold">Careers</span>
          </a>
        </li>
        <li class="border-bottom">
          <a href="contact.html" class="d-flex align-items-center gap-2 p-3 text-dark text-decoration-none">
            <img src="../assets/images/svgs/secondary-leaf.svg" alt="" width="20" height="20" class="animate-spin">
            <span class="fw-semibold">Contact</span>
          </a>
        </li>
      </ul>
    </div>
  </div>'''

def replace_mobile_nav(file_path):
    """Replace old mobile navigation with new off-canvas navigation"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the mobile menu section
    start_marker = '<div class="d-flex align-items-center gap-4 d-lg-none">'
    start_idx = content.find(start_marker)
    
    if start_idx == -1:
        print(f"  ⚠️  Mobile nav not found in {file_path}")
        return False
    
    # Find the end by counting nested divs
    temp = content[start_idx:]
    div_count = 0
    i = 0
    while i < len(temp):
        if temp[i:i+5] == '<div ':
            div_count += 1
        elif temp[i:i+6] == '</div>':
            div_count -= 1
            if div_count == 0:
                end_idx = start_idx + i + 6
                break
        i += 1
    
    # Replace the section
    new_content = content[:start_idx] + new_mobile_nav + content[end_idx:]
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

# Process all HTML files
html_files = glob.glob('html/*.html')
print(f"Found {len(html_files)} HTML files\n")

success_count = 0
for html_file in html_files:
    print(f"Processing: {html_file}")
    if replace_mobile_nav(html_file):
        success_count += 1
        print(f"  ✓ Updated successfully")
    print()

print(f"\n{'='*50}")
print(f"Updated {success_count} out of {len(html_files)} files")
print(f"{'='*50}")
