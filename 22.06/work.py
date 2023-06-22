#afiseaza anunturile de angajare prin intermediul unui filtru de text
import requests
from bs4 import BeautifulSoup

def search_jobs_by_keyword(keyword):
    url = "https://www.olx.ro/locuri-de-munca/bucuresti/?gclid=Cj0KCQjw4s-kBhDqARIsAN-ipH2LAP53BcnoGLjpD4Fu3cnx3Ldvz4lOsODKnNl49FHu25KvmQJjhMwaAiWYEALw_wcB&utm_campaign=jobs-general-%5Bro%5D-shd-romania-np-ads-%5Bm%5D&utm_medium=cpc&utm_source=google"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    titles = soup.find_all('h6', class_='css-1jmx98l')
    salaries = soup.find_all('p', class_='css-1hp12oq')
    links = soup.find_all('a', class_='css-rc5s2u')

    prefix = "https://www.olx.ro/"

    for title, salary, link in zip(titles, salaries, links):
        title_text = title.text.strip()
        salary_text = salary.text.strip()
        salary_without_last_character = salary_text[:-1]
        link_text = link.text.strip()
        href = prefix + link.get("href")
        
        #print(title_text, salary_without_last_character, href)
        if keyword.lower() in title_text.lower() or keyword.lower() in link_text.lower():
            print(title_text, salary_without_last_character, href)

# Interacțiunea cu utilizatorul
keyword = input("Introduceți cuvântul cheie pentru căutare: ")
search_jobs_by_keyword(keyword)

