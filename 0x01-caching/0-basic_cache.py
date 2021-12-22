#!/usr/bin/env python3
"""
Basic Cache module
with put and get method
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ A baseic cache class
    with a get and put method """

    def __init__(self):
        """ instantiating from the base class """
        super().__init__()

    def put(self, key, item):
        """ puts an item to the caching dictionary """
        if key and item:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        """ get an item with the key """
        if key and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
