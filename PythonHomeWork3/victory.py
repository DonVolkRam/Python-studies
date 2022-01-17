import numpy as np
import random
def victory():
    people = ["Пушкин А.С.","Толстой Л.Н.", "Лермонтов М.Ю.", "Достоевский Ф.М.", 
              "Ломоносов М.В.", "Суворов А.В.", "Джугашвили И.В.", "Циолковский К.Э.",
              "Королёв С.П.", "Менделеев Д.И."] 
    datatime = ["1799-06-06","1828-09-09", "1814-10-15", "1821-11-11",
                "1811-11-19", "1730-11-24", "1879-12-21", "1857-09-17",
                "1907-01-12", "1834-02-08"]
    days_d = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    days = ["первое" , "второе" , "третье", "четвертое" , "пятое" , "шестое" , "седьмое", "восьмое" , "девятое" , "десятое" , 
            "одиннадцатое" , "двенадцатое" , "тринадцатое" , "четырнадцатое" , "пятнадцатое" , "шестнадцатое" , "семнадцатое" , "восемнадцатое" , 
            "девятнадцатое" , "двадцатое" , "двадцать первое" , "двадцать второе" , "двадцать третье", "двадцать четвертое" , "двадцать пятое" , 
            "двадцать шестое" , "двадцать седьмое" , "двадцать восьмое" , "двадцать девятое" , "тридцатое" , "тридцать первое"]
    month = ["января" , "февраля" , "марта" , "апреля" , "мая" , "июня" , "июля" , "августа" , "сентября" , "октября" , "ноября" , "декабря"]
    month_d =[1,2,3,4,5,6,7,8,9,10,11,12]
    for val in datatime:
        val = np.datetime64(val)
        people_data = dict(zip(people,datatime))
    day_data = dict(zip(days_d,days))
    month_data = dict(zip(month_d, month))
    #print(people_data)
    num_question = 5
    result = random.sample(people, num_question)
    #print(result)
    score=0
    for i in range(num_question):
        print("Когда отмечал день рождения ", result[i], "? :", end=" ")
        answer=input()
        sdata = list(answer.split("."))
        sdata.reverse()
        #print(sdata)
        answer_for_comp=""
        for val in sdata:
            answer_for_comp+=str(val)+"-"
        answer_for_comp=answer_for_comp.rstrip("-")
        answer=answer_for_comp
        #print(answer_for_comp)
        if(answer==people_data.get(result[i])):
            print("Верно")
            score+=1
        else:
            sdata = list(str(people_data.get(result[i])).split("-"))
            print("Прваильный ответ:", day_data.get(int(sdata[2])-1), month_data.get(int(sdata[1])), sdata[0], "года", sep=" ")
        i+=1
    print("Ваши очки", score, "из", num_question, sep=" ")

res="да"
print("Добро пожаловать на викорину! Вам предстоит отгадать дни рождения известных людей в России")
print("Формат ответа дд.мм.гггг")
while (res=="да"):
    victory()
    res=input("Сыграть еще? (да/нет)")