# Podemos usar código ya escrito con ayuda de los módulos
# Al desarrollar una app, podemos usar módulos de 3 fuentes:
# módulos propios
# módulos de terceros
# módulos de la biblioteca de python (módulos preconstruídos)

# Para usar módulos de python:
import datetime #en este ejemplo, sirve para mostrar la hora de tu escritorio

# Podemos buscar en google los módulos q hay en Python
# También podemos usar https://pypi.org/ para buscar nuevos módulos

# Podemos ver la documentación del módulo si lo escribimos en google (ej. buscar: 'python datetime')
# La documentación te muestra qué puedes hacer con ése módulo (usas ctrl+f para abrir un buscador en google)
print(datetime.date.today()) # muestra la fecha de hoy
# Se lee: "desde 'datetime' quiero usar su módulo llamado 'timedelta'"
print(datetime.timedelta(minutes=70))   # convierte los minutos a horas y minutos
print("")   
print("---------------------------")
print("")
# Otra manera de importar es:
from datetime import timedelta, date
print(date.today())
print("")   
print("---------------------------")
print("")
#Importaré el módulo fmath.py que creé 
import fmath
fmath.add(2, 7)
fmath.subtract(9, 2)
print("")   
print("---------------------------")
print("")
#Acabo de actualizar el pip y bajar el módulo colorama
from colorama import Fore, Style, init #Sabemos los nombres revisando la documentación.
init(convert=True)
print(Fore.RED + "Hello World")

#Hay muchos módulos útiles, como Flask, que es un framework para cerar aplicaciones web.
#Otro módulo útil es llamado 'django'
#También, 'tkinter' si quieres diseñar interfaces gráficas de usuario en el escritorio. (ya viene pre instalado con python)








