#!/usr/bin/python3
"""
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Create a class LIFOCache that inherits
    from BaseCaching and is a caching system
    """

    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        put function
        """

        if (key is None or item is None):
            return

        if (key in self.cache_data):
            self.stack.remove(key)

        self.cache_data[key] = item
        self.stack.append(key)

        if (len(self.cache_data) > self.MAX_ITEMS):
            last_key = self.stack[-2]
            self.stack.remove(last_key)
            del self.cache_data[last_key]
            print("DISCARD: " + last_key)

    def get(self, key):
        """
        get function
        """

        if (key is None or key not in self.cache_data):
            return None

        return self.cache_data[key]
