#!/usr/bin/env python3
"""
create a Cache class and store method
"""
import redis
import uuid
from typing import Union, Callable, Optional, Any
import functools
import inspect


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


def call_history(method: Callable) -> Callable:
    """
    call_history method
    """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = str(method.__qualname__ + ':inputs')
        output_key = str(method.__qualname__ + ':outputs')

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper


def replay(method: Callable) -> None:
    """
    replay function
    """

    redis_client = method.__self__._redis
    method_name = method.__qualname__
    input_key = method_name + ':inputs'
    output_key = method_name + ':outputs'

    call_count = redis_client.get(method_name)
    if call_count:
        call_count = int(call_count)
    else:
        call_count = 0

    print(f"{method_name} was called {call_count} times:")

    inputs = redis_client.lrange(input_key, 0, -1)
    outputs = redis_client.lrange(output_key, 0, -1)

    for input_args, output in zip(inputs, outputs):
        print(
            f"{method_name}(*{input_args.decode('utf-8')}) "
            f"-> {output.decode('utf-8')}"
        )


class Cache():
    """
    Chache class
    """

    def __init__(self):
        self._redis = redis.Redis(host='localhost', port=6379, db=0)

        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store method
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable[[bytes], Any]] = None) -> Optional[Any]:
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
