# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def RLE_compression(text):
    lst = []
    count = 1
    i = 1
    while i < len(text):
        if text[i-1] == text[i]:
            count += 1
        else:
            count = str(count)
            lst.append(text[i-1]+count)
            count = 1
        i += 1

    i = 0
    count = 1
    while text[-1-i] == text[-2-i]:
        count += 1
        i += 1
    count = str(count)
    lst.append(text[-1] + count)
    return lst

def RLE_restore(lst):
    txt = ""
    for i in range(len(lst)):
        elm = str(lst[i])
        char = elm[0]
        count = int(elm[1:])
        for j in range(count):
            txt += char
    return txt        

with open('file1.txt', 'r') as f1:
    us_text = f1.read()
#print(type(RLE_compression(us_text)))
temp = RLE_compression(us_text)
txt_compress = ''.join(temp)

with open('file2.txt', 'w') as f2:
    f2.write(txt_compress)

txt_rest = RLE_restore(temp)
print(txt_rest)

   