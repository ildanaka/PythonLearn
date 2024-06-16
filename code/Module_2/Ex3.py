def PrintCollection(description, collection):
    resultLine = description + ': '
    i = 0
    lenghtCollection = len(collection)
    while i < lenghtCollection:
        resultLine = resultLine + str(collection[i])
        if i < lenghtCollection - 1:
            resultLine = resultLine + ', '


        i = i + 1

    return print(resultLine)



#homework
numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
resultCollection = []

PrintCollection('Origin', numbers)

a = len(numbers)
i = 0
while i < a:
    currentNumber = numbers[i]
    if currentNumber > 0:
        resultCollection.append(currentNumber)
    elif currentNumber < 0:
        break
    i = i + 1

PrintCollection('Result Ildana task', resultCollection)



#homework
numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = len(numbers)
i = 0
while i < a:
    currentNumber = numbers[i]
    if currentNumber > 0:
        print(currentNumber)
    elif currentNumber < 0:
        break
    i = i + 1








