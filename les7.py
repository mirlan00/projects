#словари - dictionary - > тип данныйдын бир туру
# пара болуп сох болот. индекс жок,бирок ключ аркылуу алса болот
# student = {'name' : 'Alihan', 'age':18}
#             #ключ    значение
# print(student)
# print(type(student))
# print(student['name'])
# print(student['age'])
# student.setdefault('language','Python')#жаны значение кошкондо
# print(student)
# print(len(student))
# print(student.get('name'))# ключ аркылуу значене алуу
# student.pop('age')#метод удаление ключа и значение
# print(student)
# del student['language']#удалить этуунун дагы бир способу
# print(student)

# student['name'] = "Nurbolot"# способ обновление занчение по ключу
# print(student)
# student['address'] = "Amatonv 1B"# ключ жок болсо озу кошуп обновление занчение кылат
# print(student)

# car_tesla = {
#     'id':  103,
#     'model':  'Model X',
#     'year':  2023,
#     'color':  'Black',
# }
# print(car_tesla)
# print(car_tesla['year'])
# print(car_tesla['color'])
# print(car_tesla.get('id'))
# car_tesla['color'] = 'White'
# print(car_tesla)
# car_tesla.pop('year')
# print(car_tesla)
# car_tesla.popitem()# акыркыны удалить этет
# print(car_tesla)
# car_tesla.setdefault('odometer',0)
# print(car_tesla)


# import time

# contact  = [
#     {'name' : 'Nurbolot',
#     'surname':'Erkinbaev',
#     'phone': '0222628297'
#     },
# ]
# print(contact)
# while True:
#     command = input("1 - посмотреть контакты, 2 - добавить, 3 - удалить, 4 - обновить:")
#     if command == "1":
#         for c in contact:
#             print(c)
#     elif command == "2":
#         add_name = input("Name: ")
#         add_surname = input("Surname: ")
#         add_number = input("Number: ")
#         result = {'name': add_name, 'surname':add_surname, 'phone':add_number, 'created': time.ctime()}#time.ctime() данный моменттеги убакыт
#         contact.append(result)
#         print("Контакт добавлен")
#     elif command == "3":
#         delete_number = input("Delete number: ")
#         for cont in contact:
#             for  key, value in cont.items(): #  .items() словарда ключ мн значениени алып берет
#                 if value == delete_number:
#                     contact.remove(cont)
#                     print("Контакт успешно удален")


# language =  {"name": "Python", "version": "3.10.8", "date": "08 september 2023"}
# print(language)
# for key,value in language.items(): # эки значениесиин алуу учун колдонулат
#     print(key,value)

# Function - функция
def hi():#атына кайрылмайсайын ответ бербейт
#функция перменная скобка кавычка
    print("helo world and Geeks")
# hi()
def add():
    n1  = int(input("numeber 1: "))
    n2 = int(input("numeber 2: "))
    print(n1+n2)
# add()

def mult(num1, num2):
        #переменный, переменный
    print(num1*num2)
# mult(10,10)
def welcome(name:str = "Geeks")-> str:
    "атын мн чакырат"
    print("Welcome",name)
    print("Кандайсын",name)
# welcome("Elaman")
welcome()
