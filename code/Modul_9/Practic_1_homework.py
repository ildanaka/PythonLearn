int_list = [5, 7, 10, 5]



def apply_all_func(int_list, *functions):
    dict_ = {}
    for func in functions:
        name = func.__name__
        dict_[name] = func(int_list)
    return dict_


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
