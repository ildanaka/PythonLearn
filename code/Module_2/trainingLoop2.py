from LoopCreator import PrintWithDescription
from LoopCreator import CreateList
list_ = CreateList()

PrintWithDescription('Исходная коллекция', list_)

'''
a = len(_list)
for i in range(len(_list)):
    a -= 1
    print(_list[a])
'''


list_2 = []
a = len(list_)
while a > 0:
    a -= 1
    list_2 += list_[a]
PrintWithDescription('Развернутая коллекция', list_2)



