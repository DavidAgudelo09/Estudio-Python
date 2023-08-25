# Escribe un programa en Python que permita al usuario 
# ingresar un año y luego determine y muestre si ese año es bisiesto o no.
def es_bisiesto(anno): # Definimos una función para determinar si un año es bisiesto o no
    # Un año es bisiesto si cumple con una de estas dos condiciones:
    # 1. Es divisible por 4 pero no por 100, o
    # 2. Es divisible por 400.
    if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
        return True # Si cumple alguna de las condiciones, es bisiesto.
    else:
        return False # Si no cumple ninguna condición, no es bisiesto.
try:
    #Pedimos al usuario que ingre un año
    year = int(input("Ingrese un año: "))
    # Llamamos a la función es_bisiesto para verificar si el año es bisiesto
    if es_bisiesto(year):
        print(f"{year} es un año bisiesto.")
    else:
        print(f"{year} no es un año bisiesto.")
except ValueError:
    print("Por favor, ingrese un año valido.")