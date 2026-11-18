def insertion_sort(llista):
    for i in range(1, len(llista)):
        clau = llista[i]
        j = i - 1
        while j >= 0 and llista[j] > clau:
            llista[j + 1] = llista[j]
            j -= 1
        llista[j + 1] = clau

list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
insertion_sort(list_num)
print(list_num)