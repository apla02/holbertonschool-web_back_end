#!/usr/bin/env python3
""" Implement a caching system
    cache replacement algorithm - FIFO
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """inherit from BaseCaching and is a caching system
    Args:
        BaseCaching (Father class): Implement methods
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

        len_cache = len(self.cache_data)
        if len_cache > self.MAX_ITEMS:
            index_dict = {}
            for i, j in enumerate(self.cache_data):
                index_dict.update({i: j})
            print(f"DISCARD: {index_dict.get(0)}")
            self.cache_data.pop(index_dict.get(0))

    def get(self, key):
        """Obtain a value from dict by key
        """
        if key is not None:
            value = self.cache_data.get(key)
            if value is None:
                return None
            return value
        else:
            return None
