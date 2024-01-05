
    #hw1
# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)

    #hw2

# numbers = {'num_1': 1, 'num_2': 2, 'num_3': 3, 'num_100': 100}
# print(numbers)
# for key in numbers:
#     numbers[key] *=5
# print(numbers)
    
    #hw3
# student = {'name' : 'Askhat', 'age' : 17}
# student['age'] *=2
# print(student)

    #hw4

# student = {'name' : 'Askhat', 'age' : 17, 'color ':'White'}
# student['age'] =16
# print(student)

    #hw5

# student = {'name' : 'Askhat', 'age' : 17}
# student.pop('age')
# print(student)

    #hw6

# student = {'name' : 'Askhat'}
# student.setdefault('address','Западный Анар')
# print(student)

    #hw7
# def chat_bot():
#     while True:
#         user = input("Введите ваш вопрос: ")
#         if user == "":
#             print("Как классно, когда ты молчишь. Продолжай в том же духе!")
#         elif user.isupper():#чон тамга болсо
#             print("Успокойся")
#         elif user[-1] == "?":#акыркы жагында ? символу болсо деген
#             print("Конечно!")
#         else:
#             print("Ну и что")

# chat_bot()

    #hw8
# def shorten_phrase(phrase):
#     words = phrase.split()#разбиваем ее на список
#     abbreviation = ''.join([word[0].upper() for word in words if word.isalpha()])
#     return abbreviation
    
#     return abbreviation
# print(shorten_phrase("Кыргызская Республика")) 
# print(shorten_phrase("Ruby on Rails")) 
# print(shorten_phrase("For your interest")) 

    #9
# def count_word(text:str='Hello world')-> dict:
#     print(text)
#     lower_text = text.lower().split(",")#болуп туруп лист кылып чыгарып берет 
#     print(lower_text)
#     space_delate = "".join(lower_text).split()
#     print(space_delate)
#     result = {}
#     for space in space_delate:
#         result.setdefault(space,space_delate.count(space))
#     print(result)
# count_word("Money, money, money, it's always sunny, in the richmen's world")
