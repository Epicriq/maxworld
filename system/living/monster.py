from system.living.monsters import *
from system.living.parts.info import Info
from system.living.parts.state import State
from system.living.parts.characteristics import Characteristics
from system.living.parts.abilities import Abilities
from system.living.parts.skills import Skills
from system.living.parts.spells import Spells
from system.living.parts.inventory import Inventory
from system.ctx import Context
import os
from config import PATHS
import json

log = Context.init_logger(__name__)

class Monster(Monsters):
    def __init__(self, name):
        _path = os.path.join(PATHS["dir_monsters"], name)
        self._name = name
        _file = os.path.join(_path, "info.json")
        self._info = Info() if not os.path.exists(_file) else self.on_load(Info(), _file)
        _file = os.path.join(_path, "state.json")        
        self._state = State() if not os.path.exists(_file) else self.on_load(State(), _file)
        _file = os.path.join(_path, "characteristics.json")        
        self._characteristics = Characteristics() if not os.path.exists(_file) else self.on_load(Characteristics(), _file)
        _file = os.path.join(_path, "Abilities.json")        
        self._abilities = Abilities() if not os.path.exists(_file) else self.on_load(Abilities(), _file)
        _file = os.path.join(_path, "Skills.json")        
        self._skills = Skills() if not os.path.exists(_file) else self.on_load(Skills(), _file)
        _file = os.path.join(_path, "Spells.json")        
        self._spells = Spells() if not os.path.exists(_file) else self.on_load(Spells(), _file)
        _file = os.path.join(_path, "Inventory.json")
        self._inventory = Inventory() if not os.path.exists(_file) else self.on_load(Inventory(), _file)
    def on_load(self, o, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                o._storage = json.load(f)
            return o
        except json.JSONDecodeError as e:
            mes = f"Ошибка декодирования файла {filename}: {e}"
            log.error(mes)
        except Exception as e:
            log.error(e)

    def save(self):
        self.on_save(self.info, "info.json")
        self.on_save(self.state, "state.json")
        self.on_save(self.characteristics, "characteristics.json")
        self.on_save(self.abilities, "abilities.json")
        self.on_save(self.skills, "skills.json")
        self.on_save(self.spells, "spells.json")
        self.on_save(self.inventory, "inventory.json")
    
    def on_save(self, o, filename):
        try:
            _path = os.path.join(PATHS["dir_monsters"], self.name)
            if not os.path.exists(_path):
                os.makedirs(_path)
            with open(os.path.join(_path, filename), 'w', encoding='utf-8') as f:
                json.dump(o._storage, f, indent=2, ensure_ascii=False)
        except json.JSONDecodeError as e:
            mes = f"Ошибка декодирования файла {filename}: {e}"
            log.error(mes)
        except Exception as e:
            print(e)
            log.error(e)
        

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if self._name != new_name:
            self._name = new_name  

    @property       
    def info(self):
        return self._info
    @info.setter
    def info(self, new_info):
        if self._info != new_info:
            self._info = new_info
            
    @property       
    def state(self):
        return self._state
    @state.setter
    def state(self, new_state):
        if self._state != new_state:
            self._state = new_state
            
    @property       
    def characteristics(self):
        return self._characteristics
    @characteristics.setter
    def characteristics(self, new_characteristics):
        if self._characteristics != new_characteristics:
            self._characteristics = new_characteristics
            
    @property       
    def abilities(self):
        return self._abilities
    @abilities.setter
    def abilities(self, new_abilities):
        if self._abilities != new_abilities:
            self._abilities = new_abilities
            
    @property       
    def skills(self):
        return self._skills
    @skills.setter
    def skills(self, new_skills):
        if self._skills != new_skills:
            self._skills = new_skills
            
    @property       
    def spells(self):
        return self._spells
    @spells.setter
    def spells(self, new_spells):
        if self._spells != new_spells:
            self._spells = new_spells
            
    @property       
    def inventory(self):
        return self._inventory
    @inventory.setter
    def inventory(self, new_inventory):
        if self._inventory != new_inventory:
            self._inventory = new_inventory        