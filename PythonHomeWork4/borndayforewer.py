"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""


def question (question, answer):
    year = input(question)
    while year != answer:
        print("Не верно")
        year = input(question)

question("Ввведите год рождения А.С.Пушкина:",'1799')
question("В какой день июня родился Пушкин?",'6')
