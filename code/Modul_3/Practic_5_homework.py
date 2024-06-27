# Рекурсивное умножение цифр

def get_multiplied_digits(namber):
    str_number = str(namber)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

# get_multiplied_digits(40203) -> 4 * get_multiplied_digits(203) -> 4 * 2 * get_multiplied_digits(3) -> 4 * 2 * 3

result = get_multiplied_digits(40203)
print(result)