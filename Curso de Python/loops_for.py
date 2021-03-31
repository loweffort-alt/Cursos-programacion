#Imaginemos q es una lista de datos
#Si quiero agregar nuevos datos podría escribir otro print con el último índice
foods = ["manzana", "pan", "arroz", 
"leche", "banana"]
print(foods[0])
print(foods[1])
print(foods[2])
print(foods[3])
print(foods[4])
# etc etc
print("")
print("-----------------------------------")
print("")
#Pero hay otra manera de agregar nuevos datos (que se vaya actualizando)
#Lo que hace for es ir revisando dato por dato 
tools = ["martillo", "taladro", "perforador", "goma", "cinta adhesiva", 
"regla", "esmeril", "destornillador", "clavos"] # Podemos leerlo como:
for cada_cosa in tools:                         # Por 'cada_cosa' en 'tools';    
    if cada_cosa == "taladro":                  # si 'cada_cosa' = 'taladro' entonces 
        print("Hora de hacer la compradura")    # imprime "hora de..." y sigue imprimiendo 'cada_cosa'
    if cada_cosa == "cinta adhesiva":           # si 'cada_cosa' = 'cinta adhesiva' entonces
        continue                                # ignora ese dato y continúa imprimiendo
    if cada_cosa == "esmeril":                  # si 'cada_cosa' = 'esmeril'
        break                                   # detén la impresión;
    print(cada_cosa)                            # imprime 'cada_cosa'
    
print("")
print("-----------------------------------")
print("")

for number in range(1, 10):       #También permite trabajar con rangos
    print(number)

print("")
print("-----------------------------------")
print("")

for letter in "hello world":
    print(letter)





