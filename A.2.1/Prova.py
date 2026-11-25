Llista= [2,5,8]

# Com accedim als elements
print(Llista[0])
print(Llista[1])
print(Llista[2])

# Recorregut de la llista en un bucle for
for x in Llista:
    print(x)

for x in range(len(Llista)):
    print("posició:" , x, " contingut:", Llista[x] )

Llista.append(10) #afegim un element al final de la llista
print(Llista)
Llista.insert(1,300)
print(Llista)
# Eliminar elements
del Llista[2]
print(Llista)
# update element
Llista[1] = 100
print(Llista)