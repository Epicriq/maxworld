import uuid

class Item(dict):
    def __init__(self):
        self._storage = {}
    def __getattr__(self, key):
        if key.startswith('_'):
            return super().__getattribute__(key)
        return self._storage.get(key)
    def __setattr__(self, key, value):
        if key.startswith('_'):
            super().__setattr__(key, value)
        else:
            self._storage[key] = value
    def __str__(self):
        return f"{self.__dict__}"