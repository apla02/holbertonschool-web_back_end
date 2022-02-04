#!/usr/bin/env python3
""" Implement a caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """inherit from BaseCaching and is a caching system
    Args:
        BaseCaching (Father class): Implement methods
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary an item key-value pair
        Args:
            key ([type] Any): [key of the dict]
            item ([type] Any): [value of the dict]
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """Obtain a value from dict by key
        Args:
            key ([type] Any): [key of the dict]
        Returns:
            [type] Any: value from dict
        """
        if key is not None:
            value = self.cache_data.get(key)
            if value is None:
                return None
            return value
        else:
            return None
