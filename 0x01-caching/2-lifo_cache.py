#!/usr/bin/env python3
"""
LIFO caching Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching class """
    def __init__(self):
        """ instantiating the class """
        super().__init__()
        self.keyStack = []
    
    def put(self, key, item):
        """ insert an item to the cache """
        if key and item:
            if len(self.cache_data) < self.MAX_ITEMS:
                self.cache_data[key] = item
                self.keyStack.append(key)
            else:
                removed = self.keyStack.pop()
                self.cache_data.pop(removed)
                self.cache_data[key] = item
                self.keyStack.append(key)
                print("DISCARD: {}".format(removed))
        else:
            pass
    
    def get(self, key):
        """ returns a given Item with it's key """
        # if key and key in self.cache_data:
        #     return self.cache_data
        # else:
        #     return None
        return self.cache_data[key] if key and key in self.cache_data else None
