import random
def Password():
    list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    list_2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    a = 1
    b = a + 1
    while a > 0:
        if a > 20:
            break
        for n in list_2:
            n = random.choice(list_2)
            if n % (a + b) == 0:
                print(n, ' - ', a , b)
        a += 1

Password()

