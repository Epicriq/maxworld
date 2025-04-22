import os
import platform
import json
from typing import Any
from system.living.player import Player
from config import PATHS
from system.ctx import Context
from system.man import BaseManager
from system.magic.spellsbook import SpellsBook

log = Context.init_logger(__name__)

class SysManager(BaseManager):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.spellsbook = SpellsBook()  
        self.players = self.init_players()
        self.player = self.players["Тестовый игрок"]        
        
    def init_players(self):
        players = {}
        player_dirs = sorted(os.listdir(PATHS["dir_players"]))
        for n, name in enumerate(player_dirs):
            players[name] = Player(name)
        return players