import requests
from bs4 import BeautifulSoup
import json
import pprint
url=("https://www.imdb.com/india/top-rated-indian-movies/")
data = requests.get(url)
# htmlcontent = data.content
soup = BeautifulSoup(data.text,'html.parser')
div= soup.find("div",class_="lister")
body=div.find("tbody",class_="lister-list")
name=body.find_all("tr")
def scrape_top_list():
    top_movies=[]
    serial_no=1
    for i in name:
        movie=i.find("td",class_="titleColumn").a.get_text()
        year=i.find("td",class_="titleColumn").span.get_text()
        rating=i.find("td",class_="ratingColumn imdbRating").strong.get_text()
        url=i.find("td",class_="titleColumn").a["href"]
        d="https://www.imdb.com"+url
        details={"position":"","name":"","year":"","rating":"",'url':""}
        # for i in range (len(name)):
        details["position"]=serial_no
        details["name"]=(movie)
        year=year[1:5]
        details["year"]=int(year)
        details["rating"]=float(rating)
        details["url"]=d
        top_movies.append(details.copy())
        serial_no+=1
        with open("task1.json","w") as f:
            data = json.dump(top_movies,f,indent=4)
    # return (top_movies)
scrape_top_list()