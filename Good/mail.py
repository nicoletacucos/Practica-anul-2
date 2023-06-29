import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
from bs4 import BeautifulSoup
import re
url = "https://www.mcmusic.ro/piane-digitale-pian"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

div_elements = soup.find_all('div', class_='productName prod_grid_div_like_h2')
price_elements = soup.find_all('span', class_='price')



# Adresa ta de e-mail și parola
sender_email = "practica2023cucos@gmail.com"
sender_password = "cucosnicoletapractica2023"

# Adresa de e-mail a destinatarului
recipient_email="cucosnicoleta3@gmail.com"

# Subiectul și conținutul emailului
subject = "Rezultate căutare piane digitale"
body = ""

for div_element, price in zip(div_elements, price_elements):
    title_text = div_element.text.strip()
    price_el = price.text.strip()
    link_element = div_element.find('a')
    href = link_element['href']
    if "Korg" in title_text:
        # Adăugarea detaliilor în conținutul emailului
        body += f"{title_text}\nPrice: {price_el}\nLink: {href}\n\n"

# Crearea mesajului email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Conectarea la serverul SMTP și trimiterea emailului
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(message)

print("E-mail trimis cu succes!")

