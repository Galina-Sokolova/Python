# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0

import random

def polynomial_notation(K):
    coefficient=[random.randint(-10, 10)]
    for i in range(1, k1+1):
        coefficient.append(random.randint(-10, 10))
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


k1 = int(input('Введите натуральное число '))
polyndrom1 = polynomial_notation(k1)
print(polyndrom1)
polynom1=open('pol1.txt', 'w')
polynom1.writelines(polyndrom1)
polynom1.close()

k2 = int(input('Введите натуральное число '))
polyndrom2 = polynomial_notation(k2)
print(polyndrom2)
polynom2=open('pol2.txt', 'w')
polynom2.writelines(polyndrom2)
polynom2.close()

f1 = open('pol1.txt', 'r')
pol1_lst=f1.readline()
pol1_lst2=pol1_lst.replace(" ", "").replace("-", "+-")[:-2].split("+")
print(pol1_lst)
print(pol1_lst2)
exit()
coef1={}
if 'x' not in pol1_lst2[-1]:
    #coef1[0]=int(pol1_lst2[-1])
    #del pol1_lst2[-1]
    pol1_lst2[-1]+='x^0'
    #print(pol1_lst2[-1])

for i in range(len(pol1_lst2)):
    if '^' not in pol1_lst2[i]:
        pol1_lst2[i]+='^1'
        print(pol1_lst2[i])

for i in pol1_lst2:
    a, b = i.split('x')
    if a == '':
        a=1
    elif a == '-':
        a=-1
    coef1[int(b[-1])]=int(a)            
print(pol1_lst2)
print(coef1)
f1.close()

f2 = open('pol2.txt', 'r')
pol2_lst=f2.readline()
pol2_lst2=pol2_lst.replace(" ", "").replace("-", "+-")[:-2].split("+")
print(pol2_lst)
print(pol2_lst2)

coef2={}
if 'x' not in pol2_lst2[-1]:
    #coef1[0]=int(pol1_lst2[-1])
    #del pol1_lst2[-1]
    pol2_lst2[-1]+='x^0'
    #print(pol1_lst2[-1])

for i in range(len(pol2_lst2)):
    if '^' not in pol2_lst2[i]:
        pol2_lst2[i]+='^1'
        print(pol2_lst2[i])

for i in pol2_lst2:
    a1, b1 = i.split('x')
    if a1 == '':
        a1=1
    elif a1 == '-':
        a1=-1
    coef2[int(b1[-1])]=int(a1)            
print(pol2_lst2)
print(coef2)
f2.close()