from system.cmd import BaseCmd
from rich.console import Console
from rich.table import Table
from rich import print
from system.living.parts import item

class Cmd(BaseCmd):

    cmd_info = {
        'name': 'Инвентарь',
        'description': 'Отображает игроку его инвентарь'
    }

    def on_load(self, game):
        self.game = game
        # Добавляем новую команду в игру
        game.cmd.add_command("инвентарь", self.func)

    def on_unload(self, game):
        pass

    def show_cmd_info(self, *args):
        return (f"\tКоманда: {self.mod_info['name']}\n"
                f"\tОписание: {self.mod_info['description']}")
    
    def func(self, *args):
        inventory = args[0].sys.player.inventory.__dict__
        """
        for key in inventory.__dict__:
            print(key)
        """
        table = Table(title="==== Инвентарь ====")
        for key in inventory:
            table.add_row(key, f"{inventory[key]["durability"]}")
        console = Console()
        console.print(table)
        """
        """