#!/usr/bin/python3
"""
Create a class MRUCache that inherits from
BaseCaching and is a caching system
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
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
            del self.cache_data[key]

        if (len(self.cache_data) >= self.MAX_ITEMS):
            mru_key, _ = self.cache_data.popitem(last=True)
            print("DISCARD: " + mru_key)

        self.cache_data[key] = item

    def get(self, key):
        """
        get method
        """
        if (key is None or key not in self.cache_data):
            return None

        self.cache_data.move_to_end(key)
        return self.cache_data[key]
