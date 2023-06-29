import requests
from bs4 import BeautifulSoup
import tkinter as tk
import webbrowser

location_l = ""
people = ""

def open_link(event):
    link = event.widget.cget("text")
    webbrowser.open_new_tab(link)

# GUI code
root = tk.Tk()
root.title("Search")

# Location label and entry
location_label = tk.Label(root, text="Location:", font=("Arial", 12, "bold"))
location_label.pack()
location_entry = tk.Entry(root, font=("Arial", 12))
location_entry.pack()

# Number of stars label and entry
people_label = tk.Label(root, text="Number of people:", font=("Arial", 12, "bold"))
people_label.pack()
people_entry = tk.Entry(root, font=("Arial", 12))
people_entry.pack()

# Scraping code
url = "https://travelminit.ro/ro/cazare/romania?t=HST"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

names = soup.find_all('span', 'name')
stars_data = soup.find_all('span', 'classification')
locations = soup.find_all('strong', itemprop='addressLocality')
nr_people = soup.find_all('ul', class_='extra clearfix')
links = soup.find_all('div', class_='clearfix')

prefix = "https://travelminit.ro/"

def search_results():
    global location_l, people
    location_l = location_entry.get()
    people = people_entry.get()
    print('Location:', location_l)
    print("Number of people:", people)
    
    result_text.delete(1.0, tk.END)  # Clear the result_text widget
    
    found_results = False

    for name, stars, location, nr_p, link in zip(names, stars_data, locations, nr_people, links):
        name_text = name.text.strip()
        star_count = len(stars.find_all('i', 'tico-hotel-star'))
        location_text = location.text.strip()
        number_of_people = nr_p.find('i', class_='tico tico-users tico-extra').next_sibling.strip()
        nr = number_of_people.split()[0]
        link_text = link.find('a')
        link_text = prefix + link_text.get('href')
        if location_l.lower() == location_text.lower() and int(people) <= int(nr):
            found_results = True
            result_text.insert(tk.END, f"{name_text}, {star_count} stars\n")
            result_text.insert(tk.END, f"Location: {location_text}\n")
            result_text.insert(tk.END, f"Number of people: {number_of_people}\n")
            result_text.insert(tk.END, f"Link: ")
            result_text.insert(tk.END, link_text, "link")
            result_text.insert(tk.END, "\n\n")
             
        print(name_text, star_count, location_text, number_of_people, nr, link_text)

    if not found_results:
        result_text.tag_configure("no_results", font=("Arial", 20, "bold"), justify="center")
        result_text.insert(tk.END, "No results", "no_results")
        
# Search button
search_button = tk.Button(root, text="Search", font=("Arial", 12, "bold"), command=search_results)
search_button.pack()

# Result text widget
result_text = tk.Text(root, height=30, width=70)
result_text.pack()

root.mainloop()

