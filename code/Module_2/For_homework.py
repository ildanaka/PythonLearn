#homework Найти простые числа.

# Дано натуральное число 𝑛. Напишите программу, которая печатает численный треугольник с высотой равной n, в соответствии с примером:

# n =  6

#1
#2 3
#4 5 6
#7 8 9 10
#11 12 13 14 15
#16 17 18 19 20 21


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    is_prime = True
    for j in range(2,i):
        if i % j ==0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)

