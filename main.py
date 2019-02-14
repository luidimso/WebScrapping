import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

startTime = time.time()
url = "https://www.magazineluiza.com.br/playstation-4-slim-hits-bundle-1tb-sony-1-controle-com-3-jogos/p/043077200/ga/gap4/"
selectorName = "div.header-product > h1"
selectorPrice = ".price-template-price-block meta[itemprop='price']"

response = requests.get(url).content
soup = BeautifulSoup(response, "html.parser")

name = soup.select(selectorName)[0].text
print(name)

price = soup.select(selectorPrice)[0]["content"]
print(price)

print("--- %s seconds ---" % (time.time() - startTime))

chromeOpitions = Options()
chromeDriver = "./chromedriver"

nav = webdriver.Chrome(chromeDriver, options=chromeOpitions)
nav.get(url)

navName = nav.find_element_by_css_selector(selectorName).text
print(navName)

navPrice = nav.find_element_by_css_selector(selectorPrice).get_attribute("content")
print(navPrice)

print("--- %s seconds ---" % (time.time() - startTime))
