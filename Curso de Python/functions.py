# Podemos crear nuestras propias funciones
# Al igual q print(), dir(), type()
# def = defnition
def hello():
    print("Hello World")

hello()

def name(nombre="Random"):
    print("Bienvenido señor " + nombre + ", tenga buen día")
name("Alex")
name()

print("-----------------------------------")

def add(numberOne, numberTwo):
    return (numberOne + numberTwo)
print(add(564, 6))

print("")
print("-----------------------------------")
print("")

#Otra manera de crear funciones es:

add = lambda numberOne, numberTwo: numberOne + numberTwo

print(add(49, 62))


