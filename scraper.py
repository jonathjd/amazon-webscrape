# import libraries
from inspect import getcomments
from tkinter.font import names
from bs4 import BeautifulSoup
import requests

URL = 'https://www.amazon.com/s?k=ground+coffee&page=1&crid=1VYJIVSJBDG9E&qid=1658430622&sprefix=ground+coffee%2Caps%2C178&ref=sr_pg_1'
headers={
    'Host': 'www.amazon.com',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

def getSoup(url, headers): # will get the soup for the current page
    r = requests.get(url=URL, headers=headers)
    return BeautifulSoup(r.text, 'html.parser')

def getName(soup): # get name of each coffee product on page
    results = soup.find_all('div', {'class': "a-section a-spacing-small s-padding-left-small s-padding-right-small"})
    coffeeName=[]

    for item in results:
        try:
            name = item.find('span', {'class': 'a-size-base-plus a-color-base a-text-normal'}).get_text()
        except:
            name = "Name Unavailable"
        coffeeName.append(name)
    return coffeeName

def getPrice(soup): # get price of each coffee product on page
    results = soup.find_all('div', {'class': "a-section a-spacing-small s-padding-left-small s-padding-right-small"})
    price=[]

    for item in results:
        try:
            item_price = item.find('span', {'class': "a-offscreen"}).get_text()
        except:
            item_price = "Price Unavailable"
        price.append(item_price)
    return price

def getNumRating(soup): # get number of ratings for each coffee product on page
    results = soup.find_all('div', {'class': "a-section a-spacing-small s-padding-left-small s-padding-right-small"})
    num_ratings=[]
    
    for item in results:
        try:
            item_rating = item.find('span', {'class': "a-size-base s-underline-text"}).get_text()
        except:
            item_rating = "Rating Unavailable"
        num_ratings.append(item_rating)
    return num_ratings

def getAvgRating(soup): # get avg rating of each coffee product on page
    results = soup.find_all('div', {'class': "a-section a-spacing-small s-padding-left-small s-padding-right-small"})
    avg_ratings=[]

    for item in results:
        try:
            avg_rating = item.find('span', {'class': "a-icon-alt"}).get_text()
        except:
            avg_rating = "Rating Unavailable"
        avg_ratings.append(avg_rating)
    return avg_ratings

def getProductSize(soup): # get the size of each coffee product on page
    results = soup.find_all('div', {'class': "a-section a-spacing-small s-padding-left-small s-padding-right-small"})
    product_size=[]

    for item in results:
        try:
            size = item.find('span', {'class': "a-color-information a-text-bold"}).get_text()
        except:
            size = "Size Unavailable"
        product_size.append(size)
    return product_size

def main():
    # declare page number for while loop
    page = 1

    # amazon only presents 7 pages of products
    while page != 8:
        URL = f'https://www.amazon.com/s?k=ground+coffee&page={page}&crid=1VYJIVSJBDG9E&qid=1658430602&sprefix=ground+coffee%2Caps%2C178&ref=sr_pg_{page}'
        soup = getSoup(URL, headers)

        if page == 1:
            coffee_name = getName(soup)
            coffee_price = getPrice(soup)
            coffee_rating = getNumRating(soup)
            coffee_avg_ratings = getAvgRating(soup)
            coffee_product_size = getProductSize(soup)
        else:
            coffee_name += getName(soup)
            coffee_price += getPrice(soup)
            coffee_rating += getNumRating(soup)
            coffee_avg_ratings += getAvgRating(soup)
            coffee_product_size += getProductSize(soup)
        
        page+=1 # increment page number

    # create dictonary from
    return



if __name__ =='__main__':
    main()
