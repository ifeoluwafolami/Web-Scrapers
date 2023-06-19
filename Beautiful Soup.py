#Getting data from the internet is called web scrapping.
from bs4 import BeautifulSoup
import requests

search = input("What are you looking for? ")
params = {'q' : search}
r = requests.get("https://jumia.com.ng/catalog/", params=params)
print(r.url)

soup = BeautifulSoup(r.text, features='html.parser')

with open('jumia search.txt', 'w+', encoding='utf-8') as jumia_search:
    jumia_search.write(soup.prettify())