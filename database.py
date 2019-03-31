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
        