from flask import Flask
import logging
from logging import Formatter, FileHandler
from apis.v1 import v1, api
from database import DB

app = Flask(__name__)
api.init_app(app)
app.register_blueprint(v1)

def setUpLogs():
    ''' Setup the logs configuration ''' 
    file_handler = FileHandler('output.log')
    handler = logging.StreamHandler()
    file_handler.setLevel(logging.DEBUG)
    handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s ''[in %(pathname)s:%(lineno)d]'))
    handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s ''[in %(pathname)s:%(lineno)d]'))
    app.logger.addHandler(handler)
    app.logger.addHandler(file_handler)

def setUpDb(config):
    ''' Setup the database and create the table ''' 
    app.config.from_object(config)   
    with app.app_context():
        db = DB()
        db.conn(
                table_name = app.config["TABLE_NAME"][0],
                region_name = app.config["REGION_NAME"][0], 
                endpoint_url = app.config["ENPOINT_URL"][0], 
                aws_access_key_id = app.config["AWS_ACCESS_KEY_ID"][0], 
                aws_secret_access_key = app.config["AWS_SECRET_ACCESS_KEY"][0])
        db.createTable()

if __name__ == "__main__":
    setUpLogs()
    setUpDb('config.DevelopmentConfig')
    app.run(host="0.0.0.0")
