def selection_sort(llista):          
    n = len(llista)
    for i in range(n - 1):        
        pos_min = i                 
        for j in range(i + 1, n): 
            if llista[j] < llista[pos_min]:
                pos_min = j         
        llista[i], llista[pos_min] = llista[pos_min], llista[i]   
list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
selection_sort(list_num)
print(list_num)