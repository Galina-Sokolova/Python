# Задайте список из n чисел последовательности (1 + 1/n)^n 
# и выведите на экран их сумму.
a={}
num = int(input("Ведите число: "))
sum = 0
for i in range (1, num+1):
    a[i] = round((1 + 1/i)**i, 2)
    sum+=a[i]
print(a)  
print("Сумма", num, "членов последовательности = ",sum)  