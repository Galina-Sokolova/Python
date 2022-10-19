# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.
lst = [1.1, 1.2, 3.1, 5.02, 10.01, 1.01, 7.6]
lst_fractions = []
for i in range(len(lst)):
    lst_fractions.append(round(lst[i]-int(lst[i]), 2))
print(lst_fractions)    
i_max=0
i_min=0
for i in range(len(lst_fractions)):
    if lst_fractions[i]>lst_fractions[i_max]:
        i_max=i
    elif lst_fractions[i]<lst_fractions[i_min]:
        i_min=i   
diff=lst_fractions[i_max]-lst_fractions[i_min]   
print('a[',i_max,'] -','a[',i_min,'] =',diff)      