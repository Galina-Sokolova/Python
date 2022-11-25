import c_view

def add_contact():
    with open('direct.txt', 'a', encoding='utf-8') as file:
        data = c_view.enter_entry()
        for lines in data:
            file.writelines(lines+ ' ')
        file.writelines('\n')    

def display_all_contacts():
    with open('direct.txt', 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            print(line)

def contact_search(data):
    data = data.lower()
    with open('direct.txt', 'r', encoding='utf-8') as file:
        count = 0
        line_number = 0
        while True:
            line = file.readline().lower()
            line_number+= 1
            if not line:
                break
            elif data in line:
                count+=1
                print(f'{line_number}. {line}') 
    if count == 0:
        print('Контакт не найден')

def delete_contact():
    with open('direct.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        # print(type(lines))       
        # print(lines)
        data = input('Введите текст для поиска контакта: ') 
        contact_search(data)
        count = int(input('Введите № контакта, который хотите удалить: '))
        # for i in len(lines):
        #     if count == i+1:
        print(f'Будет удален контакт {count} {lines[count-1]}\n')
        while True:
            answer = input('Вы уверены(да/нет)? ').lower()
            if answer == 'да':
                del lines[count-1]
                break
            else:
                break
        with open('direct.txt', 'w', encoding='utf-8') as file:
            for line in lines:
                file.writelines(line)
            file.writelines('\n')

           



                       

           