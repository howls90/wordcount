from flask_restplus import Namespace, Resource, fields, inputs
from flask import current_app
from flask import Flask, request, jsonify
from models import WordCountSchema
from services import WordCountService

api = Namespace('Testing', description='Count how many times a word appear in a URL')

request_model = api.model('Request', {
    'url': fields.String(required=True, description='URL to search'),
    'word': fields.String(required=True, description='Word to search'),
    'cache': fields.Boolean(required=False, description='Get from database '),
})

response_model = api.model('Response', {
    'url': fields.String(required=True, description='URL to search'),
    'word': fields.String(required=True, description='Word to search'),
    'count': fields.Integer(required=True, description='Number or time word appear'),
})

@api.route('/')
class Count(Resource):
    @api.doc('WordCount')
    @api.expect(request_model)
    @api.marshal_with(response_model, code=200)
    @api.doc(responses={
        500: 'Internal Server Error',
        400: 'Validation Error'
    })
    def post(self):
        '''Count number of times word appear in URL'''
        request = WordCountSchema().load(api.payload)
        if request.errors:
            return request.errors, 400

        res = WordCountService.process(request.data)
        
        return res, 200
