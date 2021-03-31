#Otro tipo de dato para definir keys and values

cart = {
    "name" : "book",
    "quantity" : 4,
    "price" : 2.50
}

user = {
    "frist_name":"Ryan",
    "last_name":"Ray"
}

print(type(cart))

#print(dir(cart))
print(cart.keys()) #Muestra los keys
print(cart.values()) #Muestra los values
print(user.items()) #Muestra los keys con sus respectivos values
print("")
print(cart.clear()) #Limpia los elementos
print("")
# del cart
# print(cart) #Elimina toda la lista en sí

products = [
    {"name": "book", "price":100.99},
    {"name": "celphone", "price":float(68.00)}
]

print(products)
