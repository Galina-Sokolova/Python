# Вычислить число Пи c заданной точностью d
d = input('Введите нужную точность: ')
n=list(d)
n1=1
for j in range(len(n)):
    n1*=10

num_pi = 4
for i in range(3, n1, 4):
    num_pi = num_pi - 4/i + 4/(i+2)
num_pi_as_string=str(num_pi)    
print(num_pi_as_string[:len(n)])    
