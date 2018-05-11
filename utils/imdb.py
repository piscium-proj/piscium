import redis
from config import redis_option

redis_connection = redis.StrictRedis(redis_option)