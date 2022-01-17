print("\nМОДУЛЬ 1")
inp=" "
while (inp.isdigit()==False):
    inp=input("Ведите количество элементов: ")
inp=int(inp)
lst = []
var=0
while (var<inp):
    print("Введите", var+1, "элемент:", end=' ')
    char = input(" ")
    try:
        num = int(char)
        if (num>9):
            raise Exception
        lst.append(num)
        var+=1
    except:
        print("Вы ввели не цифру")
lst.sort()
print("Вывод ", lst)
