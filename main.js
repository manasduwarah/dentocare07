// ===== NAVBAR SCROLL =====
const navbar = document.getElementById('navbar');
const hasHero = document.getElementById('hero') !== null;
if (navbar) {
  if (!hasHero) navbar.classList.add('scrolled');
  window.addEventListener('scroll', () => {
    if (hasHero) {
      navbar.classList.toggle('scrolled', window.scrollY > 60);
    }
  });
}

// ===== HAMBURGER MENU =====
const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobileMenu');
hamburger.addEventListener('click', () => {
  mobileMenu.classList.toggle('open');
});
mobileMenu.querySelectorAll('a').forEach(a => {
  a.addEventListener('click', () => mobileMenu.classList.remove('open'));
});

// ===== HERO SLIDESHOW =====
const heroSlides = document.querySelectorAll('.hero-slide');
const heroDots = document.querySelectorAll('.hero-dot');
if (heroSlides.length > 0) {
  let heroIdx = 0;
  function heroGoTo(i) {
    heroSlides[heroIdx].classList.remove('active');
    heroDots[heroIdx].classList.remove('active');
    heroIdx = (i + heroSlides.length) % heroSlides.length;
    heroSlides[heroIdx].classList.add('active');
    heroDots[heroIdx].classList.add('active');
  }
  heroDots.forEach(d => d.addEventListener('click', () => heroGoTo(+d.dataset.s)));
  setInterval(() => heroGoTo(heroIdx + 1), 4500);
}

// ===== LIGHTBOX =====
const galleryImages = [
  { src: 'gallery3.jpg', alt: 'Clinic Exterior' },
  { src: 'gallery2.jpg', alt: 'Treatment Room' },
  { src: 'gallery4.jpg', alt: 'Reception' },
  { src: 'gallery5.jpg', alt: 'Waiting Area' },
  { src: 'gallery1.jpg', alt: 'Certifications & Awards' }
];
let lbIdx = 0;
const lightbox = document.getElementById('lightbox');
const lbImg = document.getElementById('lightboxImg');
const lbCounter = document.getElementById('lightboxCounter');
if (lightbox) {
  window.openLightbox = function(i) {
    lbIdx = i;
    lbImg.src = galleryImages[i].src;
    lbImg.alt = galleryImages[i].alt;
    lbCounter.textContent = (i + 1) + ' / ' + galleryImages.length;
    lightbox.classList.add('open');
    document.body.style.overflow = 'hidden';
  };
  window.closeLightbox = function() {
    lightbox.classList.remove('open');
    document.body.style.overflow = '';
  };
  window.closeLightboxOnBg = function(e) { if (e.target === lightbox) closeLightbox(); };
  window.lightboxNav = function(dir) {
    lbIdx = (lbIdx + dir + galleryImages.length) % galleryImages.length;
    lbImg.src = galleryImages[lbIdx].src;
    lbImg.alt = galleryImages[lbIdx].alt;
    lbCounter.textContent = (lbIdx + 1) + ' / ' + galleryImages.length;
  };
  document.addEventListener('keydown', e => {
    if (!lightbox.classList.contains('open')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowRight') window.lightboxNav(1);
    if (e.key === 'ArrowLeft') window.lightboxNav(-1);
  });
}

// ===== TESTIMONIALS SLIDER =====
const track = document.getElementById('testimonialsTrack');
const testDots = document.querySelectorAll('.test-dot');
if (track && testDots.length > 0) {
  let current = 0;
  const total = testDots.length;
  function goTo(i) {
    current = (i + total) % total;
    track.style.transform = `translateX(-${current * 100}%)`;
    testDots.forEach((d, idx) => d.classList.toggle('active', idx === current));
  }
  const nextBtn = document.getElementById('testNext');
  const prevBtn = document.getElementById('testPrev');
  if(nextBtn) nextBtn.addEventListener('click', () => goTo(current + 1));
  if(prevBtn) prevBtn.addEventListener('click', () => goTo(current - 1));
  testDots.forEach(d => d.addEventListener('click', () => goTo(+d.dataset.i)));
  setInterval(() => goTo(current + 1), 6000);
}

// ===== SCROLL ANIMATIONS =====
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); observer.unobserve(e.target); } });
}, { threshold: 0.12 });
document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));

