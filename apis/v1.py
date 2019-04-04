from flask_restplus import Namespace, Resource, fields, inputs, Api
from flask import Flask, request, jsonify, Blueprint, current_app
from models.models import WordCountSchema
from services import WordCountService
from werkzeug.exceptions import BadRequest


blueprint = Blueprint('api_v1', __name__)
api = Api(
    blueprint,
    title='WordCount API',
    version='1.0',
    description='Wordcount number of times word appear (Letter case is taking into account)',
    doc="/doc/",
    default='Count', 
    default_label='Counter endpoints'
)

request_model = api.model('Request', {
    'url': fields.String('http://www.virtusize.com', required=True, description='URL to search'),
    'word': fields.String('fit', required=True, description='Word to search'),
})

response_model = api.model('Response', {
    'url': fields.String(required=True, description='URL to search'),
    'word': fields.String(required=True, description='Word to search'),
    'count': fields.Integer(required=True, description='Number or times word appear'),
})

errors_model_400 = api.model('Error400', {
    'message': fields.Raw(example = {"field":["Error description"]})
})

errors_model_404 = api.model('Error404', {
    'message': fields.Raw(example = 'URL was not found')
})

@api.route('/')
class Count(Resource):
    @api.doc('WordCount')
    @api.expect(request_model)
    @api.marshal_with(response_model, code=200)
    @api.response(code=400, model=errors_model_400, description='Bad request')
    @api.response(code=404, model=errors_model_404, description='Not Found')
    @api.doc(responses={500: 'INTERNAL SERVER ERROR'})
    def post(self):
        '''Count number of times word appear in URL'''
        request = WordCountSchema().load(api.payload)
        if request.errors:
            raise BadRequest(request.errors)

        res = WordCountService.process(request.data)
        
        return res, 200
