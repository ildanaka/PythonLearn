call = 0
def count_calls(call):
    print('Количество вызовов функций ', call)

def string_info(string):
    global call
    call += 1
    tuple_ = (len(string), string.upper(), string.lower())
    return tuple_

def is_contains(string,list_):
    global call
    call += 1
    for item in list_:
        new_list = []
        new_list.append(item.lower())
    if string.lower() in new_list:
         return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
count_calls(call)
