import os

reviews = [
    ("Yoongi's Pillow", "6 months ago", "I had a wonderful experience at this clinic. The doctor is not only excellent at his work but also very compassionate and kind. He is approachable and always takes the time to answer and explain any doubts with great patience. Before every..."),
    ("Pali Borah", "4 months ago", "Thank you so much for your outstanding service. I am now totally cured and I'm very happy with my recovery. Thanks a lot again sir and your staff too."),
    ("bornali hazarika", "a month ago", "Commendable service with well and friendly behaviour. One of the best dentists of the town."),
    ("Benu C", "6 months ago", "Very friendly dentist and does excellent work.He fixed my teeth one year ago perfectly after another doctor tried and failed multiple times. I would highly recommend."),
    ("Udita Das", "a year ago", "I'm totally satisfied and it was worth a visit. Dr. Kauchik & crew took utmost care during scaling and explained everything about dental care, place was hygienic & also parking available."),
    ("Abhijit Konwar", "6 months ago", "Very good clinic .Dr. Kaushik Borpatra and team provide excellent care. Quick service and very friendly atmosphere."),
    ("anigogoi Ggi", "2 years ago", "Had been suffering from excruciating pain from many days but Dr. Kaushik cured the pain and fixed my teeth in only a few minutes. My pain is totally gone and i am able to eat normally like before ...all thanks to Dr.Kaushik and his friendly staff.💯"),
    ("Biman Chutia", "7 months ago", "I've lost my front 3 teeth during an accident last year and I didn't knew about what to do. Somehow I visited dr. Kaushik borpatra and he gave me a fixed teeth setting within 1 week and also with warranty of 20 years now I can live the normal life.. thaks to the team dent o care"),
    ("baby das", "a year ago", "Amazing care! This clinic is providing exceptional services. One of the core aspects of this clinic is that they are taking care of people before profit. I highly recommend Dr kaushik for your dental needs. He's very professional, friendly and puts you at ease. Also his staff are very friendly and accommodating too.."),
    ("Parikhit Phonglo", "a year ago", "I recently visited this dental clinic, and I must say, it was a truly exceptional experience. The dentist was outstanding, professional, gentle, and extremely skilled. The treatment was remarkably painless and completed in a remarkably..."),
    ("Nabapallab Nath", "a year ago", "I had an exceptional experience at Dent o Care. From the moment I walked in, the staff was welcoming and professional. Dr. Kaushik is not only highly skilled but also takes the time to explain every step of the procedure, which put me at..."),
    ("Sapna Saikia", "a year ago", "I recently had a fantastic experience at dent o care for my braces treatment. From the moment I walked in, the staff was welcoming and professional. The orthodontist took the time to explain the entire process and answered all my questions,..."),
    ("Siddhartha Das", "3 months ago", "very good experience.. dentist is friendly and explains in details"),
    ("Abhijit Borah", "a year ago", "I couldn't be happier with the care I receive. Dr. Kaushik is incredibly knowledgeable, professional, and compassionate. The clinic is always clean and welcoming, and the staff are friendly and efficient. Whether it's a routine check-up or..."),
    ("lakhinath takoe", "8 months ago", "Good and friendly environment dental clinic. All procedures are carried out smoothly. Highly recommended."),
    ("Meghna Borgohain", "2 years ago", "One of the best clinic with the best dental doctor in town. They provide the best dental services with latest technology. Have visit there since it’s opening and every visit brings a smile in my face. Thank you Dr. Kaushik Borpatra and..."),
    ("Krishna Pratim Bordoloi", "2 years ago", "The best dentist I have ever visited. Exceptional dental care at DENT O CARE. Reasonable fees, friendly staff, and a patient-friendly dentist. I had a challenging RCT done a year ago, previously deemed impossible by other dentists. No..."),
    ("Patient", "a year ago", "I really like their kind gesture towards their patients....i personally like their treatment....u can ofc give it a try, n trust me they will surely not disappoint u.")
]

card_template = '''        <div class="testimonial-card">
          <div class="testimonial-inner">
            <div class="test-stars">
              <svg viewBox="0 0 24 24" fill="currentColor"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
              <svg viewBox="0 0 24 24" fill="currentColor"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
              <svg viewBox="0 0 24 24" fill="currentColor"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
              <svg viewBox="0 0 24 24" fill="currentColor"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
              <svg viewBox="0 0 24 24" fill="currentColor"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            </div>
            <p class="test-quote">"{text}"</p>
            <div class="test-author">
              <div class="test-avatar">{initial}</div>
              <div><div class="test-name">{name}</div><div class="test-label">Verified Google Review · {time}</div></div>
            </div>
          </div>
        </div>
'''

new_cards = ""
for name, time, text in reviews:
    initial = list(filter(str.isalpha, name))
    initial = initial[0].upper() if initial else "G"
    new_cards += card_template.format(text=text, initial=initial, name=name, time=time)

with open('index_original.html', 'r', encoding='utf-8') as f:
    html = f.read()

# insert cards right before </div>\n      <div class="test-controls">
track_end = '</div>\n      <div class="test-controls">'
if track_end in html:
    html = html.replace(track_end, new_cards + track_end)

# update dots. Total is 4 + 18 = 22
old_dots = '''        <div class="test-dots">
          <div class="test-dot active" data-i="0"></div>
          <div class="test-dot" data-i="1"></div>
          <div class="test-dot" data-i="2"></div>
          <div class="test-dot" data-i="3"></div>
        </div>'''
new_dots = '        <div class="test-dots">\n          <div class="test-dot active" data-i="0"></div>\n'
for i in range(1, 22):
    new_dots += f'          <div class="test-dot" data-i="{i}"></div>\n'
new_dots += '        </div>'

html = html.replace(old_dots, new_dots)

with open('index_original.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Added reviews to index_original.html!")
