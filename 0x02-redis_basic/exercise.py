#!/usr/bin/env python3
"""
Redis Module
"""
import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """
    Cache class
    """
    def __init__(self):
        """
        store an instance of the Redis client named _redis
        (using redis.Redis()) and flush the instance using flushdb
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store method that takes a data argument and returns a string.
        The method generates a random key, stores the input data in Redis
        using the random key and returns the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        take a key string argument and an optional Callable argument named fn.
        This callable willbe used to convert the data to the desired format.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is None:
            return data
        return fn(data)

    def get_str(self, key: str) -> Optional[str]:
        """
        retrieves the value of key and converts it into string
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        retrieves the value of key and converts it into integer
        """
        return self.get(key, fn=int)


cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
