# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = 'абв Ура, питон крутой абвязык, очень интересные скминарабвы'
lst = text.split()
lst1 = [lst[i] for i in range(len(lst)) if 'абв' not in lst[i]]
res = ' '.join(lst1)
print(res)
# lst = ' '.join(list(filter(lambda s: 'абв' not in s, text.split())))
# print(lst)