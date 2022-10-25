# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
# Записываем результат в файл.

def polynomial_notation(K):
    coefficient=[random.randint(-100, 100)]
    for i in range(1, K+1):
        coefficient.append(random.randint(-100, 100))
    print(coefficient)  
    polindrom = ''
    for i in range(K, 0, -1):
        if coefficient[i] == 1:
            polindrom+='+x^'+str(i)
        elif coefficient[i] == -1:  
            polindrom+='-x^'+str(i) 
        elif coefficient[i] == 0:
            polindrom+=''
        else:
            polindrom+='+'+str(coefficient[i])+'x^'+str(i)   
    if coefficient[0] != 0:        
        polindrom+='+'+str(coefficient[0])  
    polindrom = polindrom.replace("^1+", "+").replace("+-", "-")+'=0'  
    if polindrom[0] == '+':
        polindrom = polindrom[1:]
    return polindrom

import random
k = int(input('Введите натуральное число '))
# coefficient=[random.randint(-100, 100)]
# for i in range(1, k+1):
#     coefficient.append(random.randint(-100, 100))
# print(coefficient)  

polyndrom = polynomial_notation(k)
polynom=open('polynom.txt', 'w')
polynom.writelines(polyndrom)
polynom.close()
