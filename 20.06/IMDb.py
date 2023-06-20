import requests 
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

movie_containers = soup.find_all("td", class_="titleColumn")

for container in movie_containers:
    title = container.a.text
    print(f"{title}")