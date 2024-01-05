    #hw1
#исключения ошибканы алдын алыш учун колдонулат.И более понятный кылып коёт

    #hw2

# try:
#     print(name)
# except NameError:
#     print("Ошибка  переменной")
# raise IndexError("Такой индекс не существует")

    #hw3
# user_number = input("Введите несколько чисел разделенных запятой: ")
# user_number = {}
# print(user_number)

input_numbers = input("Введите числа, разделенные запятой: ")
split_numbers = input_numbers.split(',')  # разделение чисел по запятой
numbers_set = set(split_numbers)  # создание множества на основе списка
print(numbers_set)