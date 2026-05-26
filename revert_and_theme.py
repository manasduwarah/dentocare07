import os

# 1. Read existing style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 2. Revert the font and text/color changes back to original
reverts = [
    (
        "@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap');",
        "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap');"
    ),
    (
        "  --primary: #9A7E5F;\n  --primary-dark: #7A6349;\n  --primary-light: #F4EFE8;\n  --accent: #4B5A65;\n  --accent-light: #DCE3E8;\n  --white: #ffffff;\n  --off-white: #FAF9F6;\n  --text-dark: #2C2E2D;\n  --text-mid: #5B5E5C;\n  --text-light: #8E928F;\n  --border: #EBE8E1;\n  --shadow: 0 6px 28px rgba(44, 46, 45, 0.05);\n  --shadow-hover: 0 16px 42px rgba(154, 126, 95, 0.16);",
        "  --primary: #1a6fc4;\n  --primary-dark: #145da0;\n  --primary-light: #e8f3fb;\n  --accent: #00b4d8;\n  --accent-light: #caf0f8;\n  --white: #ffffff;\n  --off-white: #f7fafd;\n  --text-dark: #0d1b2a;\n  --text-mid: #3a4a5c;\n  --text-light: #6b7f95;\n  --border: #daeaf7;\n  --shadow: 0 4px 24px rgba(26, 111, 196, 0.10);\n  --shadow-hover: 0 8px 40px rgba(26, 111, 196, 0.18);"
    ),
    ("font-family: 'Outfit'", "font-family: 'Inter'"),
    ("rgba(154, 126, 95, 0.35)", "rgba(26,111,196,0.3)"),
    ("rgba(44,46,45,0.06)", "rgba(26,111,196,0.10)"),
    (
        "background: linear-gradient(105deg, rgba(28,31,30,0.85) 0%, rgba(44,46,45,0.65) 55%, rgba(154,126,95,0.40) 100%)",
        "background: linear-gradient(105deg, rgba(10,40,80,0.82) 0%, rgba(10,60,130,0.60) 55%, rgba(0,150,200,0.30) 100%)"
    ),
    ("color: #DDC5A9;", "color: #7dd3fc;"),
    (
        "background: linear-gradient(135deg, #242625 0%, #4B5A65 60%, #9A7E5F 100%);",
        "background: linear-gradient(135deg, #0d2f5e 0%, #1a6fc4 60%, #0095b0 100%);"
    ),
    ("rgba(154,126,95,0.15)", "rgba(26,111,196,0.08)"),
    ("background: #1C1E1D;", "background: #0b1e3c;"),
    ("rgba(154,126,95,0.25)", "rgba(26,111,196,0.2)")
]

for old, new in reverts:
    css = css.replace(old, new)

# 3. Add Premium Background CSS Overrides
premium_css = """
/* ===== PREMIUM BACKGROUND OVERRIDES ===== */
body {
  background: linear-gradient(135deg, #f4f7fb 0%, #e2ebf4 100%);
  background-attachment: fixed;
}
body::before {
  content: "";
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: 
    radial-gradient(circle at 10% 20%, rgba(26, 111, 196, 0.04), transparent 40%),
    radial-gradient(circle at 90% 80%, rgba(0, 180, 216, 0.05), transparent 40%);
  pointer-events: none;
  z-index: -1;
}

#about, #doctor, #services, #testimonials, #location, #contact, #treatment, #gallery-strip {
  background: transparent !important;
}

.service-card, .doctor-card, .testimonial-inner, .contact-form, .about-badge-float, .contact-info-block {
  background: rgba(255, 255, 255, 0.65) !important;
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.9) !important;
  box-shadow: 0 10px 40px rgba(0,0,0,0.04) !important;
}

.service-card:hover {
  background: rgba(255, 255, 255, 0.9) !important;
  box-shadow: 0 15px 50px rgba(26,111,196,0.12) !important;
  border-color: var(--primary) !important;
  transform: translateY(-6px);
}
"""

if "PREMIUM BACKGROUND OVERRIDES" not in css:
    css += premium_css

# 4. Write back
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Reverted colors/fonts and applied premium background globally.")
