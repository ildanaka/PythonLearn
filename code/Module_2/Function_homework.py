#homework
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        List_1 = []
        matrix.append(List_1)
        for j in range(m):
            List_1.append(value)
    return matrix


n = 3
m = 5
value = 42
result1 = get_matrix(n,m, value)
print(result1)