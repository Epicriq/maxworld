from config import PATHS
import json

class SpellsBook(dict):
    def __init__(self):
        self.load_dict(PATHS["file_spellsbook"])
        
    def get_spell(self, name):
        s = self.__dict__[name]
        return self.Spell(name, s['grade'], s['mana'], s['power'], s['description'])

    def __str__(self):
        return f"{self.__dict__}"
    
    def load_dict(self, file):
        try:
            with open(file, 'r', encoding='utf-8') as f:
                obj = json.load(f)
                self.__dict__ = obj
        except json.JSONDecodeError as e:
            print(f"Ошибка декодирования файла {file}: {e}")

    class Spell(dict):
        def __init__(self, name, grade, mana, power, description):
            self.name = name
            self.grade = grade
            self.mana = mana
            self.power = power
            self.description = description
        def to_dict(self):
            return {
                'name': self.name,
                'grade': self.grade,
                'mana': self.mana,
                'power': self.power,
                'description': self.description
            }