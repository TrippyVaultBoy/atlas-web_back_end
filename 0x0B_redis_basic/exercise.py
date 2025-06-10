#!/usr/bin/env python3
"""
create a Cache class and store method
"""
import redis
import uuid
from typing import Union, Callable, Optional, Any
import functools

def count_calls(method: Callable) -> Callable:
    """
    count_calls method
    """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

class Cache():
    """
    Chache class
    """


    def __init__(self):
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        
        self._redis.flushdb()
    
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store method
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], Any]] = None) -> Optional[Any]:
        """
        get method
        """

        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data
    
    def get_str(self, key: str) -> Optional[str]:
        """
        """

        return self.get(key, fn=lambda d: d.decode('utf-8'))
    
    def get_int(self, key: str) -> Optional[int]:
        """
        """

        return self.get(key, fn=lambda d: int(d))
