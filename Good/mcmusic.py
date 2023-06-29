import requests
from bs4 import BeautifulSoup
import re
import notify2

# Inițializează biblioteca notify2
notify2.init("My Notification App")

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
            print("\033[1m" + title_text + "\033[0m",', Price:', price_el, ', Link to:', href)
            price_value = float(price_el.replace(',', '').replace('\xa0', '').replace('lei', ''))
            if price_value < 7.500:
                notification = notify2.Notification("Preț redus la " + title_text, "Preț: " + price_el )
                notification.show()
