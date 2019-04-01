from database import DB
from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import current_app

def pullOutData(url):
    ''' Pull out data from the url '''
    html = urlopen(url) # if not exist error
    soup = BeautifulSoup(html, 'html.parser')
    current_app.logger.error(soup.find('body').get_text())
    return soup

def findNumberTimes(data, word):
    ''' Parse data ''' #10 results
    # valid_words = [word,'{}.'.format(word), '{},'.format(word)] 
    lines = data.find_all(text=lambda text: text and "{}".format(word) in text) #check mes de un per line
    count = 0
    for line in lines:
        if word in line:
            count += 1
    return count

def process(wordcount):
    ''' Process data '''
    db = DB() 
    count = db.read(wordcount.url)
    if count is not None:
        wordcount.count = int(count)
    else:        
        data = pullOutData(wordcount.url)
        wordcount.count = findNumberTimes(data, wordcount.word)
        db.save(wordcount.url, wordcount.count)
    return wordcount