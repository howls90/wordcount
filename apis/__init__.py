from flask_restplus import Api

from .wordcount import api as wordcount
from .settings import api as settings


api = Api(
    title='WordCount API',
    version='1.0',
    description='Backend task to count how many times a certain word appear in a url',
)

api.add_namespace(wordcount, path='/count')
# api.add_namespace(settings, path='/settings')
