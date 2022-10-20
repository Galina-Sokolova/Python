# Задайте число. Составьте список чисел Фибоначчи, в том числе для 
# отрицательных индексов.
def Compose_Fibonacci_lst(num):
    lst = [0, 1]
    i = 1
    while i < num:
        lst.append(lst[i-1] + lst[i])
        i+=1

    i = 0
    k = 1
    while i < num*2:
        lst.insert(0, lst[i+1]*k)
        i+=2
        k=-k
    return lst        

num = int(input('Введите целое число: '))
print(Compose_Fibonacci_lst(num))    