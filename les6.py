#Исключение try, except ощибканы алдын ала ондоо 

# try: #попытайся
#     print(100/0)
# except ZeroDivisionError: #если
#     print("нолго болсо болбойт")



# while True:
#     num1 = int(input("num1: "))
#     operator = input("+,-,*,/: ")
#     num2 = int(input("num2: "))
#     if operator == "+":
#         print(num1+num2)
#     elif operator == "-":
#         print(num1-num2)
#     elif operator == "*":
#         print(num1*num2)
#     elif operator == "/":
#         try:
#             print(num1/num2)
#         except ZeroDivisionError:
#             print("Деление на ноль")
#     elif num1 == 0 and operator == "0"  and num2 == 0:
#         print("STOP")
#         break
#     else:
#         print("operator not found")

# name = "Nur"
# try:
#     print(neme)
# except NameError:
#     print("Ошибка  переменной")



# try:
#     print(kk)
# except BaseException as error:
#     print("Error",error)


# raise StopIteration("Cпециальный вызов ошибки Python StopIteration") #raise  атайы ошибканы чакырганда колдо


# car = "BMW"
# try:
#     print(car[2])
# except BaseException:
#     raise IndexError("Мындай индекс жок")
# finally:
#     print("Баарыбир иштейм")


#  set=> дубликат азайтуу, озгоро турган тип данный,  frozenset-> озгорбогон  тип данный. кошумча тип данныйлар

# n1= [10,20,30,40,50]
# n2= [30,40,50,60,70]
# print(n1+n2)
# print(set(n1+n2)) # {} ушу знак мн терминалга чыгарат

# names = {"argen","nurik","nurik","baigazy"}# set жазбайле мынаны -> {} жазса болот ордуна: .pop()кокостан любойун очурот 
# print(names)
# names.add("Geeks")
# print(names)
# names.remove("argen")
# print(names)
# names.pop()#удалить по индексу
# print(names)
# names.clear()#удалить всё
# print(names)


# car1 = {"BMW", "LEXUS"}
# car2 = {"LEXUS", "TOYOTA"}
# print(car1.difference(car2))

# frzn_set = frozenset({10,10,20,20,30,})
# print(frzn_set)


# import random

# random_number = random.randint(1,11)
# # print(random_number)
# attempts = 3
# while True:
#     attempts -=1 # ушу эко окшош эле attempts = attempts-1
#     use_number = int(input("Число от 11 до 10: "))
#     if random_number == use_number:
#         print("Ты выиграл!")
#         break
#     elif attempts == 0:
#         print("Ты проиграл :( правильный ответ: ", random_number)
#     else:
#         print("неправилно у вас ", attempts, "попыток")