# Реализуйте алгоритм перемешивания списка.
import random

stek = [23, 5, -15, 36, -1, 1.25, -100]
stek1 = []
while stek != []:
    i = random.randint(0, len(stek)-1)
    stek1.append(stek[i])
    stek.pop(i)
print(stek1)