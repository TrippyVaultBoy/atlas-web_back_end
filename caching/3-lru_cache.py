#!/usr/bin/python3
"""
Create a class LRUCache that inherits from
BaseCaching and is a caching system
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LRU class
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        put method
        """

        if (key is None or item is None):
            return

        if (key in self.cache_data):
            self.cache_data.move_to_end(key)

        self.cache_data[key] = item

        if (len(self.cache_data) > self.MAX_ITEMS):
            lru_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD: " + lru_key)

    def get(self, key):
        """
        get method
        """
        if (key is None or key not in self.cache_data):
            return None

        self.cache_data.move_to_end(key)
        return self.cache_data[key]
