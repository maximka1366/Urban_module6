def calculate_structure_sum(structure):
    summa = 0
    if isinstance(structure, str):
        summa += len(structure)
    elif isinstance(structure, (int, float)):
        summa += structure
    elif isinstance(structure, dict):
        for i, j in structure.items():
            summa += calculate_structure_sum(i)
            summa += calculate_structure_sum(j)
    elif isinstance(structure, (list, tuple, set)):
        for i in structure:
            summa += calculate_structure_sum(i)
    return summa


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

res = calculate_structure_sum(data_structure)
print(res)