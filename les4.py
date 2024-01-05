# #list списки 
# # бардык тип данныйлар кире берет 

# names = ["nur", "bek", "mir"] #созсуз квадратный кавычкада болот
# print(names)
# names.append("ulan") # метод append уже барга дагы жаны нерсе Аягына кошуу
# print(names)
# names.insert(0,"jigit")#метод insert индекс мн любой жерге кошуу
# print(names)
# names.remove("bek")#метод remove списоктон удалить эткени
# print(names)
# # names.pop(2) #метод pop индекс мн удалить эткени
# # print(names)
# # del names[1]#метод del индекс мн удалить эткени бирок за раз бир нече удалить этсе болот
# # #по срезам тоже можно
# # print(names)
# names[0] = "mirbek"#обнавление данных из списка с  индексу
# print(names)

# cars = ["BMW", "LEXUS", "TOTOTA","BYD"]
# print(cars)
# print(cars[1]) # ичинен бир индексти гана чыгаруу
# print(cars[1][2])
# cars.insert(2,"Tesla")
# print(cars)
# cars[2] = "MERCEDES"
# print(cars)
# cars.remove("BYD")
# print(cars)
# print(cars[::-1])


                    #tuple - кортежи
                    #озгортсо болбойт анан тоголок каша алынат
names = ("adilet","erbol", "beksultan")
print(names)
print(type(names))# тип билуу учун
print(names.count("erbol"))#count  окшош элемент канчоо бар экенин билиш учун
print(names.index("adilet")) #index элементтин индексин билиш учун

lst_names = list(names)
print(lst_names)

lst_names.append("gena")
print(lst_names)
