import requests
from bs4 import BeautifulSoup
import random

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

html = requests.get(url).content
soup = BeautifulSoup(html,'html.parser')

list = soup.find("tbody", {"class":"lister-list"}).find_all("tr")
i = random.randint(0,249)
liste = {"name":[],"year":[]}
for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).find("a").text
    year = tr.find("td",{"class":"titleColumn"}).find("span").text
    liste["name"].append(title)
    liste["year"].append(year)
    # print(f'{str(i)}-   {title} {year}')
    # i +=1

print(liste["name"][i],liste["year"][i])