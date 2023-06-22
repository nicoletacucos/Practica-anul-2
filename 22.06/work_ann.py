#afiseaza anunturile sub forma unei ferestre
import tkinter as tk
import webbrowser
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def open_link(event):
    webbrowser.open(event.widget.cget("text"))

def search_jobs_by_keyword(keyword):
    url = "https://www.olx.ro/locuri-de-munca/bucuresti/?gclid=Cj0KCQjw4s-kBhDqARIsAN-ipH2LAP53BcnoGLjpD4Fu3cnx3Ldvz4lOsODKnNl49FHu25KvmQJjhMwaAiWYEALw_wcB&utm_campaign=jobs-general-%5Bro%5D-shd-romania-np-ads-%5Bm%5D&utm_medium=cpc&utm_source=google"

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
        root = tk.Tk()
        root.geometry("800x600")  # Setează dimensiunile ferestrei (lățime x înălțime)
        root.title("Rezultate căutare")

        text_box = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
        text_box.pack(expand=True, fill=tk.BOTH)

        for title, salary, href in filtered_data:
            text_box.insert(tk.END, f"{title}\nSalariu: {salary}\nLink: ")
            text_box.insert(tk.END, href, ("link", href))  # Adaugă linkul cu stilul "link"

            # Adaugă funcția de deschidere a linkului la evenimentul de clic pentru link
            text_box.tag_bind(href, "<Button-1>", open_link)

            text_box.insert(tk.END, "\n\n")

        text_box.tag_configure("link", foreground="blue", underline=True)  # Stilul pentru link

        root.mainloop()
    else:
        messagebox.showinfo("Rezultate căutare", "Nu s-au găsit rezultate pentru cuvântul cheie introdus.")

# Interacțiunea cu utilizatorul
keyword = input("Introduceți cuvântul cheie pentru căutare: ")
search_jobs_by_keyword(keyword)
