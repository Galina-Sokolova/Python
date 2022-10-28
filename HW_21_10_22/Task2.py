# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два 
# игрока делая ход друг после друга. Первый ход определяется 
# жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход. 
#  Сколько конфет нужно взять первому игроку, чтобы забрать все 
#  конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import random
import os

def clear_screen():
    os.system('cls')

def choose_game_option():
    while True:
        try:
            game_option = int(input("Введите 1, если хотите игрaть с ботом и 2 - если с человеком: "))
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

def who_is_first_bot():
    first = random.randint(0, 1)
    if first == 0:
        print('Первым ходит Bot')
    else:
        print('Первым ходит игрок 1')
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
    elif player == 2:
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

def bot_move(total, limit):
    rem = total%limit
    if rem == 0 or rem == 1:
        num = limit
    else:    
        num = total%limit-1
    print(f'\t\t\tBot взял конфет: {num}')
    total-=num
    #clear_screen()
    print(f'осталось {total} конфет')
    return total    

total = 134
limit = 28    
game_option = choose_game_option()
if game_option == 2:
    print(f'изначально {total} конфет')
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

else: #game_option == 1: 
    print(f'иначально {total} конфет')                      
    player = who_is_first_bot()
    while total >= limit:
        if player == 0:
            total = bot_move(total, limit)
            player = 1
        else:    
            total = man_move(total, limit, player)
            player = 0
        #clear_screen()    
    if player == 1:
        print('Выйграл Игрок 1')
    else:
        print('Выйграл Bot')                    



