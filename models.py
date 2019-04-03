from flask import current_app
from marshmallow import Schema, fields, validate, fields, post_load
from flask_restplus import inputs
import json

class WordCountModel(object):
    '''Rquest data'''
    def __init__(self, url, word, count = 0):
        self.word = word
        self.url = url
        self._count = count

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        if count < 0:
            raise ValueError('Cannot be negative')
        self._count = count

    def __str__(self):
        pass

    def __repr__(self):
        return json.dumps(self.__dict__)


class WordCountSchema(Schema):
    '''Serialize json'''
    word = fields.String(required=True, validate=validate.Regexp('^[a-zA-Z0-9]+$', 0,'Word must be alphanumeric'))
    url = fields.URL(required=True, relative=False, require_tld=False) #check without .

    @post_load
    def create_object(self, data):
        return WordCountModel(**data)