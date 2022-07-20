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
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def getNextPage(soup):
    for link in soup.find_all('a', class_="s-pagination-next"):
        newURL = 'https://www.amazon.com' + link.get('href')
        return newURL

def getData(soup):
    # get title & price of all the coffee on the page
    coffeeName= soup.find('span', class_="a-size-base-plus").get_text()    
    coffeePrice = soup.find('span', class_="a-price-whole").get_text()
    return coffeePrice

def main():
    soup = getSoup(URL, headers)
    newURL = getNextPage(soup)
    soup = getSoup(newURL, headers)
    print(newURL)

if __name__ =='__main__':
    main()
