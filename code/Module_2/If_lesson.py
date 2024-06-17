#homework

first = input()
second = input()
third = input()
if first == second and third:
    print('3')
elif first == second or third:
    print('2')
else:
    print('0')



# Условный оператор. Как работает оператор if

name = input('Введите ваше имя ')
if name == 'Urban':
    print('Здравствуйте, администратор')
if name == 'Ildana':
    print('Здравствуйте, студент')
else:
    print('Привет, ', name)

 #Fizz, Buzz, FizzBuzz. Число должно делиться на 3, на 5, или на 3 и 5 одновременно
# or - and
# самое маловероятное и сложное условие ставим вначало, чтобы после него компьютер больше не проверял следующие условия - для этого ставим команду elif вместо if

number = int(input('Введите число '))
if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print('Число не подходит')



# Цикл While

while True:
    number = int(input('введите число: '))
    if number % 2 == 0:
        print('число четное')
        continue
    else:
        print('число нечетное')
    break

print('цикл окончен')