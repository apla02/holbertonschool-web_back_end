#!/usr/bin/env python3
""" Implement a caching system
    cache replacement algorithm - LIFO
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """inherit from BaseCaching and is a caching system
    Args:
        BaseCaching (Father class): Implement methods
    """
    def __init__(self):
        """Init method from father
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data.update({key: item})
        len_cache = len(self.cache_data)
        if len_cache > BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data)[-2]
            print(f"DISCARD: {last_key}")
            self.cache_data.pop(last_key)

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
