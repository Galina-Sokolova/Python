#  Напишите программу, которая принимает на вход вещественное 
#  число и показывает сумму его цифр.
num = input("Ведите число: ")
num = num.replace('.', '')
num = num.replace(',', '')
num = num.replace('-', '')
num = int(num)
sum = 0
while num != 0:
    rem = num%10
    num = num//10
    sum+=rem
print("Сумма цифр введенного числа = ",sum)




