# На вход программы подается 3 целых числа. Напишите программу, которая находит серединное значение из этих чисел

a = input('Введите число ')
b = input('Введите число ')
c = input('Введите число ')

if a > b and a < c:
    print(a)
elif a > c and a < b:
    print(a)
elif b < a and b > c:
    print(b)
elif b > a and b <c:
    print(b)
elif c > a and c < b:
    print(c)
elif c < a and c > b:
    print(c)
else:
    print('число не найдено')




