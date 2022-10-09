# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти 
# (x и y).
quarterNumber = int(input('Введите номер четверти: '))
while quarterNumber<0 or quarterNumber>4: 
    print ('Четверти с таким номером не существует')
    quarterNumber = int(input('Введите номер четверти: '))

if quarterNumber == 1:
    print (f'В {quarterNumber} четверти x>0 и y>0')
if quarterNumber == 2:
    print (f'В {quarterNumber} четверти x<0 и y>0')
if quarterNumber == 3:
    print (f'В {quarterNumber} четверти x<0 и y<0')
if quarterNumber == 4:
    print (f'В {quarterNumber} четверти x>0 и y<0')