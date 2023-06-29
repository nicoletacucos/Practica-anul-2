#afisare anunuturi de munca, afisare numar de telefon

import tkinter as tk
from tkinter import messagebox
import webbrowser
import requests
from bs4 import BeautifulSoup

def search_jobs_by_keyword(keyword):
    url = "https://www.olx.ro/locuri-de-munca/?q="
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    titles = soup.find_all('h6', class_='css-1jmx98l')
    salaries = soup.find_all('p', class_='css-1hp12oq')
    links = soup.find_all('a', class_='css-rc5s2u')

    prefix = "https://www.olx.ro/"

    filtered_data = []

    for title, salary, link in zip(titles, salaries, links):
        title_text = title.text.strip()
        salary_text = salary.text.strip()
        salary_without_last_character = salary_text[:-1]
        link_text = link.text.strip()
        href = prefix + link.get("href")
        if keyword.lower() in title_text.lower() or keyword.lower() in link_text.lower():
            filtered_data.append((title_text, salary_without_last_character, href))

    if filtered_data:
        root = tk.Tk() #fereastra principală a aplicației GUI
        root.geometry("800x600")  # Setează dimensiunile ferestrei
        root.title("Anunturi de munca")

        text_box = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
        text_box.pack(expand=True, fill=tk.BOTH) #obiectul text va ocupa tot spațiul disponibil în container, atât pe orizontală, cât și pe verticală

        for title, salary, href in filtered_data:
            text_box.insert(tk.END, f"{title}\nSalariu: {salary}\nLink: ")
            text_box.insert(tk.END, href, ("link", href))  # Adaugă linkul cu stilul "link"
            text_box.insert(tk.END, "\n\n")

            url1=href
            print(url1)
            
            response1 = requests.get(url1)
            soup1 = BeautifulSoup(response1.text, "html.parser")

            phone_element = soup1.find('a', {'class': 'css-v1ndtc', 'data-testid': 'primary-contact-phone'})
            if phone_element is not None:
                phone_number = phone_element['href'].split(':')[1]
                #print(phone_number)

        text_box.tag_configure("link", foreground="blue", underline=True)  # Stilul pentru link

        root.mainloop()
    else:
        messagebox.showinfo("Rezultate căutare", "Nu s-au găsit rezultate pentru cuvântul cheie introdus.")

# Interacțiunea cu utilizatorul
keyword = input("Introduceți cuvântul cheie pentru căutare: ")
search_jobs_by_keyword(keyword)

