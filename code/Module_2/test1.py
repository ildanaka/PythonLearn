def PrintWithDescription(description, message):
    print(str(description) + ':' + str(message))

def PrintStars(count):
    result_= str()
    for i in range(count):
        result_ += '*'
    print(result_)

PrintStars(5)


