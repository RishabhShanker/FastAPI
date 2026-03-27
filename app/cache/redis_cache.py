import json
import redis
from app.core.config import settings

redis_client = redis.Redis.from_url(settings.REDIS_URL)

def get_cached_prediction(key):
    cached_value = redis_client.get(key)
    if cached_value:
        return json.loads(cached_value)
    return None

def set_cached_prediction(key:str, value:dict, expiry: int = 3600):
    redis_client.setex(key, expiry, json.dumps(value))