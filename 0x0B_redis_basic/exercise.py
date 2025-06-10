"""
create a Cache class and store method
"""
import redis
import uuid
from typing import Union


class Cache():
    """
    Chache class
    """


    def __init__(self):
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        
        self._redis.flushdb()
    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store method
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
