import requests
from bs4 import BeautifulSoup

def scraper(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.select("div[class*=FpEdX]")
    if(results):
        price = int(results[0].text.strip()[1:].replace(',',''))
    else:
        price = 2000
    return price

