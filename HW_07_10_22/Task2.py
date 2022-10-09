# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
from itertools import count
from unittest import result


print('Левая часть выражения ¬(X ⋁ Y ⋁ Z)   Правая часть выражения ¬X ⋀ ¬Y ⋀ ¬Z\n')
print(' X \tY \tZ \tРезультат   X\t  Y\t  Z\tРезультат\n')
count=0
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            resultLeft = not(x or y or z)
            resultRight = not x and not y and not z
            print(f'{x}\t{y}\t{z}\t  {resultLeft} |    {x}\t   {y}\t {z}\t{resultRight}')
            if resultLeft == resultRight:
                count+=1
if count == 8:
    print('Результаты идентичны, утверждение истинно') 
else:
    print('Утверждение ложно')    

            
    


