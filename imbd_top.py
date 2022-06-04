import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"
response = requests.get(url)

htmlV = response.content
soup = BeautifulSoup(htmlV, "html.parser")

titles = soup.find_all("td", {"class": "titleColumn"})
ratings = soup.find_all("td", {"class": "ratingColumn imdbRating"})

for title, rating in zip(titles, ratings):
    title = title.text
    title = title.strip()
    title = title.replace("\n", " ")

    rating = rating.text
    rating = rating.strip()
    rating = rating.replace("\n", " ")

    print("TITLE: ", title)
    print("RATING: ", rating)
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

