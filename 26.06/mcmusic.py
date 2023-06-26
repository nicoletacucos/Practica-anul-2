import requests
from bs4 import BeautifulSoup
import re
url = "https://www.mcmusic.ro/piane-digitale-pian"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

div_elements = soup.find_all('div', class_='productName prod_grid_div_like_h2')
price_elements = soup.find_all('span', class_='price')

for div_element, price in zip(div_elements, price_elements):
    title_text=div_element.text.strip()
    price_el= price.text.strip()
    link_element = div_element.find('a')
    href = link_element['href']
    if "Korg" in title_text:
        print(title_text, price_el, href)
