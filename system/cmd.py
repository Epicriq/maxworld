from system.man import BaseManager
from system.gen import *
from system.living.npc import get_ai_response
#from system.commands.инвентарь import инвентарь
import sys
import msvcrt
import os
import importlib.util
from config import PATHS
#from rich.console import Console
#from rich.table import Table
#from rich import print
#from system.commands import base_cmd
from abc import ABC, abstractmethod

#table = Table(title="Команды")
#table.add_column("Имя", style="cyan")
#table.add_column("Описание", style="white")


class BaseCmd(ABC):
    @abstractmethod
    def on_load(self, game):
        pass
    @abstractmethod
    def on_unload(self, game):
        pass
    @abstractmethod    
    def show_cmd_info(self, *args):
        pass
    @abstractmethod    
    def func(self, *args):
        pass
    
class CommandManager(BaseManager):
    def __init__(self, game):        
        super().__init__()
        self.game = game
        self.cmds_dir = PATHS["dir_commands"]        
        self.commands = {}
        self.active_cmds = {}

    def load_commands(self):
        #print("\n[yellow]Загрузка команд...[/yellow]")
        for cmd_file in os.listdir(self.cmds_dir):
            if cmd_file.endswith('.py') and not (cmd_file.startswith('__')):
                cmd_name = cmd_file[:-3]
                self.load_command(cmd_name)    
        # Выводим таблицу с загруженными командами
#        console = Console()
#        console.print(table)    

    def add_command(self, name, func):
        self.commands[name] = func
        
    def remove_command(self, name):
        if name in self.commands:
            del self.commands[name]

    def load_command(self, cmd_name):
        try:
            file_path = os.path.join(self.cmds_dir, f"{cmd_name}.py")

            spec = importlib.util.spec_from_file_location(cmd_name, file_path)
            cmd_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(cmd_module)
            if hasattr(cmd_module, 'Cmd'):
                cmd_class = cmd_module.Cmd
                if issubclass(cmd_class, BaseCmd):
                    cmd_instance = cmd_class()
                    cmd_instance.on_load(self.game)
                    self.active_cmds[cmd_name] = cmd_instance
                    _name = cmd_instance.cmd_info["name"]
                    #print(f"  Команда \"{_name}\" успешно загружена и инициализирована")
                    #table.add_row(*prepare_row(cmd_instance.cmd_info.values()))                    
                    return True
                else:
                    print(f"  Команда \"{cmd_name}\" не наследует BaseCmd")
            else:
                print(f"  Команда \"{cmd_name}\" не содержит класс Cmd")
                
        except Exception as e:
            print(f"  {__name__} Ошибка загрузки команды \"{cmd_name}\": {str(e)}")
        
        return False
        
    def unload_mod(self, cmd_name):
        if cmd_name in self.active_mods:
            self.active_mods[cmd_name].on_unload(self.game)
            del self.active_cmds[cmd_name]
            print(f"  Команда {cmd_name} выгружена")
            return True
        return False        

    def input(self):        
        while True:
            #dungeon_room = generate_dungeon_room()
            #print(dungeon_room.description)
            print(madlibs_room())
            #print(get_ai_response("deepseek", "Привет! Хочешь со мной поговорить?"))
            print("Доступные команды:", ", ".join(self.commands))
            print("Нажмите Tab для автодополнения")
            
            user_input = input_with_autocomplete("> ", self.commands).strip()
            
            if not user_input:
                continue
            
            if user_input.lower() == "выход":
                break
            
            sorted_dict = dict(sorted(self.commands.items()))
            if user_input not in self.commands and not any(cmd.startswith(user_input) for cmd in sorted_dict):
                print("Неизвестная команда. Доступные команды:", ", ".join(self.commands))
                continue
            else:
                for cmd in (sorted_dict):
                    if (cmd.startswith(user_input)):
                        print(cmd)
                        print(f"Выполняю команду: {cmd}")
                        # Вызов функции команды
                        self.commands[f"{cmd}"](self.game)
                        break
        print("Игра завершена")

class Autocomplete:
    def __init__(self, commands):
        self.commands = commands
        self.current_matches = []
        self.current_input = ""
        self.match_index = 0
    
    def get_matches(self, text):
        return [cmd for cmd in self.commands if cmd.startswith(text)]
    
    def show_matches(self):
        if self.current_matches:
            print("\nВозможные варианты:")
            for i, match in enumerate(self.current_matches):
                prefix = ">" if i == self.match_index else " "
                print(f"{prefix} {match}")
    
    def handle_tab(self):
        if not self.current_input:
            self.current_matches = self.commands.copy()
            self.show_matches()
            return
        
        self.current_matches = self.get_matches(self.current_input)
        
        if not self.current_matches:
            return
        
        if len(self.current_matches) == 1:
            self.current_input = self.current_matches[0]
            print("\r> " + self.current_input + " " * 1, end="")
        else:
            self.match_index = (self.match_index + 1) % len(self.current_matches)
            print("\r> " + self.current_matches[self.match_index] + " " * 1, end="")

def input_with_autocomplete(prompt, commands):
    completer = Autocomplete(commands)
    print(prompt, end="", flush=True)
    
    while True:
        char = msvcrt.getwch()
        
        if char == '\t':  # Tab
            completer.handle_tab()
        elif char == '\r':  # Enter
            print()
            return completer.current_input
        elif char == '\x08':  # Backspace
            if completer.current_input:
                completer.current_input = completer.current_input[:-1]
                completer.current_matches = []
                completer.match_index = 0
                print("\r" + prompt + completer.current_input + " " * 1 + "\r" + prompt + completer.current_input, end="", flush=True)
        elif char.isprintable():
            completer.current_input += char
            completer.current_matches = completer.get_matches(completer.current_input)
            completer.match_index = 0
            print(char, end="", flush=True)    
            
def prepare_row(items):
    return [", ".join(item) if isinstance(item, list) else str(item) for item in items]