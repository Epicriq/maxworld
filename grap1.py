import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_game(player_x, player_y):
    clear_screen()
    for y in range(5):
        for x in range(10):
            if x == player_x and y == player_y:
                print("@", end="")
            else:
                print(".", end="")
        print()

# Игровой цикл
player_x, player_y = 0, 0
while True:
    draw_game(player_x, player_y)
    move = input("Куда идти? (wasd): ").lower()
    if move == "d" and player_x < 9:
        player_x += 1
    elif move == "a" and player_x > 0:
        player_x -= 1
    elif move == "s" and player_y < 4:
        player_y += 1
    elif move == "w" and player_y > 0:
        player_y -= 1
    elif move == "q":
        break