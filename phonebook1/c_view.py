from model import display_all_contacts
from model import add_contact
from model import contact_search
from model import delete_contact


def view_data(data):
    for i in data:
        print(i)

def get_fio():
    return input('Enter fio: ')

def get_comment():
    return input('Enter comment: ')        

def get_phone_number():
    return input('Enter phone number: ')


def enter_entry():
    f = get_fio()
    pn = get_phone_number()
    c = get_comment()
    data = [f, pn, c]
    return data  

def menu():
    print('\nГлавное меню:\n'
    '\n1. Показать все контакты\n'
    '2. Поиск контакта\n'
    '3. Добавить конаткт\n'
    '4. Удалить контакт\n'
    '0. Выход')
    return (int(input('-->')))      

def main_lopp():
    while True:
        choise = menu()
        if choise == 1:
            display_all_contacts()
        elif choise == 2:
            contact_search(input('Введите текст для поиска контакта: '))
        elif choise == 3:
            add_contact()
        elif choise == 4:
            delete_contact()
        elif choise == 0:
            break