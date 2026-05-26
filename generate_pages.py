import re

with open('index_original.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace JS inline script with <script src="main.js"></script>
html = re.sub(r'<script>.*?</script>', '<script src="main.js"></script>', html, flags=re.DOTALL)

# Update nav links in the desktop nav
nav_old = '''    <ul class="nav-links">
      <li><a href="#hero">Home</a></li>
      <li><a href="#about">About</a></li>
      <li><a href="#doctor">Our Doctor</a></li>
      <li><a href="#services">Services</a></li>
      <li><a href="#treatment">Treatments</a></li>
      <li><a href="#testimonials">Reviews</a></li>
      <li><a href="#contact">Contact</a></li>
      <li><a class="btn-nav" href="tel:+918428425878">📞 Call Now</a></li>
    </ul>'''
nav_new = '''    <ul class="nav-links">
      <li><a href="index.html">Home</a></li>
      <li><a href="doctors.html">Doctors</a></li>
      <li><a href="services.html">Services</a></li>
      <li><a href="gallery.html">Gallery</a></li>
      <li><a href="reviews.html">Reviews</a></li>
      <li><a href="contact.html">Contact</a></li>
      <li><a class="btn-nav" href="appointment.html">📅 Book Now</a></li>
    </ul>'''
html = html.replace(nav_old, nav_new)

# Update nav links in mobile menu
mob_old = '''<div class="mobile-menu" id="mobileMenu">
  <a href="#hero">Home</a>
  <a href="#about">About</a>
  <a href="#doctor">Our Doctor</a>
  <a href="#services">Services</a>
  <a href="#treatment">Treatments</a>
  <a href="#testimonials">Reviews</a>
  <a href="#contact">Contact</a>
  <a class="btn btn-primary" href="tel:+918428425878">📞 Call Now</a>
</div>'''
mob_new = '''<div class="mobile-menu" id="mobileMenu">
  <a href="index.html">Home</a>
  <a href="doctors.html">Doctors</a>
  <a href="services.html">Services</a>
  <a href="gallery.html">Gallery</a>
  <a href="reviews.html">Reviews</a>
  <a href="contact.html">Contact</a>
  <a class="btn btn-primary" href="appointment.html">📅 Book Appointment</a>
</div>'''
html = html.replace(mob_old, mob_new)

# Update footer links
footer_old1 = '''<div class="footer-col">
        <h4>Quick Links</h4>
        <ul>
          <li><a href="#hero">Home</a></li>
          <li><a href="#about">About Us</a></li>
          <li><a href="#doctor">Our Doctor</a></li>
          <li><a href="#services">Services</a></li>
          <li><a href="#treatment">Treatments</a></li>
          <li><a href="#testimonials">Reviews</a></li>
          <li><a href="#contact">Book Appointment</a></li>
        </ul>
      </div>'''
footer_new1 = '''<div class="footer-col">
        <h4>Quick Links</h4>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="doctors.html">Doctors</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="reviews.html">Reviews</a></li>
          <li><a href="appointment.html">Book Appointment</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>'''
html = html.replace(footer_old1, footer_new1)

footer_old2 = '''<div class="footer-col">
        <h4>Services</h4>
        <ul>
          <li><a href="#services">Dental Implants</a></li>
          <li><a href="#services">Root Canal Treatment</a></li>
          <li><a href="#services">Teeth Cleaning</a></li>
          <li><a href="#services">Braces &amp; Orthodontics</a></li>
          <li><a href="#services">Cosmetic Dentistry</a></li>
          <li><a href="#services">Smile Designing</a></li>
        </ul>
      </div>'''
footer_new2 = '''<div class="footer-col">
        <h4>Services</h4>
        <ul>
          <li><a href="services.html">Dental Implants</a></li>
          <li><a href="services.html">Root Canal Treatment</a></li>
          <li><a href="services.html">Teeth Cleaning</a></li>
          <li><a href="services.html">Braces &amp; Orthodontics</a></li>
          <li><a href="services.html">Cosmetic Dentistry</a></li>
          <li><a href="services.html">Smile Designing</a></li>
        </ul>
      </div>'''
html = html.replace(footer_old2, footer_new2)


footer_old3 = '''<div class="footer-col">
        <h4>Contact</h4>
        <ul>
          <li><a href="#">Girls' School Road</a></li>
          <li><a href="#">North Lakhimpur, Assam 787001</a></li>
          <li><a href="tel:+918428425878">+91 84284 25878</a></li>
          <li><a href="#location">View on Google Maps</a></li>
        </ul>
        <a class="footer-call-btn" href="tel:+918428425878">📞 Call Now</a>
      </div>'''
footer_new3 = '''<div class="footer-col">
        <h4>Contact</h4>
        <ul>
          <li><a href="contact.html">Girls' School Road</a></li>
          <li><a href="contact.html">North Lakhimpur, Assam 787001</a></li>
          <li><a href="tel:+918428425878">+91 84284 25878</a></li>
          <li><a href="contact.html">View on Google Maps</a></li>
        </ul>
        <a class="footer-call-btn" href="tel:+918428425878">📞 Call Now</a>
      </div>'''
html = html.replace(footer_old3, footer_new3)

# Other href=#contact -> href=appointment.html
html = html.replace('href="#contact"', 'href="appointment.html"')

# Now extract Header and Footer
# Header: everything up to the end of <div class="mobile-menu" id="mobileMenu">...</div>
header_match = re.search(r'(.*?</div>\n)', html, flags=re.DOTALL)
header = html.split('<!-- ===== HERO ===== -->')[0]

# Footer: everything from <!-- ===== FOOTER ===== -->
footer = '<!-- ===== FOOTER ===== -->' + html.split('<!-- ===== FOOTER ===== -->')[1]

# Extract sections
# For regular sections:
def get_sec(name):
    # Using split approach for resilience instead of regex
    start = f'<!-- ===== {name} ===== -->'
    if start not in html: return ''
    part = html.split(start, 1)[1]
    # find the next section marker or footer
    next_marker = part.find('<!-- =====')
    if next_marker != -1:
        return start + part[:next_marker]
    else:
        return start + part

sec_hero = get_sec('HERO')

# Trust bar is not a section, it's a div
trust_match = re.search(r'(<!-- ===== TRUST BAR ===== -->.*?</div>\n</div>\n)', html, flags=re.DOTALL | re.IGNORECASE)
sec_trust = trust_match.group(1) if trust_match else ''

sec_gallery = get_sec('GALLERY STRIP')
lb_start = html.find('<!-- LIGHTBOX -->')
lb_end = html.find('<!-- ===== ABOUT ===== -->')
sec_lightbox = html[lb_start:lb_end] if lb_start != -1 and lb_end != -1 else ''

sec_about = get_sec('ABOUT')
sec_doctor = get_sec('DOCTOR')
sec_services = get_sec('SERVICES')
sec_why = get_sec('WHY CHOOSE')
# "HOW WE TREAT OUR PATIENTS" -> ID treatment
sec_treatment = get_sec('HOW WE TREAT OUR PATIENTS')
sec_testimonials = get_sec('TESTIMONIALS')
sec_location = get_sec('LOCATION / MAP')
sec_contact = get_sec('CONTACT')

def add_spacing(content):
    return content.replace('<section id="', '<section class="page-top-spacing" id="')

# Generate pages
with open('doctors.html', 'w', encoding='utf-8') as f:
    f.write(header + '\n' + add_spacing(sec_doctor) + '\n' + footer)

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(header + '\n' + add_spacing(sec_services) + '\n' + sec_why + '\n' + footer)

with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(header + '\n' + add_spacing(sec_gallery) + '\n' + sec_lightbox + '\n' + sec_treatment + '\n' + footer)

with open('reviews.html', 'w', encoding='utf-8') as f:
    f.write(header + '\n' + add_spacing(sec_testimonials) + '\n' + footer)

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(header + '\n' + add_spacing(sec_location) + '\n' + footer)

with open('appointment.html', 'w', encoding='utf-8') as f:
    f.write(header + '\n' + add_spacing(sec_contact) + '\n' + footer)

# Main page: hero, trust, about (only, accessible as a single page intro)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(header + '\n' + sec_hero + '\n' + sec_trust + '\n' + sec_about + '\n' + footer)

print("Pages generated successfully.")
