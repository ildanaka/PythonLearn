def PrintStars(count):
    result_= str()
    for i in range(count):
        result_ += '*'
    print(result_)


n = int(input('введите число: '))
for i in range(n):
    PrintStars(n-i)
