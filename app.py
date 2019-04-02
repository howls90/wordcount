from flask import Flask
import os
import logging
from logging import Formatter, FileHandler
from apis.v1 import v1, api

app = Flask(__name__)
app.register_blueprint(v1, url_prefix='/v1')
api.init_app(app)

def setUpLogs():
    file_handler = FileHandler('output.log')
    handler = logging.StreamHandler()
    file_handler.setLevel(logging.DEBUG)
    handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s ''[in %(pathname)s:%(lineno)d]'))
    handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s ''[in %(pathname)s:%(lineno)d]'))
    app.logger.addHandler(handler)
    app.logger.addHandler(file_handler)
    app.logger.error('WordCount API running...')

if __name__ == "__main__":
    setUpLogs()
    app.run(host='0.0.0.0', debug=True)