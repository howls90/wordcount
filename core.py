from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import current_app

    
def pullOutData(url):
    '''Pull out data from the url'''
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def findNumberTimes(data, word):
    '''Parse data'''
    num = data.find_all(text=lambda text: text and " {} ".format(word) in text) #check mes de un per line
    return len(num)

