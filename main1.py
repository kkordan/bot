import requests
from bs4 import BeautifulSoup as BS
#парсинг
hed = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36'
}
r = requests.get(url="https://kinosmena.ru/", headers=hed)

html = BS(r.content,'html.parser')


for el in html.find_all("div", class_='EventList__Event-sc-14wck6-3 dKUEol event rental large'):
    t = el.find_all("a",class_="event-name")
    print(t[0].text)

for el in html.find_all("div", class_='EventList__Event-sc-14wck6-3 dKUEol event rental pushkin-card large'):
    t = el.find_all("a",class_="event-name")
    print(t[0].text)

