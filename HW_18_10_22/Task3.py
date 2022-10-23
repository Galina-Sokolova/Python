# Задайте последовательность цифр. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.
subseq='1113384455229'
lst=list(subseq)
lst1=[]
for i in range(len(lst)):
    count=lst.count(lst[i])
    if count==1:
        lst1.append(int(lst[i]))
      
print(lst1)