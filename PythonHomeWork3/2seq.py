
print("\nМОДУЛЬ 2")
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
        lsts=set(lst);
        lst_cpy = []
        string = str(lst)
        string = string.replace(',','')
        string = string.replace(' ','')
        for val in lst:
            if(lst.count(val)>1):
                string=string.replace(str(val),'')
        string=string.lstrip('[')
        string=string.rstrip(']')
        for char in string:
            lst_cpy.append(int(char))
        print("Вывод",lst_cpy)
    else:
        print("Разделители дожны быть одного типа")