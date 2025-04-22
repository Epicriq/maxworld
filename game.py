from system.ctx import clear_console, print_logo
from system.sys import SysManager
from system.map import MapManager
from system.cmd import CommandManager
from system.mod import ModManager

class Game:
    def __init__(self):    
        clear_console()
        print_logo()
        # Модули...
        self.sys = SysManager(self)
        self.cmd = CommandManager(self)
        self.map = MapManager(self)
        self.mod = ModManager(self)
        
    def run(self):
        # Загрузка команд
        self.cmd.load_commands()
        
        # Загрузка модов
        self.mod.load_mods()
        
        # Работа с картой
        #self.map.view_map()
        #self.map.view_position()
        
        # Управление
        self.cmd.input()
        
game = Game()
game.run()