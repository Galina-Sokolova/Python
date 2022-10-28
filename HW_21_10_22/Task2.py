import random
import os

def clear_screen():
    os.system('cls')

def choose_game_option():
    while True:
        try:
            game_option = int(input("Введите 1, если хотите игроть с ботом и 2 - если с человеком: "))
            if game_option == 1 or game_option == 2:
                break
            else:
                 print("Вы ввели другое число")
        except ValueError:
            print("Неправильно ввели! Попробуйте ещё раз!")
    return game_option        

def who_is_first():
    first = random.randint(1, 2)
    if first == 1:
        print('Первым ходит игрок 1')
    else:
        print('Первым ходит игрок 2')
    return first 

def man_move(total, limit, player):
    if player == 1:
        while True:
            try:
                num = int(input(f'Возьмите не более {limit} конфет. \n Игрок 1: '))
                if 0<num<limit+1:
                    break
                else:
                    print("Вы ввели неверное число")
            except ValueError:
                print("Неправильно ввели! Попробуйте ещё раз!")
    else:
        while True:
            try:
                num = int(input(f'Возьмите не более {limit} конфет. \n \t\t\t Второй игрок: '))
                if 0<num<limit+1:
                    break
                else:
                    print("Вы ввели неверное число")
            except ValueError:
                print("Неправильно ввели! Попробуйте ещё раз!")
    total-=num
    clear_screen()
    print(f'осталось {total} конфет')
    return total

total = 117
limit = 28    
game_option = choose_game_option()
if game_option == 2:
    player = who_is_first()
    while total >= limit:
        total = man_move(total, limit, player)
        if player == 1:
            player = 2
        else:
            player = 1
if player == 1:
    print("Выйграл первый игрок")
else:
    print("Выйграл второй игрок") 

if game_option == 1:                       



