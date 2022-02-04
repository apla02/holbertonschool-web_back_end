#!/usr/bin/env python3
""" Implement a caching system
    cache replacement algorithm - MRU
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """inherit from BaseCaching and is a caching system
    Args:
        BaseCaching (Father class): Implement methods
    """
    def __init__(self):
        """init method"""
        super().__init__()
        self.lst = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.lst.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = self.lst.pop(-2)
            print('DISCARD:', last)
            del self.cache_data[last]

    def get(self, key):
        """Obtain a value from dict by key
        """
        if key in self.cache_data:
            self.lst.append(key)
        if key in self.cache_data:
            return self.cache_data[key]
