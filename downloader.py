import requests
from bs4 import BeautifulSoup
from google import search
import urllib

query = raw_input()
quer = query + " tutorials point"
add = []
for j in search(quer, tld="com", num=1, stop=1, pause=2):
    add.append(j)

if "https://www.tutorialspoint.com" in add[0]:
    url = "https://www.tutorialspoint.com/" + str(query) + "/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    data = soup.find("button", class_="btn btn-default btn-sm btn-buy-tutorial")
    data = data.find('a')['href']

    url = "https://www.tutorialspoint.com" + data
    print url
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    data = soup.find_all("h1")
    rcf = []
    for i in data:
        rcf.append(i.find("a"))
    url = "https://tutorialspoint.com" + rcf[2]['href']
    urllib.urlretrieve(url, query+".pdf")
else:
    print "Sorry no results found"
