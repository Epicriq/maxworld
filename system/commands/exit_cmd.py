from system.cmd import BaseCmd

class Cmd(BaseCmd):

    cmd_info = {
        'name': 'Выход',
        'description': 'Завершает игру'
    }

    def on_load(self, game):
        self.game = game
        # Добавляем новую команду в игру
        game.cmd.add_command("выход", self.func)

    def on_unload(self, game):
        pass

    def show_cmd_info(self, *args):
        return (f"\tКоманда: {self.mod_info['name']}\n"
                f"\tОписание: {self.mod_info['description']}")
    
    def func(self, *args):
        exit()