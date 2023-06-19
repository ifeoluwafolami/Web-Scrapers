from random import randint
from time import *
from bs4 import BeautifulSoup
import requests

search = input('Search for: ')

page = 1

while page < 10:

    params = {'page' : page, 'q' : search}

    r = requests.get("https://goodreads.com/search", params=params)

    f = open('goodreadssearch.html', 'w+', encoding='utf-8')

    f.write(r.text)

    soup = BeautifulSoup(r.text, 'html.parser')

    with open('./goodreadstitles.txt', 'w+', encoding='utf-8') as gr:
        gr.write(soup.prettify())


    results = soup.findAll('tr', {'itemtype' : "http://schema.org/Book"})


    for result in results:
        title = result.find('a', {'class' : 'bookTitle'}).text
        author = result.find('a', {'class' : 'authorName'}).text
        rating = result.find('span', {'class' : 'minirating'}).text
        # result_link = result.find('a').attrs['href']
        # if result_link[:7] == "/url?q=":
            # result_link = result_link[7:]

        if title and author:
            print(title)
            print(author)
            print('Average Rating: {}'.format(rating))
            print("-------------")

        else:
            print('No Results Found.')
            exit()
    
    x = randint(2,5)
    
    sleep(x)
    page += 1

