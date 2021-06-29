import requests
from bs4 import BeautifulSoup
from task2 import group_by_year
import pprint
import json
def group_by_decade(movies):
    moviedec = {}
    list1 = []
    for index in movies: # for year
        mod = index%10
        decade=index-mod
        if decade not in list1:
            list1.append(decade) #it is creating list of decade
    list1.sort()
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10 = i + 9 ##dec10 = 1959
        for x in movies:
            if x <= dec10 and x>=i: ##dec10 = e.g 1959 or i = e.g 1950
                for v in movies[x]:
                    moviedec[i].append(v)
                with open("task_3.json","w") as file:
                    json.dump(moviedec,file,indent=4)    
    return(moviedec)
pprint.pprint(group_by_decade(dec_arg))