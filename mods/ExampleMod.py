from system.mod import BaseMod

class Mod(BaseMod):

    # В модуле мода
    mod_info = {
        'name': 'Example Mod',
        'version': '1.0',
        'author': 'ASuslov',
        'description': 'Демонстрация возможностей добавления новых команд в игру'
    }

    def on_load(self, game):       
        # Добавляем новую команду в игру
        game.cmd.add_command("example", self.example_command)
        
    def on_unload(self, game):
        game.example_mod_loaded = False
        game.remove_command("example")
                
    """Показывает информацию о моде."""
    def show_mod_info(self, *args) -> str:
        return (f"\tМод: {self.mod_info['name']}\n"
                f"\tВерсия: {self.mod_info['version']}\n"
                f"\tАвтор: {self.mod_info['author']}\n"
                f"\tОписание: {self.mod_info['description']}")
                
    def example_command(self, *args):
        print("КОМАНДА ВЫПОЛНЕНА !")
        return 0
