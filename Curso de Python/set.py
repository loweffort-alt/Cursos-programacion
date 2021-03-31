#Definimos un conjunto de datos desordenada y sin índices

colors = {'red', 'black', 'white'}
print(type(colors))
print("")
print('red' in colors)
print("")
# Apriori, pensarías q lo agregaría al final, pero lo agrega al inicio por q no tiene índices
colors.add('violet')
print(colors)
colors.remove('black')
print(colors)
print("")
colors.clear()
print(colors)
print("")
del colors
print(colors)


