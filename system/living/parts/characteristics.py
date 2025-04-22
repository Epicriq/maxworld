class Characteristics:
    def __init__(self):
        self._storage = {
          "strength": 0,
          "endurance": 0,
          "dexterity": 0,
          "perception": 0,
          "intelligence": 0,
          "wisdom": 0
        }
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