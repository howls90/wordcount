import json

mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}

def test_bad_character(client):
    '''Check bad word bad input not common characters'''
    data = {
        'word':'@$^*&',
        'url':'http://www.virtusize.com'
    }
    response = client.post("/count/", data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json == {'count': None, 'url': None, 'word': "['Word must be alphanumeric']"}


def test_bad_word_break_line(client):
    '''Check bad word bad input line break'''
    data = {
        'word':'@$^*&\n',
        'url':'http://www.virtusize.com'
    }
    response = client.post("/count/", data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json == {'count': None, 'url': None, 'word': "['Word must be alphanumeric']"}

def test_bad_word_spaces(client):
    '''Check bad word bad input not spaces'''
    data = {
        'word':'@$^* &',
        'url':'http://www.virtusize.com'
    }
    response = client.post("/count/", data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json == {'count': None, 'url': None, 'word': "['Word must be alphanumeric']"}

def test_bad_url_protocol(client):
    '''Check bad url bad input not protocol'''
    data = {
        'word':'fit',
        'url':'www.virtusize.com'
    }
    response = client.post("/count/", data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json["url"] == "['Not a valid URL.']"

def test_bad_url_domain(client):
    '''Check bad url bad input bad domain'''
    data = {
        'word':'fit',
        'url':'http://www.virtusize'
    }
    response = client.post("/count/", data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json == {'message': 'URL not found'} != {'message': 'Input payload validation failed'}

def test_sucess(client):
    '''Check bad word bad input not spaces'''
    data = {
        "word":"fit",
        "url":"http://www.virtusize.com"
    }
    response = client.post("/count/", data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    assert response.json == {'count': 10, 'url': 'http://www.virtusize.com', 'word': 'fit'}
