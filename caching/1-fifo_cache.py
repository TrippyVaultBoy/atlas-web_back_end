#!/usr/bin/python3
"""
Create a class FIFOCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        put Function
        """
        if (key is None or item is None):
            return

        self.cache_data[key] = item

        if (len(self.cache_data) > self.MAX_ITEMS):
            first_item = next(iter(self.cache_data.keys()))
            self.cache_data.pop(first_item)
            return

        return

    def get(self, key):
        """
        get Function
        """

        if (key is None or key not in self.cache_data):
            return None

        return self.cache_data[key]
