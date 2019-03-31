from flask import current_app
from validator_collection import validators, checkers


class WordCountRequest:
    '''Rquest data'''
    def __init__(self, args, count = 0):
        self.url = args["url"]
        self.word = args["word"]
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
        pass