from flask_restplus import Api
from .wordcount import api as wordcount


api = Api(
    title='WordCount API',
    version='1.0',
    description='Backend task to count how many times a certain word appear in a url',
    catch_all_404s=True
)

api.add_namespace(wordcount, path='/count')
