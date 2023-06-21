#zilele cu 30 de grade + pe o saptamana redirectionate intr-un csv si notificare cu vremea pe ziua respectiva

import csv
import notify2
import requests
from bs4 import BeautifulSoup
import time

# Inițializează biblioteca notify2
notify2.init("My Notification App")

while True:
    url = "https://weather.com/ro-RO/weather/tenday/l/Bucure%C8%99ti?canonicalCityId=09ab35eae00f21604b305d3aa496ff31777f8979cf6cfa560e1dd22133813806"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    day_elements = soup.find_all('h3', class_='DetailsSummary--daypartName--kbngc')
    temp_elements=soup.find_all('span', class_='DetailsSummary--highTempValue--3PjlX')
    condition_elements = soup.find_all('span', class_='DetailsSummary--extendedData--307Ax')

    with open("weather.csv", "w", newline="") as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(["Day", "Temperature"])
        for day_element, temp_element, condition_element in zip(day_elements, temp_elements, condition_elements):
            temp=temp_element.text.strip()
            day = day_element.text.strip()
            condition=condition_element.text.strip()
            if day=='Astăzi':
                notification = notify2.Notification("Atentie!", f"Astazi se anunta {temp}! {condition}.")
                notification.show()
            if temp>='30°':
                writer.writerow([day, temp])
 # Așteaptă 3 ore înainte de a relua programul
    time.sleep(3 * 60 * 60)  # 3 ore în secunde
~                                                  