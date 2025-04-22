from config import PATHS
from system.man import BaseManager
import importlib.util
import os
from rich.console import Console
from rich.table import Table
from rich import print

from abc import ABC, abstractmethod

table = Table(title="Моды")
table.add_column("Имя", style="cyan")
table.add_column("Версия", style="magenta")
table.add_column("Автор", style="green")
table.add_column("Описание", style="white")

class BaseMod(ABC):
    @abstractmethod
    def on_load(self, game):
        pass
    @abstractmethod
    def on_unload(self, game):
        pass
    @abstractmethod    
    def show_mod_info(self, *args):
        pass

class ModManager(BaseManager):
    def __init__(self, game, mods_dir=PATHS["dir_mods"]):
        super().__init__()
        self.game = game
        self.mods_dir = mods_dir
        self.active_mods = {}
        
    def load_mods(self):
        print("\n[yellow]Загрузка модов...[/yellow]")
        if not os.path.exists(self.mods_dir):
            os.makedirs(self.mods_dir)
            return
            
        for mod_file in os.listdir(self.mods_dir):
            if mod_file.endswith('.py'):
                mod_name = mod_file[:-3]
                self.load_mod(mod_name)
        # Выводим таблицу с загруженными модами
        console = Console()
        console.print(table)    
        
    def load_mod(self, mod_name):
        try:
            file_path = os.path.join(self.mods_dir, f"{mod_name}.py")
            
            spec = importlib.util.spec_from_file_location(mod_name, file_path)
            mod_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod_module)
            if hasattr(mod_module, 'Mod'):
                mod_class = mod_module.Mod
                if issubclass(mod_class, BaseMod):
                    mod_instance = mod_class()
                    mod_instance.on_load(self.game)
                    self.active_mods[mod_name] = mod_instance
                    #print(f"  Мод \"{mod_name}\" успешно загружен и инициализирован")
                    table.add_row(*prepare_row(mod_instance.mod_info.values()))
                    return True
                else:
                    print(f"  Мод \"{mod_name}\" не наследует BaseMod")
            else:
                print(f"  Мод \"{mod_name}\" не содержит класс Mod")
                
        except Exception as e:
            print(f"  Ошибка загрузки мода \"{mod_name}\": {str(e)}")
        
        return False
    
    def unload_mod(self, mod_name):
        if mod_name in self.active_mods:
            self.active_mods[mod_name].on_unload(self.game)
            del self.active_mods[mod_name]
            print(f"  Мод {mod_name} выгружен")
            return True
        return False
    
    def get_mod(self, mod_name):
        return self.active_mods.get(mod_name)
        
def prepare_row(items):
    return [", ".join(item) if isinstance(item, list) else str(item) for item in items]        