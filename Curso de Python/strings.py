# Podemos analizar nuestra variable (str en este caso)
myStr = "Hello World"
print(myStr)
# Usamos dir para saber lo q podemos hacer con la variable
# print(dir(myStr))
print("")
# print("se divide en propiedades '_algo_' y métodos 'algo'")
# print("")
print("Métodos:")
print(myStr)        #Normal
print(myStr.upper()) #Todo mayúsucula
print(myStr.lower()) #Todo minúscula
print(myStr.swapcase()) #Las minúsculas a mayúsculas y viceversa
print(myStr.capitalize()) #Sólo la primera letra en mayúscula
#Reemplaza la palabra seleccionada por otra
print(myStr.replace('Hello', 'Bye')) 
#Se puede ejecutar un método dentro de otro método
print(myStr.replace('World', 'Mundeishon').replace('Mundeishon', 'Worldeichon').upper())
print("")
#Cuenta las veces q aparece el caracter q quieras
print(myStr.count('l')) 
print(myStr.count(' ')) #También cuenta los espacios
print("")
# Verifica si empieza o termina con la palabra 
print(myStr.startswith('Hola'))
print(myStr.startswith('Hello'))
print(myStr.startswith('Hel'))
print("")
print(myStr.endswith('Mundo'))
print(myStr.endswith('ld'))
print("")
#Para dividir mi dato str en formato list
print(myStr.split()) # Por defecto lo separa por el espacio
print(myStr.split('o')) #Usa el caracter "o" como separador
print("")
#Para encontrar el índice de un caracter (empezando desde el 0)
print(str("Para saber el índice de la letra 'e' ="), myStr.find('e'))
print(myStr.find('d'))
print("")
#Para saber la cantidad de caracteres 
print(len(myStr))
print("")
#Para saber si es numérico o alfanumércio (números + letras)
print(myStr.isnumeric())
print(myStr.isalpha())
print("")
# Para seleccionar el caracter del índice especificado
print(myStr[8]) #Se usa corchetes
print(myStr[-5]) #Cuenta desde atrás si tiene -
#OJO: "ctrl + shift + p" abres el buscador

print("----------------------------------------------------------------")

#Tenemos varias maneras de concatenar un string
Nombre = "Alex"
print("My name is " + Nombre)
#La f dice q dentro de la oración hay una variable
print(f"Mi nombre es {Nombre}") #Entre llaves y de Python 3.6 hacia arriba
#Usando format
print("Me llamo {0}".format(Nombre))