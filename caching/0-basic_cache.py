#!/usr/bin/python3
"""
Create a class BasicCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache Class
    """

    
    def __init__(self):
        super().__init__()

    
    def put(self, key, item):
        """
        put Function
        """
        if (key == None or item == None):
            return

        self.cache_data[key] = item
        return

    
    def get(self, key):
        """
        get Function
        """
        if (key == None):
            return None
        
        if (key not in self.cache_data):
            return None

        return self.cache_data[key]
