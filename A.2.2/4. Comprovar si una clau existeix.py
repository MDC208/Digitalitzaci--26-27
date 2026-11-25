capital_pais = {"Espanya": "Madrid", "França": "París", "Italia": "Roma"}
pais = input("Introdueix un país: ")
# a)
if pais in capital_pais.keys():
    print("La capital de " ,pais, " és " ,capital_pais[pais], ".")
else:
    print("No tinc aquest país.")

# b)
capital=capital_pais.get(pais, "No tinc aquest país.")
if capital!="No tinc aquest país.":
    print("La capital de " ,pais, " és " ,capital, ".")