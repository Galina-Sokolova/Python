# Задайте натуральное число N. Напишите программу, которая составит 
# список простых множителей числа N.

def is_num_prime(n):
    count=0
    for i in range(1, n+1):
        rem=n%i
        if rem==0:
            count+=1
    if count==2:
        return True
    else:
        return False   

N = int(input('Введите натуральное число '))
#print(is_num_prime(N))
lst=[]
for i in range(1, N+1):
    if N%i==0 and is_num_prime(i)==True:
        lst.append(i)
print(lst)