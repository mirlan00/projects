# for i in range(1,6):
#     if i % 2 == 0:
#         print(f"четный {i}")
#     else:
#         print(f"нечетный {i}")

# s=0

# for i in range(1,11):  #1 -10 го чейинкинин ортонку числосу
#     s += i
#     a=s/10
# print(a)

# sum = 0
# for i in range(1, 11):
#     sum += i
# print("Сумма чисел от 1 до 5:", sum)
# average = sum / 10
# print(average)

# num = 4
# for i in range(1,11):
#     print(num, "x", i, "=",num*i)

# num = 4
# for i in range(1,11):#4 тун таблицасын чыгар де атат
#     res = num*i
#     print(f"{num} x {i} = {res}")

# word = input("Введите слово: ") # Получаем ввод слова от пользователя
# for char in word: # Итерируем по каждому символу в слове
#     print(char * 3, end='') 
n = 5  # количество строк в узоре
for i in range(n):  # для каждой строки
    for j in range(i + 1):  # для каждого символа в строке
        print("*", end="")  # выводим символ звезды
    print()  # переводим строку