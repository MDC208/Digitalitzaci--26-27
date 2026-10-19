text =  "hola"
fraseInv = ""
for i in range(len(text)-1, -1, -1):
    fraseInv += text[i]
print(fraseInv)

fraseInv = ""

for i in range(0, len(text)):
    fraseInv = text[i] + fraseInv
print(fraseInv)

