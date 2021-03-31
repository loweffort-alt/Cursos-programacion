#Hacemos las operaciones básicas
# print(5+7)
# print(8*2.4)
# print(10/3)
# print(5/9)
# print(10//3, "= cociente") #Si queremos el cociente de una división
# print(10%3, "= residuo") #Si queremos el residuo de una división
# print("")
# #Se respeta las reglas aritméticas
# print(5+8*3/6) #Si hay una división, da un float
# print(4*2+5) #No división = int
# print("")
# print("--------------------------------------------------------------------")
#Para hacer formularios hacemos lo siguiente:

#Sirve para tomar datos de entrada de la consola
# name = input("Nombre:")
# lastname = input("Apellidos:")
# fullname = str(f"{name}"+f" {lastname}")
# age = input("Edad:")
# password = age+name+lastname
# new_age = int(age) + 10
# posibility = [password]
# print("La muerte de {} será dentro de 10 años, osea, cuando tenga {}".format(fullname,new_age))
# print("y sólo podrá salvarse si la contraseña es verdadera")
# clave = input("Contraseña:")
# if (f"{clave}" in posibility) == True:
#     print("You are alive, Congrats!")
# else:
#    print("Haha you die >:)")

#Otra manera de hacerlo
name = input("Nombre:")
lastname = input("Apellidos:")
fullname = str(f"{name}"+f" {lastname}")
age = input("Edad:")
key = age+name+lastname
new_age = int(age) + 10
print("La muerte de {} será dentro de 10 años, osea, cuando tenga {}".format(fullname,new_age))
print("y sólo podrá salvarse si la contraseña es verdadera")
password = input("Contraseña:")
if password == key:
    print("Congratulations brooOoOther!! you are alived")
else:
    print("You don't deserved you life, DIE! >:)")


