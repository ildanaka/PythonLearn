collection_size = int(input('Введите размер коллекции '))
list_ = []
i = 0;
while i < collection_size:
    list_.append(input('Введите элемент [' + str(i) + ']: '))
    i += 1

result = ''
for j in range(collection_size):
    if j < (collection_size - 1):
        result += str(list_[j]) + ', '
    else:
        result += str(list_[j])
print('Результирующий список ', result)