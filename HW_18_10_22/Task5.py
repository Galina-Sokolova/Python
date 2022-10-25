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
    for i in range(1, K+1):
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
pol1_lst2=pol1_lst.replace(" ", "").replace("-", "+-")[:-2]
if pol1_lst2[0]=='+':
    pol1_lst2=pol1_lst2[1:]
pol1_lst2=pol1_lst2.split("+")    
#print(pol1_lst2)

coef1={}
if 'x' not in pol1_lst2[-1]:
    pol1_lst2[-1]+='x^0'

for i in range(len(pol1_lst2)):
    if '^' not in pol1_lst2[i]:
        pol1_lst2[i]+='^1'

for i in pol1_lst2:
    a, b = i.split('x')
    if a == '':
        a=1
    elif a == '-':
        a=-1
    coef1[int(b[-1])]=int(a)            
# print(pol1_lst2)
# print(coef1)
f1.close()

f2 = open('pol2.txt', 'r')
pol2_lst=f2.readline()
pol2_lst2=pol2_lst.replace(" ", "").replace("-", "+-")[:-2]
if pol2_lst2[0]=='+':
    pol2_lst2=pol2_lst2[1:]
pol2_lst2=pol2_lst2.split("+")

coef2={}
if 'x' not in pol2_lst2[-1]:
    pol2_lst2[-1]+='x^0'
    
for i in range(len(pol2_lst2)):
    if '^' not in pol2_lst2[i]:
        pol2_lst2[i]+='^1'
        
for i in pol2_lst2:
    a1, b1 = i.split('x')
    if a1 == '':
        a1=1
    elif a1 == '-':
        a1=-1
    coef2[int(b1[-1])]=int(a1)            
#print(pol2_lst2)
#print(coef2)
f2.close()

max_coef=max(max(coef1.keys()), max(coef2.keys()))
coef={}
for i in range(max_coef+1):
    coef[i]=coef1.get(i, 0)+coef2.get(i, 0)
#print(coef) 
valLst=list(coef.values()) 
#print(valLst)  

res = ''
for i in range(len(valLst)-1, 0, -1):
    if valLst[i] == 1:
        res+='+x^'+str(i)
    elif valLst[i] == -1:  
        res+='-x^'+str(i) 
    elif valLst[i] == 0:
        res+=''
    else:
        res+='+'+str(valLst[i])+'x^'+str(i)   
if valLst[0] != 0:        
    res+='+'+str(valLst[0])  
res = res.replace("^1+", "+").replace("+-", "-")+'=0'  
if res[0] == '+':
    res = res[1:]
print('Результат сложения 2-х многочленов (записан в файл poly.txt): \n', res) 

poly=open('poly.txt', 'w')
poly.writelines(res)
poly.close()       