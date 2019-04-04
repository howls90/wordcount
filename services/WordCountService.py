from database import DB
from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import current_app
from werkzeug.exceptions import NotFound
import re, json

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i,j)
    return text

def getAndProcess(url, word):
    ''' Pull out data from the url and process it '''
    try:
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
    except:
        raise NotFound('URL was not found')
    else:
        lines = soup.find_all(text=re.compile(word))
        opt = {".": " ", ",": " "}
        count = 0
        for line in lines:
            count += replace_all(line, opt).count(" {} ".format(word))

    return count

def process(wordcount):
    ''' Process data '''
    db = DB() 
    count = db.read(wordcount.url, wordcount.word)
    if count is not None:
        wordcount.count = int(count)
    else:        
        wordcount.count = getAndProcess(wordcount.url, wordcount.word)
        db.save(wordcount.url, wordcount.word, wordcount.count)
    return wordcount