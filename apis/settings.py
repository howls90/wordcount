from flask_restplus import Namespace, Resource, fields, inputs
from flask import current_app
from flask import Flask, request, jsonify
from core import pullOutData, findNumberTimes
from requests import WordCountRequest
from database import DB

db = DB()

api = Namespace('Testing', description='Count how many times a word appear in a URL')

count_model = api.model('Count', {
    'url': fields.String(required=True, description='http://www.virtusize.com'),
    'word': fields.String(required=True, description='fit'),
})

count_request = api.parser()
count_request.add_argument('data', 
                            required=True,
                            help='Must be String', 
                            location='json')

@api.route('/')
class Count(Resource):
    @api.doc('WordCount')
    @api.expect(count_model)
    @api.doc(parser=count_request)
    @api.marshal_with(count_model, code=200)
    @api.doc(responses={
        500: 'Internal Server Error',
        400: 'Validation Error'
    })
    def post(self):
        '''Count number of times word appear in URL'''
        args = count_request.parse_args()
        current_app.logger.error(args)
        # request = WordCountRequest(count_request.parse_args())

        # count = db.read(request.url)
        # if count is not None:
        #     request.count = int(count)
        # else:        
        #     data = pullOutData(request.url)
        #     request.count = findNumberTimes(data, request.word)
        #     db.save(request.url, request.count)

        # return {"word":request.word,"url":request.url,"count":request.count}, 200
