# Para operar con variables primero definimos sus valores
# Puedes escribir varios tipos de datos en una variable
# Puedes escribir varias variables en 1 línea:
name, wrongname = "aleX", "Alex"
print(name, wrongname)
print("≠")
print(name + wrongname)
print("")

# Puedes escribir en varias líneas
x = 50-10
y = 75/5
c = x+y
ecuacion = c
print(ecuacion)
print("")

# Conventions = Son convenciones para mejorar y homogeneizar 
# los distintos tipos de escritura de los programadores
book_name = "I Robot" #Snake Case
bookName = "Digital Fortress" #Camel Case
BookName = "Python for dummies" #Pascal Case

# Si quieres usar variables constantes, se usan Mayusculas
PI = 3.14159
MI_NOMBRE = "Alexit0 emozith0"

# Si hay 2 valores con la misma variable, Python usa la última variable asignada
nombre = "Alex"
nombre = "Darío"
print(name)