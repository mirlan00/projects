#циклы for,while
# for i in range(1001):  #range = диапазон 
#     print(i)

# for i in range(1, 11):  # 1ден 10 го чейин чыгар деп айтканда
#     print("Geeks", i)

# for i in range(1, 101, 2):    #  i бул переменый: четный кылат  
#     print(i)

# for i in range(2, 201): 
#     if  i % 2 == 0:
#         print(i, "четный")
#     else:
#         print(i, "нечетный")

# cars = ["BMW", "LEXUS", "TOYOTA", "BYD"]
# print(cars)
# print(len(cars))#len узундугун ичинлегини эсептейт
# for car in cars:
#     print(car)

# names = "Beksultan"
# for n in names:
#     print(n)

# names = "Beksultan"
# print(names)
# for n in names:
#     if n  == "s":
#         print("s есть")

# numbers = (10,25,15,48,75,5)
# for number in numbers:
#     if number % 2 == 0:
#         print(number, "четный")
#     else:
#         print(number, "нечетный")

# import random # выбор случайности
# len_password = int(input("Длина пароля:"))
# letters = "qwertyuiopasdfghjk123456789"
# result = ""

# for i in range(len_password):
#     choice = random.choice(letters)
#     print(choice)

# import random # выбор случайности
# len_password = int(input("Длина пароля:"))
# count_password = int(input("Количество  паролей:"))
# letters = "qwertyuiopasdfghjk123456789@#$%^^&*"
# for c in range(count_password):
#     result = ""

#     for i in range(len_password):
#         choice = random.choice(letters)
#         result += choice
#     print(c + 1, result)

# import random # выбор случайности
# len_password = int(input("Длина пароля:"))
# letters = "qwertyuiopasdfghjk123456789@#$%^^&*"
# result = ""

# for i in range(len_password):
#     choice = random.choice(letters)
#     result += choice
# print(result)

# n1 = 10
# n2 = 20
# while n1 < n2: #while  ичи true  болгондо гана иштейт
#     n1 += 1
#     print(n1)

# n = 0
# while True:
#     n +=1
#     print(n) #CTRL + C бесконечносту токтотот
#     if n == 10:
#         print("До 10ти")
#         break # тототот

# for num in range(1, 1000):
#     print(num)
#     if num == 509:
#         print("До 509ти")
#         break
#     else:
#         continue#улантат


# import time #убакытты кошту
# progress = 0
# while True:
#     time.sleep(1.5)
#     progress += 10
#     print("HACK", str(progress)+"%") #intти  strга озгортту аркасында %кошуш учун
#     if progress == 100:
#         print("HACKED")
#         break
