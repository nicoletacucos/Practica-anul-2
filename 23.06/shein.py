#motor de cautare pentru anunturile NEW IN de pe shein, la fiecare anunt gasit se poate deschide pagina web
import webbrowser
import requests
from bs4 import BeautifulSoup

def search_jobs_by_keyword(keyword):
    url = "https://euqs.shein.com/daily-new.html?icn=what%27snew&ici=euqs_tab01navbar01&src_module=topcat&src_tab_page_id=page_home1687497810161&src_identifier=fc%3DWomen%60sc%3DNEW%20IN%60tc%3D0%60oc%3D0%60ps%3Dtab01navbar01%60jc%3Ddailynew_0&srctype=category&userpath=category-NEW-IN"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    prefix= "https://euqs.shein.com/"
    titles = soup.find_all('a', class_='S-product-item__link_jump S-product-item__link')
    links=soup.find_all('a', class_='S-product-item__img-container j-expose__product-item-img')
    for title, link in zip(titles, links):
        title_text ="\033[1m" + title.text.strip()+ "\033[0m"
        link_text=prefix+link['href']
        if keyword.lower() in title_text.lower() or keyword.lower() in link_text.lower():
            print(title_text,"\n",link_text)
            input("Apăsați Enter pentru a deschide următoarea pagină...")
            webbrowser.open_new_tab(link_text)

# Interacțiunea cu utilizatorul
keyword = input("Introduceți cuvântul cheie pentru căutare: ")
search_jobs_by_keyword(keyword)

