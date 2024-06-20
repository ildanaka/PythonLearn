from LoopCreator import CreateList
myList = CreateList()

print(myList)
len = len(myList)

#Сортировка путызьком


for j in range(len):
    for i in range(len - 1):
        if i < len/2:                  #если i меньше середины длины списка, то пропустить
            continue
        a = myList[i]
        b = myList[i+1]
        if a > b:
            myList[i] = b
            myList[i+1] = a
print(myList)


'''
for j in range(len):
    for i in range(len - 1):
        if int(myList[i]) > int(myList[i + 1]):
            a = myList[i]
            myList[i] = myList[i + 1]
            myList[i+1] = a
print(myList)
'''




