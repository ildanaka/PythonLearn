def print_params(a=1, b='string', c=True):
    print(a, b, c)

print_params()
print_params(3, 2, 3)
print_params(b=25)
print_params(c = [1, 2, 3])

values_list = [2, True, 'string']
values_dict = {'a': 1, 'b': 'string', 'c': 3}
print_params(*values_list)
print_params(**values_dict)

values_list2 = [True, 'string']
print_params(*values_list2, 42)
