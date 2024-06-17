# Функции:
# - обычные
# - принимающие
# - возвращающие
# - анонимные

def say_hello():
    print('Hello')

say_hello()

# Принимающие функции: те функции, у которых в момент создания определяем какие-то значения,
# а значит в момент вызова мы их тоже должны будем передать

def say_hello(name):
    print('Hello', name)

say_hello(input('введите имя '))
say_hello('Denis')

# Возвращающая функция. В этом примере лотерея с рандомным выбором. Обращаемся к библиотеке random, метод choice
# выбирает случайный элемент из списка

import random
def lottery():
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win = random.choice(tickets)
    return win

win = lottery()               # создали переменную и созранили в нее значение вызова функции
print(win)

# Функции могут быть одновременно возвращающими и принимающими
import random
def lottery(mon,thue):
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(mon,thue)
    return win1, win2

win1, win2 = lottery('mon', 'thue')
print(win1, win2)

#можем задавать значение по умолчанию:
def test(a=2, b=True):
    print(a, b)

test(False, 'ok')

#списки

def test(a=2, b=True):
    print(a, b)

test([1,2])





