from __future__ import print_function
from flask import current_app
import boto3
from botocore.exceptions import ClientError
from werkzeug.exceptions import InternalServerError
import decimal
import json


class DB:
    __instance = None
    table_name = None
    client = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if DB.__instance == None:
            DB()
        return DB.__instance 

    def __init__(self):
        """ Virtually private constructor. """
        if DB.__instance != None:
            DB.getInstance()
        else:
            DB.__instance = self

    def conn(self, table_name, region_name, endpoint_url, aws_access_key_id, aws_secret_access_key):
        '''Create connection'''
        DB.table_name = table_name
        DB.client = boto3.resource('dynamodb', 
                                    region_name = region_name, 
                                    endpoint_url = endpoint_url, 
                                    aws_access_key_id = aws_access_key_id, 
                                    aws_secret_access_key = aws_secret_access_key)

    def createTable(self):
        ''' Create Table if not exist '''
        try:
            table = DB.client.create_table(
                TableName = DB.table_name,
                KeySchema = [
                    {
                        'AttributeName': 'word',
                        'KeyType': 'HASH'  #Partition key
                    },
                    {
                        'AttributeName': 'url',
                        'KeyType': 'RANGE'  #Sort key
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'word',
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': 'url',
                        'AttributeType': 'S'
                    },
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10
                }
            )
            current_app.logger.error('Table successfully created!')
        except ClientError as ce:
            if str(ce) != 'An error occurred (ResourceInUseException) when calling the CreateTable operation: Cannot create preexisting table':
                current_app.logger.error(ce)
                raise InternalServerError()

    def save(self, word, url, count):
        ''' Save item to the database '''
        try:
            table = DB.client.Table(DB.table_name)
            response = table.put_item(
                Item={
                        'word': word,
                        'url': url,
                        'count': count,
                    }
            )
        except ClientError as e:
            current_app.logger.error(e.response['Error']['Message'])
        else:
            return True

    def read(self, word, url):
        ''' Add item to the database '''
        try:
            table = DB.client.Table(DB.table_name)
            response = table.get_item(
                Key={
                    'word': word,
                    'url': url
                }
            )
        except ClientError as e:
            current_app.logger.error(e.response['Error']['Message'])
        else:
            if response.get('Item') != None:
                current_app.logger.error(response['Item']['count'])
                return response['Item']['count']
        return None 

    def delete(self):
        ''' Delete Table '''
        try:
            table = DB.client.Table(DB.table_name)
            table.delete()
        except ClientError as e:
            current_app.logger.error(e.response['Error']['Message'])        