def CreateList():
    collection_size = int(input('Введите размер коллекции '))
    list_ = []
    i = 0
    while i < collection_size:
        list_.append(int(input('Введите элемент [' + str(i) + ']: ')))
        i += 1
    return list_

def PrintWithDescription(description, body):
    print(str(description) + ':' + str(body))
