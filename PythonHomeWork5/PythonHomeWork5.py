import os
import sys
import shutil
import pickle

FILE_NAME = 'listdir.txt'

sys.path.insert(1,os.path.join(sys.path[0], '..'))

from PythonHomeWork3.victory import victory_game
from PythonHomeWork4.use_functions import money_game
from PythonHomeWork1.PythonHomeWork1 import about

def add_separators(f):
    # inner - итоговая функция с новым поведение
    def inner(*args, **kwargs):
        # поведение до вызова
        print('*' * 10)
        result = f(*args, **kwargs)
        # поведение после вызова
        print('*' * 10)
        return result

    # возвращается функция inner с новым поведением
    return inner

@add_separators
def get_dirs():
    dirs = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'rb') as f:
            dirs = pickle.load(f)
    return dirs

@add_separators
def save_dirsfiles(indirs, infiles):
    with open(FILE_NAME, 'w') as f:
        files = "files: "
        for i in infiles:
            files += i+", " 
        files += "\ndirs: " 
        for i in indirs:
            files += i+", "
        f.write(files)

@add_separators
def create_dir():
    dir_name = input("Введите имя новой папки: ")
    path = os.path.join(os.getcwd(),dir_name)
    if not os.path.exists(path):
        # сздать папку передаем путь
        os.mkdir(path)  
        print(f"Создана папка {path}")
    else:
        print("Такая папка уже существет")

@add_separators
def remove_dir():
    dir_name = input("Введите имя удаляемой папки: ")
    path = os.path.join(os.getcwd(),dir_name)
    if os.path.exists(path):
        # сздать папку передаем путь
        os.rmdir(path)
        print(f"Удалена папка {path}")
    else:
        print("Такая папка не существет")

@add_separators
def about_me():
    print("Автор Волков К.А.")

@add_separators
def watch_all():
    print(os.listdir())

@add_separators
def watch_files():
    files = []
    with os.scandir(os.getcwd()) as listOfEntries:
        files = [entry.name for entry in listOfEntries if entry.is_file()] #генератор
        print(files)
        #for entry in listOfEntries:        
        #    if entry.is_file():
        #        print(entry.name)
        #        files.append(entry.name)
    return files

@add_separators
def watch_dirs():
     dirs = []
     with os.scandir(os.getcwd()) as listOfEntries:  
        dirs = [entry.name for entry in listOfEntries if not entry.is_file()]  #генератор
        print(dirs)
        #for entry in listOfEntries:        
        #    if not entry.is_file():
        #        print(entry.name)
        #        dirs.append(entry.name)
     return dirs

@add_separators
def copy_file():
    name = input("Введите имя файла/папки: для копирования ")
    path = os.path.join(os.getcwd(),name)
    if not os.path.exists(path):
        print("Такого файла/папки не существует")
        return
    name_cpy = input("Введите новое имя файла/папки: для копирования ")
    path = os.path.join(os.getcwd(),name_cpy)
    shutil.copy(name, name_cpy) if not os.path.exists(path) else print("Такой файл/папка уже существует")  #тернарный оператор
    #if not os.path.exists(path):
    #    shutil.copy(name, name_cpy)
    #else:
    #    print("Такой файл/папка уже существует")

@add_separators
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
        print('12. сохранить содержимое рабочей директории в файл')
        print('13. выход')

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
            save_dirsfiles(watch_dirs(),watch_files())
        elif choice == '13':
            break
        else:
            print('Неверный пункт меню')