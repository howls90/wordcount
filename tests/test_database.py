from database import DB
from werkzeug.exceptions import InternalServerError
import pytest
import json
from app import app as server
from app import setUpDb

db = DB()

def test_read_item_failure(client):
    ''' Item not save in the DB '''
    data = {
        "url": "http://www.virtusize.com",
        "word": "fit",
    }
    response = db.read(**data)
    assert response == None

def test_add_item_success(client):
    '''Save item iin the DB'''
    data = {
        "url": "http://www.virtusize",
        "word": "fit",
        "count": 10
    }
    response = db.save(**data)
    assert response == True

def test_read_item_success(client):
    ''' Item not save in the DB '''
    data = {
        "url": "http://www.virtusize.com",
        "word": "fit",
        "count": 10
    }
    db.save(**data)

    data = {
        "url": "http://www.virtusize",
        "word": "fit",
    }
    response = db.read(**data)
    assert response == 10

def test_clean(client):
    ''' Clean DB'''
    db.delete()