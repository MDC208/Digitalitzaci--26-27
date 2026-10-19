textdna =  "atggatcattta"
lletra = "c"
contador = 0
for i in textdna:
    if i == lletra:
        contador += 1
print("La lletra", lletra, "apareix", contador, "vegades en la cadena", textdna)