from flask_restplus import Namespace, Resource, fields, inputs, Api
from flask import Flask, request, jsonify, Blueprint, current_app
from models import WordCountSchema
from services import WordCountService

v1 = Blueprint('v1_api', __name__, url_prefix='/myapi')
api = Api(
    title='WordCount API',
    version='1.0',
    description='Backend task to count how many times a certain word appear in a url',
    catch_all_404s=True,
    doc="/doc/",
)

count = api.namespace('count', description='Count number of times word appear in URL')

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

@count.route('/test', endpoint='base-endpoint')
class BaseResource(Resource):
    def get(self):
        return {"from":"base"}


@count.route('/')
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