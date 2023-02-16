"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

import os
import pickle

FILE_NAME_ORDERS = 'orders.data'
FILE_NAME_MONEY = 'money.data'

def get_orders():
    orders = []
    if os.path.exists(FILE_NAME_ORDERS):
        with open(FILE_NAME_ORDERS, 'rb') as f:
            orders = pickle.load(f)
    return orders


def get_money():
    money = 0
    if os.path.exists(FILE_NAME_MONEY):
        with open(FILE_NAME_MONEY, 'rb') as f:
            money = pickle.load(f)
    return money

def money_game():
    orders = get_orders()
    money = get_money();
    #history_m = []
    #history_w = []
    while True:
        
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            while (True):
             try:
                 money += int(input("Внесите денежные средства: "))
                 print(f"Доступные средства {money}")
                 break
             except ValueError:
                 print("Ошибка ввода")
             except:
                 print("Неизвестная ошибка!")
             finally:
                 print("Спасибо что пользуетесь нашим банком")
        elif choice == '2':
            while (True):
             try:
                 cost = int(input("Введите сумму покупки: "))
                 name=''
                 if cost>money:
                    print("Недостаточно средств")
                    break
                 else:
                    name = input("Введите название покупки: ")
                    #history_m.append(cost)
                    #history_w.append(name)
                    order = (name, cost)
                    orders.append(order)
                    print("Покупка одобрена")
                    money-=cost
                    print(f"Доступные средства {money}")
                    break
             except ValueError:
                 print("Ошибка ввода")
             except:
                 print("Неизвестная ошибка!")
             finally:
                 print("Спасибо что пользуетесь нашим банком")
        elif choice == '3':
            print("История покупок")
            #for i in range(len(history_m)):
            #    print(f"{history_w[i]} --> {history_m[i]}")
            for order in orders:
                print(order)
        elif choice == '4':
            with open(FILE_NAME_ORDERS, 'wb') as f:
                pickle.dump(orders, f)
            with open(FILE_NAME_MONEY, 'wb') as f:
                pickle.dump(money, f)
            break
        else:
            print('Неверный пункт меню')

#money_game()