import requests
import http.client 
http.client._MAXHEADERS = 1000

stran = requests.get(
    "https://worldathletics.org/records/all-time-toplists/sprints/100-metres/outdoor/women/senior"
)


with open("stran1.html", "w", encoding='utf-8') as dat:
    dat.write(stran.text)

for i in range(1, 10):
    stran = requests.get(
        f"https://worldathletics.org/records/all-time-toplists/sprints/100-metres/outdoor/women/senior?page={i}"
    )
    with open(f"stran{i}.html", "w", encoding='utf-8') as dat:
        dat.write(stran.text)
