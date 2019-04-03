from database import DB
from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import current_app
from werkzeug.exceptions import BadRequest
import re

def getAndProcess(url, word):
    ''' Pull out data from the url and process it '''
    try:
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
    except:
        raise BadRequest('URL not found')
    
    lines = soup.find_all(text=re.compile(word))
    count = 0
    for line in lines:
        count += line.count(' {} '.format(word))
        count += line.count(' {},'.format(word))
        count += line.count(' {}.'.format(word))

    return count

def process(wordcount):
    ''' Process data '''
    db = DB() 
    count = db.read(wordcount.url)
    if count is not None:
        wordcount.count = int(count)
    else:        
        wordcount.count = getAndProcess(wordcount.url, wordcount.word)
        db.save(wordcount.url, wordcount.count)
    return wordcount