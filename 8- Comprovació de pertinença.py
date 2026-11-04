list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
input = int(input("Escriu un nombre de la llista:"))
if input in list_num:
    print("El nombre", input, "forma part de la llista.")
else:
    print("El nombre", input, "no forma part de la llista.")