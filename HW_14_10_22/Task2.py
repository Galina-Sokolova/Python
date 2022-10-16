# Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.
N = int(input("Ведите число: "))
list=[]
list.append(1)
for i in range(1, N):
    list.append(list[i-1]*(i+1))
print(list)    