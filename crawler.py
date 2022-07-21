# import libraries
from inspect import getcomments
from tkinter.font import names
from bs4 import BeautifulSoup
import requests

# Grab website URL
URL = 'https://www.amazon.com/s?k=ground+coffee&crid=1VYJIVSJBDG9E&qid=1658426638&sprefix=ground+coffee%2Caps%2C178&ref=sr_pg_1'
headers={
    'Host': 'www.amazon.com',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

# get the page content
def getSoup(url, headers):
    r = requests.get(url=URL, headers=headers)
    return BeautifulSoup(r.text, 'html.parser')


def getName(soup):
    # get data of all the coffee on the page
    results = soup.find_all('div', {'class': "a-section a-spacing-small s-padding-left-small s-padding-right-small"})

    coffeeName=[]
    for item in results:
        name = item.find('span', {'class': 'a-size-base-plus a-color-base a-text-normal'}).get_text()
        coffeeName.append(name)
    return coffeeName

def getPrice(soup):
    results = soup.find_all('div', {'class': "a-section a-spacing-small s-padding-left-small s-padding-right-small"})

    price=[]
    for item in results:
        item_price = item.find('span', {'class': "a-offscreen"}).get_text()
        price.append(item_price)
    return price

def getNumRating(soup):
    num_ratings=[]
    pass

def getAvgRating(soup):
    avg_rating=[]
    pass

        # productData = {
        #     'name': item.find('span', {'class': 'a-size-base-plus a-color-base a-text-normal'}),
        #     'price_whole': item.find('span', {'class': 'a-price-whole'}),
        #     'price_fraction': item.find('span', {'class': 'a-price-fraction'}),
        #     'number_of_ratings': item.find('span', {'class': 'a-size-base s-underline-text'}),
        #     'avg_rating': item.find('span', {'class': 'a-icon-alt'})
        # }

def main():
    soup = getSoup(URL, headers)
    coffeeName = getName(soup)
    print(getPrice(soup))
    return



if __name__ =='__main__':
    main()
