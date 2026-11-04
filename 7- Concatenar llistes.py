list_num = [2, 7, 4, 5, 1]
list_num2 = [ 8, 3, 9, 6, 10]
llista_concatenada = []
for x in list_num and list_num2:
    esta = False
    for y in llista_concatenada:
        if x == y:
            esta = True
    if esta == False:
        llista_concatenada.append(x)
print(llista_concatenada)
    