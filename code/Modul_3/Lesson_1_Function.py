# Способы вызова функции по умолчанию:
def print_params(a=1, b=2, c=3):
    print(a, b, c)

print_params()

# ---------------------------
# 2
def print_params(a, b, c):
    print(a, b, c)

print_params(1, 2, 3)                # параметры указаны позиционно

# ----------------------------
# 3
def print_params(a=1, b=2, c=3):
    print(a, b, c)

print_params(a=3, b=5, c=9)                   # параметры указаны явно

# ----------------------------
# 4
def print_params(a=1, b=2, c=3):
    print(a, b, c)

print_params(c = 'string')                   # именованный параметр

# ----------------------------
# 5
def print_params(a, b, c):
    print(a, b, c)
    print(a + b)

print_params(3, 2, 3)

# ----------------------------
# 6
def print_params(a,*, b, c):                # * - обозначили, что после * параметры будут передаваться явно
    print(a, b, c)

print_params(3, b=2, c=3)                # первый параметр передался позиционно, остальные нужно указать явно, потому что ставили *


print('richiest'.upper)
