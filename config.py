import logging
PATHS = {
    # Расположение модов
    "dir_mods": "mods",
    # Расположение команд
    "dir_commands": "system\\commands",
    # База данных
    "file_database": "data\\game.db",
    # Расположение данных игрока
    "dir_players": "data\\player\\", 
    # Расположение данных монстров
    "dir_monsters": "data\\monster\\", 
    # Справочник заклинаний
	"file_spellsbook": "data\\spellsbook.json"
}
# Настройки логирования
LOG = {
    "filename": "app.log",
    "level": logging.DEBUG,
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "datefmt": "%Y-%m-%d %H:%M:%S"
}