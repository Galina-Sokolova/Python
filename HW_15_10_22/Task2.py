# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
stek = [2, 3, 4, 5, 6]
stek_total = []
middle = round(len(stek)/2 + 0.1)
for i in range(middle):
    stek_total.append(stek[i]*stek[len(stek)-1-i])
print(stek_total)    
