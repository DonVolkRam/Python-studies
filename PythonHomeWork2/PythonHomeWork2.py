
#Задачи на циклы и оператор условия------
#----------------------------------------

print("Задача 1")
print("Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.")
str_zero="строка нулей 000"
for val in range(1,6):
    print(val,str_zero)


print("\nЗадача 2")
print("Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.")
lst = []
var=0
while (var<10):
    char = input("Введите цифру: ")
    try:
        num = int(char)
        if (num>9):
            raise Exception
        lst.append(num)
        var+=1
    except:
        print("Вы ввели не цифру")
count=0
find=5
for var in lst:
    if (var==find):
        count+=1
print("Количество введенных цифр ",find, " = ",  count)


print("\nЗадача 3")
print("Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран")
sum = 0
for i in range(1,101):
    sum+=i
print(sum)


print("\nЗадача 4")
print("Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.")
sum=1
for i in range(1,11):
    sum*=i
print(sum)


print("\nЗадача 5")
print("Вывести цифры числа на каждой строчке.")
integer_number = 2129
cpy=integer_number
print("Число ", integer_number)
#уже было
while integer_number>0:
     print(integer_number%10)
     integer_number = integer_number//10
print("mine")
#мое решение
str_number = str(cpy)
for char in str_number:
    print(char)


print("\nЗадача 6")
print("Найти сумму цифр числа.")
inp=''
while not inp.isdigit():
    inp=input("Введите чиcло ")
str_number = str(inp)
sum=0
for char in str_number:
    sum+=int(char)
print("Сумма чисел = ", sum)


print("\nЗадача 7")
print("Найти произведение цифр числа.")
sum=1
for char in str_number:
    sum*=int(char)
print("Произведение чисел = ", sum)


print("\nЗадача 8")
print("Дать ответ на вопрос: есть ли среди цифр числа 5?")
print("Число ", inp)
copy_inp=int(inp);
while copy_inp>0:
    if copy_inp%10 == 5:
        print('Есть 5')
        break
    copy_inp = copy_inp//10
else: print('Нет 5')


print("\nЗадача 9")
print("Найти максимальную цифру в числе")
max_num=0;
copy_inp=int(inp);
print("Число ", inp)
while copy_inp>0:
    if copy_inp%10 > max_num:
        max_num=copy_inp%10
    copy_inp = copy_inp//10
print("Максимальная цифра = ", max_num)


print("\nЗадача 10")
print("Найти количество цифр 5 в числе")
print("Число ", inp)

str_number = str(inp)
sum=0
for char in str_number:
    if(char=='5'):
        sum+=1
print("Количество цифр 5 = ", sum)

