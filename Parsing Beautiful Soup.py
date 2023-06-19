from random import randint
from time import *
from bs4 import BeautifulSoup
import requests

search = input('Search for: ')

params = { 'q' : search}

r = requests.get("https://google.com/search", params=params)

soup = BeautifulSoup(r.text, 'html.parser')

# headings = soup.find_all('h3')

results = soup.findAll('div', {'class' : 'egMi0 kCrYT'})


for result in results:
    result_text = result.find('h3').text
    result_link = result.find('a').attrs['href']
    if result_link[:7] == "/url?q=":
        result_link = result_link[7:]

    if result_text and result_link:
        print(result_text)
        print(result_link)
        print("-------------")
    x = randint(2,5)
    sleep(x)


# for heading in headings:
#     print(heading.getText())
#     print("---------------")