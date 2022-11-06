# Создайте программу для игры в ""Крестики-нолики"".

from tkinter import *
import random
root = Tk()
root.title('крестики-нолики')
game_run = True
board = []
count_cross = 0

def new_game():
    for row in range(3):
        for col in range(3):
            board[row][col]['text'] = ' '
            board[row][col]['background'] = 'peach puff'
    global game_run
    game_run = True
    global count_cross
    count_cross = 0

def press(row, col):
    if game_run and board[row][col]['text'] == ' ':
        board[row][col]['text'] = 'X'
        global count_cross
        count_cross += 1
        check_is_win('X')
        if game_run and count_cross < 5:
            computer_move()
            check_is_win('O')

def check_is_win(symbol):
    for n in range(3):
        check_is_line(board[n][0], board[n][1], board[n][2], symbol)
        check_is_line(board[0][n], board[1][n], board[2][n], symbol)
    check_is_line(board[2][0], board[1][1], board[0][2], symbol)
    check_is_line(board[0][0], board[1][1], board[2][2], symbol)

def check_is_line(i1, i2, i3, symbol):
    if i1['text'] == symbol and i2['text'] == symbol and i3['text'] == symbol:
        i1['background'] = i2['background'] = i3['background'] = 'OliveDrab1'
        if symbol == 'X':
            print('Вы победили!!!')
        elif symbol == 'O':
            print('Попробуйте ещё раз')  
        global game_run
        game_run = False


def can_win(i1, i2, i3, symbol):
    res = False
    if i1['text'] == symbol and i2['text'] == symbol and i3['text'] == ' ':
       i3['text'] = 'O'
       res = True
    if i1['text'] == symbol and i2['text'] == ' ' and i3['text'] == symbol:
       i2['text'] = 'O'
       res = True
    if i1['text'] == ' ' and i2['text'] == symbol and i3['text'] == symbol:
       i1['text'] = 'O'
       res = True
    return res

def computer_move():
    for n in range(3):
        if can_win(board[n][0], board[n][1], board[n][2], 'O'):
            return 
        if can_win(board[0][n], board[1][n], board[2][n], 'O'):
            return
    if can_win(board[2][0], board[1][1], board[0][2], 'O'):
            return
    if can_win(board[0][0], board[1][1], board[2][2], 'O'):
            return
    for n in range(3):
        if can_win(board[n][0], board[n][1], board[n][2], 'X'):
            return 
        if can_win(board[0][n], board[1][n], board[2][n], 'X'):
            return
    if can_win(board[2][0], board[1][1], board[0][2], 'X'):
            return
    if can_win(board[0][0], board[1][1], board[2][2], 'X'):
            return
               
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
             
        if board[row][col]['text'] == ' ':
            board[row][col]['text'] = 'O'
            break

for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text = ' ', width = 4, height = 2,
                        font=('Verdana', 20, 'bold'),
                        background='peach puff',
                        command=lambda row = row, col = col: press(row, col))
        button.grid(row = row, column = col, sticky = 'nsew')
        line.append(button)
    board.append(line)
new_button = Button(root, text = 'new game', command = new_game)
new_button.grid(row = 3, column = 0, columnspan = 3, sticky = 'nsew')
root.mainloop()        
         
        


