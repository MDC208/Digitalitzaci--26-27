list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
unique_list = []
for x in list_num:
    esta = False
    for y in unique_list:
        if x == y:
            esta = True
    if esta == False:
        unique_list.append(x)
print(unique_list)


