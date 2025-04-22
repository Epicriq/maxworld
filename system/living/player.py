import os
import json
from abc import ABC, abstractmethod, abstractproperty
from system.living import characters
from system.living.parts import *
from config import *
from system.ctx import Context

log = Context.init_logger(__name__)

class Player(characters.Characters):
    def __init__(self, name):
        _path = os.path.join(PATHS["dir_players"], name)
        self._name = name
        self._info = self.on_load(info.Info(), os.path.join(_path, "info.json"))
        self._state = self.on_load(state.State(), os.path.join(_path, "state.json"))
        self._characteristics = self.on_load(characteristics.Characteristics(), os.path.join(_path, "characteristics.json"))
        self._abilities = self.on_load(abilities.Abilities(), os.path.join(_path, "abilities.json"))
        self._skills = self.on_load(skills.Skills(), os.path.join(_path, "skills.json"))
        self._spells = self.on_load(spells.Spells(), os.path.join(_path, "spells.json"))
        self._inventory = self.on_load(inventory.Inventory(), os.path.join(_path, "inventory.json"))
        
    def on_load(self, o, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                o.__dict__ = json.load(f)
            return o
        except json.JSONDecodeError as e:
            mes = f"Ошибка декодирования файла {filename}: {e}"
            log.error(mes)
        except Exception as e:
            log.error(e)
            if logging.getLevelName(LOG["level"]) == "DEBUG":
                print(e)
    

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
        