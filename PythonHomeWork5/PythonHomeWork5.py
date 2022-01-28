import os
import sys
import shutil
sys.path.insert(1,os.path.join(sys.path[0], '..'))

from PythonHomeWork3.victory import victory_game
from PythonHomeWork4.use_functions import money_game
from PythonHomeWork1.PythonHomeWork1 import about

def create_dir():
    dir_name = input("Введите имя новой папки: ")
    path = os.path.join(os.getcwd(),dir_name)
    if not os.path.exists(path):
        # сздать папку передаем путь
        os.mkdir(path)  
        print(f"Создана папка {path}")
    else:
        print("Такая папка уже существет")

def remove_dir():
    dir_name = input("Введите имя удаляемой папки: ")
    path = os.path.join(os.getcwd(),dir_name)
    if os.path.exists(path):
        # сздать папку передаем путь
        os.rmdir(path)
        print(f"Удалена папка {path}")
    else:
        print("Такая папка не существет")

def about_me():
    print("Автор Волков К.А.")

def watch_all():
    print(os.listdir())

def watch_files():
    with os.scandir(os.getcwd()) as listOfEntries:  
        for entry in listOfEntries:        
            if entry.is_file():
                print(entry.name)

def watch_dirs():
     with os.scandir(os.getcwd()) as listOfEntries:  
        for entry in listOfEntries:        
            if not entry.is_file():
                print(entry.name)

def copy_file():
    name = input("Введите имя файла/папки: для копирования ")
    path = os.path.join(os.getcwd(),name)
    if not os.path.exists(path):
        print("Такого файла/папки не существует")
        return
    name_cpy = input("Введите новое имя файла/папки: для копирования ")
    path = os.path.join(os.getcwd(),name_cpy)
    if not os.path.exists(path):
        shutil.copy(name, name_cpy)
    else:
        print("Такой файл/папка уже существует")

def change_dir():
    name = input("Введите имя новой директории ")
    if os.path.exists(name):
        print(f"смена рабочей директории с {os.getcwd()}")
        os.chdir(name)
        print(f"на {os.getcwd()}")
    else:
        print("Такой директории не существует")

while True:
        print('\n1. создать папку')
        print('2. удалить (файл/папку)')
        print('3. копировать (файл/папку)')
        print('4. просмотр содержимого рабочей директории')
        print('5. посмотреть только папки')
        print('6. посмотреть только файлы')
        print('7. просмотр информации об операционной системе')
        print('8. создатель программы')
        print('9. играть в викторину')
        print('10. мой банковский счет')
        print('11. смена рабочей директории')
        print('12. выход')

        choice = input('Выберите пункт меню: ')
        print("\n")
        if choice == '1':           
            create_dir()
        elif choice == '2':
            remove_dir()
        elif choice == '3':
            copy_file()
        elif choice == '4':
            watch_all()
        elif choice == '5':
            watch_dirs()
        elif choice == '6':
            watch_files()
        elif choice == '7':
            about()
        elif choice == '8':
            about_me()
        elif choice == '9':
            victory_game()
        elif choice == '10':
            money_game()
        elif choice == '11':
            change_dir()
        elif choice == '12':
            break
        else:
            print('Неверный пункт меню')