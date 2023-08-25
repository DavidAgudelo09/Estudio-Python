# Escribe un programa en Python que perm ita al usuario 
# ingresar una cantidad de minutos y luego calcule y 
# muestre la equivalencia en horas y minutos.
minutos = int(input("Ingresa la cantidad de minutos: "))
horas = minutos // 60
minutos_restantes = minutos % 60
print(f"{minutos} minutos equivalen a {horas} horas y {minutos_restantes} minutos.")