// ===== TREATMENT GALLERY =====
const treatData = [
  { src: 'treat1.jpg', title: 'Smile Transformation', desc: 'Before and after – complete smile restoration using implants and cosmetic dentistry by Dr. Kaushik Borpatra.' },
  { src: 'treat2.jpg', title: 'Surgical Implant Procedure', desc: 'Dr. Borpatra and team performing a dental implant surgery with full sterile protocol and precision equipment.' },
  { src: 'treat3.jpg', title: 'In-Chair Dental Treatment', desc: 'A dental procedure in progress, showcasing our modern chair setup and intraoral video monitoring system.' },
  { src: 'treat4.jpg', title: 'UV Light Bonding Treatment', desc: 'Cosmetic bonding using UV curing light – a painless procedure for restoring and beautifying teeth.' },
  { src: 'treat5.jpg', title: 'Local Anaesthesia Administration', desc: 'Precise anaesthesia delivery to ensure the patient feels absolutely nothing during the procedure.' },
  { src: 'treat6.jpg', title: 'Surgical Tooth Extraction', desc: 'Step-by-step intraoral camera documentation of a complex surgical extraction performed at our clinic.' },
  { src: 'treat7.jpg', title: 'Intraoral Camera Diagnosis', desc: 'Real-time HD intraoral imaging used to provide patients with a clear, transparent view of their dental condition.' },
  { src: 'treat8.jpg', title: 'Braces & Orthodontic Treatment', desc: 'Coloured bracket braces fitted precisely to correct misalignment and achieve a perfectly straight smile.' },
  { src: 'treat9.jpg', title: 'Cavity Restoration – Before & After', desc: 'Intraoral camera footage showing a deep cavity and the completed composite filling – a seamless, natural result.' },
  { src: 'treat10.jpg', title: 'Full Mouth Intraoral Scan', desc: 'Waldent intraoral camera capturing a complete multi-angle view of the patient’s oral health for precise diagnosis.' }
];
const treatImg = document.getElementById('treatMainImg');
if (treatImg) {
  let treatIdx = 0;
  const treatTitle = document.getElementById('treatTitle');
  const treatDesc = document.getElementById('treatDesc');
  const treatThumbs = document.querySelectorAll('.treat-thumb');
  const treatDotsArray = document.querySelectorAll('.treat-dot');
  window.treatGoTo = function(i) {
    treatIdx = (i + treatData.length) % treatData.length;
    treatImg.classList.add('fading');
    setTimeout(() => {
      treatImg.src = treatData[treatIdx].src;
      treatImg.alt = treatData[treatIdx].title;
      treatTitle.textContent = treatData[treatIdx].title;
      treatDesc.textContent = treatData[treatIdx].desc;
      treatImg.classList.remove('fading');
    }, 220);
    treatThumbs.forEach((t, idx) => t.classList.toggle('active', idx === treatIdx));
    treatDotsArray.forEach((d, idx) => d.classList.toggle('active', idx === treatIdx));
  };
  const treatNext = document.getElementById('treatNext');
  const treatPrev = document.getElementById('treatPrev');
  if(treatNext) treatNext.addEventListener('click', () => window.treatGoTo(treatIdx + 1));
  if(treatPrev) treatPrev.addEventListener('click', () => window.treatGoTo(treatIdx - 1));
  setInterval(() => window.treatGoTo(treatIdx + 1), 5000);
}

// ===== CONTACT FORM (GOOGLE SHEETS WEBHOOK) =====
const form = document.getElementById('contactForm');
if (form) {
  const msg = document.getElementById('formMsg');
  const submitBtn = document.getElementById('submitBtn');

  form.addEventListener('submit', function(e) {
    e.preventDefault();
    submitBtn.textContent = 'Submitting...';
    submitBtn.style.opacity = '0.7';

    // To use standard form data for Apps Script:
    const formData = new FormData(form);

    // Provide the Google Sheets App Script Webhook URL here once it's created.
    // E.g., const scriptURL = "https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec";
    const scriptURL = "https://script.google.com/macros/s/AKfycbwYOUR_SCRIPT_URL_HERE/exec"; // Placeholder

    fetch(scriptURL, { 
      method: 'POST', 
      body: formData
    })
    .then(response => {
      if (response.ok) {
        msg.textContent = 'Thank you! Your appointment request has been sent.';
        msg.style.color = '#10b981';
        msg.style.display = 'block';
        form.reset();
      } else {
        throw new Error('Network response was not ok.');
      }
    })
    .catch(error => {
      console.error('Error!', error.message);
      msg.textContent = 'Oops! Something went wrong. Please try calling us instead.';
      msg.style.color = '#ef4444';
      msg.style.display = 'block';
    })
    .finally(() => {
      submitBtn.textContent = '📅 Book My Appointment';
      submitBtn.style.opacity = '1';
      setTimeout(() => msg.style.display = 'none', 6000);
    });
  });
}
