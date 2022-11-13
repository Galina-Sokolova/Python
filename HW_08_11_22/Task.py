# 1. Задайте последовательность цифр. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

# subseq='1113384455229'
# lst=list(subseq)
# lst1 = list(map(int, lst))
# lst2 = [lst1[i] for i in range(len(lst1)) if lst1.count(lst1[i]) == 1]
# print(lst2)

##################################################################################


# 2. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# text = 'абв Ура, питон крутой абвязык, очень интересные скминарабвы'
# lst = ' '.join(list(filter(lambda s: 'абв' not in s, text.split())))
# print(lst)

###################################################################################

# 3. Напишите программу, которая принимает на вход вещественное 
#  число и показывает сумму его цифр.

# num = input("Ведите число: ")
# num = num.replace('.', '')
# num = num.replace(',', '')
# num = num.replace('-', '')
# sum = sum([int(i) for i in num])
# print(sum)


########################################################################################

# 4. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# from math import prod

# my_list = input('Введите числа через пробел: ')
# my_list = list(map(int, my_list.split(' ')))
# n = int(len(my_list)/2)
# print(n)
# first_half_list = my_list[0:n+1]
# second_half_list = list(reversed(my_list[n:]))
# temp_list = list(zip(first_half_list, second_half_list))
# result_list = list(map(prod, temp_list))
# print(f'Исодный список: {my_list}, произведение пар чисел: {result_list}')