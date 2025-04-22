from system.man import BaseManager
import random

class MapManager(BaseManager):
    def __init__(self, game):
        super().__init__()
        self.game = game
        
        # Генерация карты
        self.dungeon = self.generate_dungeon(50, 25)
        # Установка точки выхода
        self.dungeon, self.player_pos = self.place_entities(self.dungeon)

    def view_map(self):
        """Отображение карты"""
        for row in self.dungeon:
            print(''.join(row))
    
    def view_position(self):
        print(f"Ваша позиция: {self.player_pos}")


    def place_entities(self, game_map):
        """Размещение игрока и выхода на карте"""
        height = len(game_map)
        width = len(game_map[0]) if height > 0 else 0
        
        # Находим все проходимые клетки
        walkable = []
        for y in range(height):
            for x in range(width):
                if game_map[y][x] == '.':
                    walkable.append((x, y))
        
        if len(walkable) < 2:
            return game_map  # Недостаточно места
        
        # Размещаем игрока и выход
        player_pos = random.choice(walkable)
        walkable.remove(player_pos)
        exit_pos = random.choice(walkable)
        
        # Обновляем карту
        game_map[player_pos[1]][player_pos[0]] = '@'
        game_map[exit_pos[1]][exit_pos[0]] = 'E'
        
        return game_map, player_pos
    
    def chage_entities(self, player_pos_new):
        tail = self.dungeon[player_pos_new[1]][player_pos_new[0]]
        if (tail == '.'):
            # Обновляем карту        
            self.dungeon[self.player_pos[1]][self.player_pos[0]] = '.'
            self.dungeon[player_pos_new[1]][player_pos_new[0]] = '@'
            self.player_pos = player_pos_new
            return True
        elif (tail == 'E'):
            print("Вы нашли выход!")
            return True
        else:
            print("Туда не пройти!")
            return False
    def generate_dungeon(self, width, height, max_rooms=10, min_room_size=3, max_room_size=8):
        """Генерация подземелья с комнатами и коридорами"""
        # Создаем полностью заполненную карту
        dungeon = [['#' for _ in range(width)] for _ in range(height)]
        rooms = []
        
        for _ in range(max_rooms):
            # Случайные размеры комнаты
            room_width = random.randint(min_room_size, max_room_size)
            room_height = random.randint(min_room_size, max_room_size)
            
            # Случайная позиция комнаты
            x = random.randint(1, width - room_width - 1)
            y = random.randint(1, height - room_height - 1)
            
            new_room = {'x': x, 'y': y, 'w': room_width, 'h': room_height}
            
            # Проверяем пересечение с другими комнатами
            intersects = False
            for room in rooms:
                if (x < room['x'] + room['w'] and x + room_width > room['x'] and
                    y < room['y'] + room['h'] and y + room_height > room['y']):
                    intersects = True
                    break
            
            if not intersects:
                # Добавляем комнату
                rooms.append(new_room)
                # "Выкапываем" комнату
                for i in range(y, y + room_height):
                    for j in range(x, x + room_width):
                        dungeon[i][j] = '.'
                
                # Соединяем с предыдущей комнатой коридором
                if len(rooms) > 1:
                    prev_room = rooms[-2]
                    # Центры комнат
                    new_x, new_y = x + room_width // 2, y + room_height // 2
                    prev_x, prev_y = (prev_room['x'] + prev_room['w'] // 2, 
                                      prev_room['y'] + prev_room['h'] // 2)
                    
                    # Горизонтальный коридор
                    for j in range(min(new_x, prev_x), max(new_x, prev_x) + 1):
                        dungeon[new_y][j] = '.'
                    # Вертикальный коридор
                    for i in range(min(new_y, prev_y), max(new_y, prev_y) + 1):
                        dungeon[i][prev_x] = '.'
        
        return dungeon