#!/bin/bash

# New footer content
new_footer='<footer class="footer bg-dark py-5 py-lg-11 py-xl-12">
    <div class="container">
      <div class="row">
        <div class="col-xl-5 mb-8 mb-xl-0">
          <div class="d-flex flex-column gap-8 pe-xl-5">
            <h2 class="mb-0 text-white">How to connect to CCG?</h2>
            <div class="d-flex flex-column gap-2">
              <a href="" target="_blank" class="link-hover hstack gap-3 text-white fs-5">
                <iconify-icon icon="lucide:arrow-up-right" class="fs-7 text-primary"></iconify-icon>
                info@ccitadelgroup.com
              </a>
              <a href="https://maps.app.goo.gl/vLQvYJbg2VozJMNP8" target="_blank"
                class="link-hover hstack gap-3 text-white fs-5">
                <iconify-icon icon="lucide:arrow-up-right" class="fs-7 text-primary"></iconify-icon>
                30 N Gould St, suite R Sheridan, WY 82801
              </a>
            </div>
          </div>
        </div>
        <div class="col-md-4 col-xl-2 mb-8 mb-xl-0">
          <ul class="footer-menu list-unstyled mb-0 d-flex flex-column gap-2">
            <li><a class="link-hover fs-5 text-white" href="index.html">Home</a></li>
            <li><a class="link-hover fs-5 text-white" href="about-us.html">About</a></li>
            <li><a class="link-hover fs-5 text-white" id="services" href="projects.html ">Services</a></li>
            <li><a class="link-hover fs-5 text-white" id="" href="insight.html">Insights</a></li>
            <li><a class="link-hover fs-5 text-white" id="" href="projects.html">How we Work</a></li>
          </ul>
        </div>
        <div class="col-md-4 col-xl-2 mb-8 mb-xl-0">
          <ul class="footer-menu list-unstyled mb-0 d-flex flex-column gap-2">
            <li><a class="link-hover fs-5 text-white" id="" href="careers.html">Careers</a></li>
            <li><a class="link-hover fs-5 text-white" id="" href="audit.html">Audits</a></li>
            <!-- <li><a class="link-hover fs-5 text-white" href="terms-and-conditions.html">Terms</a></li> -->
            <!-- <li><a class="link-hover fs-5 text-white" href="privacy-policy.html">Privacy Policy</a></li> -->
            <li><a class="link-hover fs-5 text-white" href="#!">Facebook</a></li>
            <li><a class="link-hover fs-5 text-white" href="#!">Instagram</a></li>
            <li><a class="link-hover fs-5 text-white" href="#!">Twitter</a></li>
          </ul>
        </div>
        <div class="col-md-4 col-xl-3 mb-8 mb-xl-0">
          <p class="mb-0 text-white text-opacity-70 text-md-end"><a href="index.html" class="logo-dark">
            <img src="../assets/images/logos/Coastline-Citadel-Group-white.png" alt="logo" style="width: 150px;"  class="img-fluid">
          </a></p>
        </div>
      </div>
    </div>
  <p class="mb-0 text-white text-opacity-70 text-md-center mt-10">© 2026 Coastline Citadel Group</a></p>
  </footer>'

# Loop through all HTML files in html/ directory
for file in html/*.html; do
  # Use sed to replace the footer
  # First, find the line with <footer> and replace until </footer>
  # But since it's multiline, use awk or sed with -z
  # Use perl for multiline replacement
  perl -i -pe 'BEGIN{undef $/;} s/<footer[^>]*>.*?<\/footer>/$ENV{NEW_FOOTER}/s' "$file"
done
