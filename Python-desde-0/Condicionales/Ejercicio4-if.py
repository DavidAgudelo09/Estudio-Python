# Escribe un programa en Python que solicite al usuario 
# ingresar un número entero y luego determine y muestre si el número ingresado es par o impar.
num = int(input("Digite un numero: "))
if num % 2 == 0:
    print("El numero es PAR")
else:
    print("El numero es IMPAR")