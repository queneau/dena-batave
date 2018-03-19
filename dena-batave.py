import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen("http://npb.jp/bis/teams/rst_db.html")
soup = BeautifulSoup(html, "html.parser")
rosterplayers = soup.find_all("td", class_ = "rosterRegister")

records = {}

for record in rosterplayers:
    name = record.string
    if record.find("a") is None:
        continue
    url = record.find("a").get("href")
    if url is None:
        continue
    recordurl = ("http://npb.jp/" + url)
    records[name] = recordurl

for player, url in records.items():
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    td = soup.find_all("td", class_ = "year")
    batave = []
    for record in td:
        years = record.find_all("td")
        if len(years) == 0:
            continue
        batave.append(float(years[19].string))       
    print(player)
    print(batave)