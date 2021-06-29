import requests
from bs4 import BeautifulSoup
import json
import pprint
url="https://webscraper.io/test-sites"
data1=requests.get(url)
soup = BeautifulSoup(data1.text,'html.parser')
div1=soup.find_all("div",class_="col-md-7 pull-right")
list1=[]
serial_no=1
for i in div1:
    div2=i.find("h2",class_="site-heading").get_text().strip()
    link=i.find("h2",class_="site-heading").a["href"]
    q={"position":"","name":"","url":""}
    q["position"]=serial_no
    q["name"]=div2
    q["url"]=link
    list1.append(q.copy())
    serial_no+=1
with open("eco.json","w") as f:
    json.dump(list1,f,indent=3)