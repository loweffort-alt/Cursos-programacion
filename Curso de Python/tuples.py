# Nos permite definir tipos de datos inmutables
# Son más rápidos q las listas y sirve para hacer más eficiente el código
x = (1, 2, 3, 4, 5, 6)
print(x)
#Se usa la función tuples
y = tuple(((1,2,3),2,4))
print(y)
print("")
print("-----------------")
print("")
print(dir(x))
print("")
print("-----------------")
print("")
#Si sólo consideramos un dato, el sistema lo entiende como int
#Para q sea considerado tupla tenemos q ponerle una ,
print(type((1,)))
print(tuple((1,2,3,4,5)))
print("")
print("-----------------")
print("")
#Para acceder a un dato específico colocamos su posición entre llaves
# print(x[3])
# del y #Sirve para eliminar la tupla
# print(y)

locations = {
    (35.153, 45.144):"Tokyo",
    (12.251, 75.142):"Lima"
}
print(locations)

