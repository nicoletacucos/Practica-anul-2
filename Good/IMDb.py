#top 10 filme IMDb
import csv
import requests 
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

movie_containers = soup.find_all("td", class_="titleColumn")

with open("imdb_movies.csv", "w", newline="") as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(["Titlee", "Year"])
    for container in movie_containers[:10]:
        title = container.a.text
        year=container.span.text[1:5]
        print(title, year)
        writer.writerow([title, year])
