    #hw1
import random

def write_random_to_file(lst):
    # Выбираем случайный элемент из списка
    random_element = random.choice(lst)

    # Записываем результат в файл
    with open('output2.txt', 'w') as f:
        f.write(random_element)
    return random_element

language = ["Python", "Java", "Kotlin", "JavaScript", "C#", "RUBY"]
random_language = write_random_to_file(language)
print(f"Случайный язык программирования: {random_language}")


    #hw2
# text = """
# Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
# Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
# when an unknown printer took a galley of type and scrambled it to make a type
# specimen book. It has survived not only five centuries, but also the leap into
# electronic typesetting, remaining essentially unchanged. It was popularized in
# the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
# and more recently with desktop publishing software like Aldus PageMaker including 
# versions of Lorem Ipsum."""
# with open('text.txt', 'w') as file: #1-й метод
#     file.write(text)

# text = open('text.txt','w')#2-й метод
# text.write("print(""Lorem Ipsum is simply dummy text of the printing and typesetting industry.\n Lorem Ipsum has been the industrys standard dummy text ever since the 1500s,\n when an unknown printer took a galley of type and scrambled it to make a type\n specimen book. It has survived not only five centuries, but also the leap into\n electronic typesetting, remaining essentially unchanged. It was popularized in\n the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,\n and more recently with desktop publishing software like Aldus PageMaker including\n versions of Lorem Ipsum."")")
# text.close()
