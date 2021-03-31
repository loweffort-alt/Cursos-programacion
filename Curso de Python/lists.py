#Por hacer una analogía, lists = teoría de conjuntos
#Creas listas o conjuntos de datos de todo tipo, inclusive una lista dentro de otra
demo_list = [1, 'hello', 5.4, False, [4.2, 'Alex']]
colors = ['rojo', 'azul', 'verde']
print(colors)
#Ordena, por defecto, de forma creciente
numbers_list = list({1,5,4,7,3,0})
print(numbers_list)
print("")
#Creas lista de números acotados e ignora el ultimo número
r = list(range(1,5))
print(r)
print("")
#Recordemos q usando dir podemos analizar nuestros datos 
#print(dir(colors)) 
print(len(colors))
print(len(demo_list))
print(colors[1])
print(colors[1][3]) #Aquí mando a llamar al dígito 3 del dato 1 de la lista colors
print(colors[-1])
# Si quieros saber si existe un dato o no dentro de la lista
print("green" in colors)
print("verde" in colors)
print("")
#Para reemplazar datos en las listas
colors[1]="blue"
print(colors)
print("")

#Método
print("--------")
#colors.append(['violet', 'yellow']) #Para agregar subconjuntos
colors.extend(['sky blue', 'brown']) #Para agregar nuevos datos
print(colors)
print("")
print("--------")
colors.insert(2, 'BLACK') #Para insertar en la posición dada
colors.insert(len(colors), 'orange') #Si quiero ponerlo al último
colors.insert(-1,'pink') 
print(colors)
print("")
print("----------")
colors.pop() #Se usa para remover el último dato
colors.pop(-2) #Remueves el de la posición dada
print(colors)
print("")
print("--------")
colors.remove("BLACK") #Remueve el dato específico
print(colors)
print("")
print("--------")
#Para orderar se necesitan mismo tipos de datos
colors.sort() #Ordena alfabéticamente
print(colors)
colors.sort(reverse=True)
print(colors)
print("")
print("-------------")
print(colors.index("rojo")) #Indica la posición del dato ingresado
print(colors.count("verde")) #Cuenta las veces q se repite un dato




