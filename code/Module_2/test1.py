def PrintWithDescription(description, message):
    print(str(description) + ':' + str(message))

# На вход программе подается натуральное число 𝑛. Напишите программу, которая выводит звездный треугольник в соответствии с примером.

# n = 3

# ***
# **
# *

def PrintStars(count):
    result_= str()
    for i in range(count):
        result_ += '*'
    print(result_)

PrintStars(5)


