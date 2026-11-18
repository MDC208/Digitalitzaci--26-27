list_num = [2, 7, 4, 5, -1, 8, 3, 9, 6, 1012]
min = None
max = None
for elem in list_num:
    if min is None or elem < min:
        min = elem
    if max is None or elem > max:
        max = elem
print(f"El valor mínim és: {min}")
print(f"El valor màxim és: {max}")