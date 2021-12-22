#!/usr/bin/env python3
"""
FIFO Cache Module
"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    A FIFO class
    """

    def __init__(self):
        """ instantiate class """
        super().__init__()
        self.keys = deque()

    def put(self, key, item):
        """ add item """
        if key and item:
            if len(self.cache_data) < self.MAX_ITEMS:
                self.cache_data[key] = item
                self.keys.append(key)
            else:
                removed = self.keys.popleft()
                self.cache_data.pop(removed)
                self.cache_data[key] = item
                self.keys.append(key)
                # print(self.keys)
                # print(self.cache_data)
                print("DISCARD: {}".format(removed))
        else:
            pass

    def get(self, key):
        """ get an item with the given key """
        if key and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
