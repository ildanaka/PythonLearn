sum_result = 0

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(collection):
    global sum_result
    if isinstance(collection, list):
        for i in collection:
            calculate_structure_sum(i)
    if isinstance(collection, dict):
        for key, value in collection.items():
            calculate_structure_sum(key)
            calculate_structure_sum(value)
    if isinstance(collection, tuple):
        for i in collection:
            calculate_structure_sum(i)
    if isinstance(collection, set):
        for i in collection:
            calculate_structure_sum(i)

    if isinstance(collection, str):
        sum_result += len(collection)
    if isinstance(collection, int):
        sum_result += collection

calculate_structure_sum(data_structure)
print("Result sum: ", sum_result)

