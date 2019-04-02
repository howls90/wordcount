from redis import Redis, RedisError
from flask import current_app

class DB:
    def __init__(self):
        '''Create connection'''
        self.r = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

    def save(self, key, value):
        '''Save results'''
        try:
            self.r.set(key, value)
        except Exception as e:
            current_app.logger.error(e)

    def read(self, key):
        '''Read results'''
        msn = None
        try:
            msg = self.r.get(key)
        except Exception as e:
            current_app.logger.error(e)
        return msg



# from __future__ import print_function
# import boto3
# import decimal
# import json


# dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

# TABLE_NAME = 'WordCount'

# # Helper class to convert a DynamoDB item to JSON.
# class DecimalEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, decimal.Decimal):
#             if o % 1 > 0:
#                 return float(o)
#             else:
#                 return int(o)
#         return super(DecimalEncoder, self).default(o)


# table = dynamodb.create_table(
#     TableName=TABLE_NAME,
#     KeySchema=[
#         {
#             'AttributeName': 'word',
#             'KeyType': 'HASH'  #Partition key
#         },
#         {
#             'AttributeName': 'url',
#             'KeyType': 'RANGE'  #Sort key
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'word',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'url',
#             'AttributeType': 'S'
#         },

#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 10,
#         'WriteCapacityUnits': 10
#     }
# )

# print("Table status:", table.table_status)

# # PUT
# table = dynamodb.Table(TABLE_NAME)

# word = "aaa"
# url = "bbbbb"

# response = table.put_item(
#    Item={
#         'word': word,
#         'url': url,
#         'info': {
#             'plot':"Nothing happens at all."
#         }
#     }
# )

# print("PutItem succeeded:")
# print(json.dumps(response, indent=4, cls=DecimalEncoder))

# # Read

# try:
#     response = table.get_item(
#         Key={
#             'word': word,
#             'url': url
#         }
#     )
# except ClientError as e:
#     print(e.response['Error']['Message'])
# else:
#     item = response['Item']
#     print("GetItem succeeded:")
#     print(json.dumps(item, indent=4, cls=DecimalEncoder))
        