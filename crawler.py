# import libraries
from inspect import getcomments
from tkinter.font import names
from bs4 import BeautifulSoup
import requests

# Grab website URL
URL = 'https://www.amazon.com/s?k=coffee&crid=A34N1M202SCT&sprefix=coffee%2Caps%2C231&ref=nb_sb_noss_1'
headers={
    'Host': 'www.amazon.com',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

# get the page content and parse
def getSoup(url, headers):
    r = requests.get(url=URL, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

# get title of all the coffee on the page
def getTitle(soup):
    #names = []
    coffeeName= soup.find('span', class_="a-size-base-plus").get_text()
    return coffeeName

# find corresponding price for all coffee
def findPrice(soup):
    coffeePrice = soup.find('span', class_="a-price-whole").get_text()
    return coffeePrice


def main():
    soup = getSoup(URL, headers)
    coffeeName = getTitle(soup)
    coffeePrice = findPrice(soup)
    print(coffeeName, coffeePrice)

if __name__ =='__main__':
    main()
