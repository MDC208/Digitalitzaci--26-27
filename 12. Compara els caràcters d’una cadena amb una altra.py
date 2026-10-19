text =  "Hello World"
text2 = "Hola mon!!!"
nomDeLletresIguals = 0
for i in range(len(text)):
    if text[i] == text2[i]:
        print ("coincideixen les lletrres:", text[i])
        nomDeLletresIguals += 1
        print("El nombre de lletres que coincideixen és:", nomDeLletresIguals)