# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
stek = [12, -5, 65, 3, -8, 77, 7]
sum = 0
for i in range(len(stek)-1):
    if i%2 != 0:
        sum+=stek[i]
        print(' stek[',i,'] +', end='')
print('=',sum)        