from task1 import scrape_top_list
import requests
from bs4 import BeautifulSoup
import json
import pprint
s=scrape_top_list()
def group_by_year(movies):
    years=[]
    for i in movies:
        y=i['year']
        if y not in years:
            years.append(y)
    movie_dict={i:[]for i in years}
    for i in movies:
        y=i["year"]
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(movies[i])
            with open("task2.json","w") as d:
                data2=json.dump(movie_dict,d,indent=3)
    return movie_dict
group_by_year(s)

