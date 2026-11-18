list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
Ordenada = []
while len(list_num) > 0:
    min = list_num[0]
    for elem in list_num:
        if elem < min:
            min = elem
    Ordenada.append(min)
    list_num.remove(min)
print (Ordenada)



