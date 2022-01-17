print("\nМОДУЛЬ 3")

def input_list():
    inp=" "
    sep=''
    lst=[]
    len_lst=1
    len_inp=0

    while (len_lst>len_inp):
        inp=input("Ведите цифры с одним из разделителей ',' '/' ';': ")
        inp = inp.strip(' ')
        lst = inp;
        count1=bool(lst.count(','))
        count2=bool(lst.count('/'))
        count3=bool(lst.count(';'))
        if((count1^count2^count3)&(not(count1&count2&count3))):
            if(count1):
                sep=','
            if(count2):
                sep='/'
            if(count3):
                sep=';'
            lst = []
            try:
                for var in inp.split(sep):
                    lst.append(int(var))
                    len_lst=len(lst)
                    len_inp=int(len(inp)/2+1)
            except:
                print("В данных есть не только цифры")
                len_lst=1
                len_inp=0
        else:
            print("Разделители дожны быть одного типа")
    print(lst)
    return lst
print("Первый список")
lst1 = list(input_list())
print("Второй список")
lst2 = list(input_list())
lst3 = lst1
for val in lst2:
    try:
        lst3.remove(val)
    except:
        a=0
print("Результирующий список\n",lst3)
