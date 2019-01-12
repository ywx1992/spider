import redis


class RedisHelper(object):
    def __init__(self, host='localhost', port=6379):
        self.__redis = redis.StrictRedis(host, port)

    def get(self, key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return ''

    def set(self, key, value):
        self.__redis.set(key, value, 120)


r = RedisHelper()
print(r.get('age').decode())
