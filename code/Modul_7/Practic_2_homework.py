import io
from pprint import pprint

def custom_write(file_name, strings):
    strings_positions = {}
    i = 0
    with open(file_name, 'w', encoding='utf-8') as file:
        for string in (strings):
            # Получаем текущую позицию указателя в файле перед записью строки
            byte_position = file.tell()

            # Записываем строку в файл
            file.write(string + '\n')

            # Сохраняем номер строки, позицию и саму строку в словарь
            strings_positions[(i + 1, byte_position)] = string
            i += 1

    return strings_positions


# Пример использования функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
