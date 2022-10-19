#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
num = int(input('Введите целое число: '))
decimal_num=num
i=1
binary_num=0
while num != 0:
    rem = num%2
    num = num//2
    binary_num+=rem*i
    i*=10
print(decimal_num,'->',binary_num)