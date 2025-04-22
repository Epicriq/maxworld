from system.cmd import BaseCmd

class Cmd(BaseCmd):

    cmd_info = {
        'name': 'Запад',
        'description': 'Перемещает игрока на запад'
    }

    def on_load(self, game):
        self.game = game
        # Добавляем новую команду в игру
        game.cmd.add_command("запад", self.func)

    def on_unload(self, game):
        pass

    def show_cmd_info(self, *args):
        return (f"\tКоманда: {self.mod_info['name']}\n"
                f"\tОписание: {self.mod_info['description']}")
    
    def func(self, *args):
        map = self.game.map
        pos = map.player_pos
        xy = (pos[0] - 1, pos[1])
        map.chage_entities(xy)
        map.view_map()
        
        