import random
from dataclasses import dataclass
from typing import List, Dict

def madlibs_room():
    templates = [
        "Вы в {adj} {room}. На {wall} вы видите {object}. {atmosphere}",
        "{Room} {adj} как {comparison}. {Object} {position}."
    ]
    
    params = {
        'adj': ['мрачной', 'загадочной', 'заброшенной'],
        'room': ['пещере', 'комнате', 'зале'],
        'Room': ['Пещера', 'Комната', 'Зал'],  # Уже с заглавной буквы
        'wall': ['северной стене', 'полу', 'потолке'],
        'object': ['странные символы', 'разбитый сундук', 'окровавленный топор'],
        'Object': ['Странные символы', 'Разбитый сундук', 'Окровавленный топор'],
        'atmosphere': ['Воздух пахнет серой.', 'Где-то капает вода.'],
        'comparison': ['нора дракона', 'чертог короля'],
        'position': ['стоит в углу', 'лежит на боку']
    }
    
    def get_param(key):
        """Безопасное получение параметра с обработкой отсутствующих ключей"""
        return random.choice(params.get(key, ['']))
        
    template = random.choice(templates)
    try:
        # Заменяем плейсхолдеры с учетом их наличия в шаблоне
        result = template.format(
            adj=get_param('adj'),
            room=get_param('room'),
            Room=get_param('Room'),
            wall=get_param('wall'),
            object=get_param('object'),
            Object=get_param('Object'),
            atmosphere=get_param('atmosphere'),
            comparison=get_param('comparison'),
            position=get_param('position')
        )
        return result
    except KeyError as e:
        print(f"Ошибка: отсутствует ключ {e} в шаблоне")
        return "Таинственная комната."  # Запасной вариант
  