#модули (башка  файлдан код алып келуу)и файлы
#3 методу бар 1 си
# import  moduls # без оканчание .py

# moduls.reverse_word("Bayastan")

# moduls.count_word("Hello")
# print(moduls.it)

    #2чи метод. импортировать отдельные определение из модуля

# from moduls import reverse_word, count_word
# reverse_word("Elaman")
# count_word("Django")

    #3 ичиндеги бардыгын импорт кылат

# from moduls import * # звёздочка -> барын алып иштете алат деген
# reverse_word("Python")
# count_word("API")
# print(it)

        # работа с файлами. Функция open()

# f = open('test.txt','w')# жаны файл ачат
# f.write("Hello world and Geeks It Courses")#  ичине ушу созду жазат
# f.close() #файлы жабат жаппаса нагруска келет

# py = open('open.py','w')
# py.write("print('Hello world')")
# py.close()

# read_py = open('les5.py','r')
# print(read_py.read())


# rus = open('russian.txt', 'w',encoding='utf-8')
# rus.write("Привет всем,как ваши дела")
# rus.close()

with open('close.txt','w',encoding='utf-8')as close:# озу мн озу жабылып калат
    close.write("How are you? Как дела?")