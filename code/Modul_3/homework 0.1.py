call = 0
def count_calls():
    global call
    call += 1
    print('Количество вызовов функций ', call)

def string_info(string):
    tuple_ = (len(string), string.upper(), string.lower())
    count_calls()
    return tuple_

def is_contains(string,list_):
    for item in list_:
        new_list = []
        new_list.append(item.lower())
    count_calls()
    if string.lower() in new_list:
         return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
count_calls()
