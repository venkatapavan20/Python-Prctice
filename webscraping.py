import requests
from bs4 import BeautifulSoup


req = requests.get("https://m.cricbuzz.com/")

soup = BeautifulSoup(req.content,"html.parser")
detail=soup.select(".cb-col-100 .cb-col .cb-col-scores")
for i in detail:
    print(i.getText())


print(soup)



