from flask_restplus import Namespace, Resource, fields, inputs
from flask import current_app
from core import pullOutData, findNumberTimes
from requests import WordCountRequest
from database import DB
from validator_collection import validators, checkers


db = DB()

api = Namespace('Count', description='Count how many times a word appear in a URL')

count_model = api.model('Count', {
    'url': fields.String(required=True, description='URL to parser'),
    'word': fields.String(required=True, description='Word to Count'),
    'count': fields.Integer(required=True, description='Number of times word in URL'),
})

count_request = api.parser()
count_request.add_argument('word', 
                            required=True,
                            type=inputs.regex('^[a-zA-Z0-9]+$'), #check
                            help='Must be String', 
                            location='form')
count_request.add_argument('url', 
                            type=inputs.URL(schemes=['http', 'https'], check=True), # allow IPS
                            required=True, 
                            help='Please enter a valid URL format', 
                            location='form')
count_request.add_argument('cache', 
                            type=bool, 
                            required=False, 
                            help='Read from Database', 
                            location='form')

@api.route('/')
class Count(Resource):
    @api.doc('WordCount')
    @api.doc(parser=count_request)
    @api.marshal_with(count_model, code=200)
    @api.doc(responses={
        500: 'Internal Server Error',
        400: 'Validation Error'
    })
    def post(self):
        '''Count number of times word appear in URL'''
        request = WordCountRequest(count_request.parse_args())

        count = db.read(request.url)
        if count is not None:
            request.count = int(count)
        else:        
            data = pullOutData(request.url)
            request.count = findNumberTimes(data, request.word)
            db.save(request.url, request.count)

        return {"word":request.word,"url":request.url,"count":request.count}, 200
