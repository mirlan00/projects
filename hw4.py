    #hw1
# bigcompany = ["Meta", "Amazon AWS", "Starlink", "Google","BMW", "LEXUS", "TOYOTA", "BYD","ALIBABA","XIOMI","SAMSUNG","APPLE","Alphabet","Volkswagen","Walmart"]
# print(bigcompany[2:7])

    #hw2
# numbers = ["5","4","3","2","1"]
# print(numbers[::-1])
    #2чи методу
# numbers.reverse()
# print(numbers)
    #hw3
# a = [1, 3, 4, 5] 
# b = [4, 5, 6, 7]
# a.extend(b) # б ны а га кошуп атат
# result =list(set(a))# set > {} ушундай квадрат чыгаргандыктан list менен аны озгортовуз
# print(result)
    #hw4
# numbers = [5,4,3,2,1]
# x = min(numbers)
# print(x)
    #hw5
# numbers = [5,4,3,2,1]
# # # numbers.remove(5,4,3,2,1)
# # #del numbers [0:5]
# numbers.clear()
# print(numbers)

    #hw6
# numbers = [5,4,3,2,1]
# print(sum(numbers))

    #hw7
# numbers = [5,4,3,2,1]
# print(sum(numbers)/len(numbers))

    #hw8
# music = ["мен дагы бай болом","Let It Be","Someone Like You","Imagine","gummy-you-are-my-everything","No Way","greedy","STAY. STAY","drivers license","Levitating"]
# print(music)
# music[3],music[7] = music[7],music[3]#индекс аркылуу месталын озгортуу
# print(music)
#     #hw9
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
# 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 
# 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 
# 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 
# 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 
# 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 
# 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 
# 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 
# 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 
# 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 
# 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 
# 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 
# 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 
# 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 
# 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
# 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 
# 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 
# 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 110, 111, 112, 113, 114, 115, 
# 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 
# 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145,146, 147, 
# 148, 149, 150, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 
# 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 
# 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 
# 295, 296, 297, 298, 299, 110]
# print(numbers.count(110))

    #h10
# it_company = ("Google", "Amazon", "Microsoft")
# it_company1 = list(it_company)
# print(it_company1)
# it_company1.append("Tesla")
# print(it_company1)
# it_company = tuple(it_company1)
# print(it_company)

    #hw11

# it_company = ["Google", "Amazon", "Microsoft"]
# print(it_company.index("Amazon"))

    #hw12

# it_company = ["Google", "Amazon", "Microsoft"]
# it_company[0] = "Apple"
# print(it_company)

    #hw13

# it_company = ["Apple", "Amazon", "Microsoft"]
# print(it_company[0:3])

    #hw14
# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language', 
# 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 
# 'the', 'clean', 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 
# 'Whet', 'your', 'appetite', 'with', 'our', 'Python', '3', 'overview')
# print(text_tuple.count("Python"))

    #дп зд
password1 = input("Write a password: ")
lst = []

if len(password1) >= 8:
    if "123" not in password1:
        password2 = input("Write the password again: ")
        if password1 == password2:
            lst.append(password1)
            print("OK")
            print("Пароль создан!")
        else:
            print("Различаются")
    else:
        print("Простой пароль!")
else:
    print("Короткий пароль!")
print(lst)