# import libraries
from inspect import getcomments
from tkinter.font import names
from bs4 import BeautifulSoup
import requests

# Grab website URL
URL = 'https://www.amazon.com/s?k=coffee'
headers={
    'Host': 'www.amazon.com',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

# get the page content
def getSoup(url, headers):
    r = requests.get(url=URL, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

# def getNextPage(soup):
#     url_list = []
#     for i in range(1,8):
#         link = soup.find_all('a')
#         newURL = 'https://www.amazon.com' + link.get('href')
#         url_list.append(newURL)
#     return url_list




def getName(soup):
    # get data of all the coffee on the page
    results = soup.find_all('div', {'class': "a-section a-spacing-small s-padding-left-small s-padding-right-small"})

    coffeeName=[]
    for item in results:
        name = item.find('span', {'class': 'a-size-base-plus a-color-base a-text-normal'}).get_text()
        coffeeName.append(name)
    return coffeeName

def getPrice(soup):
    whole_price=[]
    # w_price = item.find('span', {'class': 'a-offscreen'}).text
    # whole_price.append(w_price)
    pass

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
    return



if __name__ =='__main__':
    main()
