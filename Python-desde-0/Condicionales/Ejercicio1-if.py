# Ejercicio 1 IF

n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese segundo numero: "))

if n1 % 2 == 0 and n2 % 2 == 0:
    print("Ambos son pares")
elif n1 % 2 == 0 and n2 % 2 != 0:
    print(f"{n1} es un numero par")
elif n1 % 2 != 0 and n2 % 2 == 0:
    print(f"{n2} es un numero par")
else:
    print("Los dos numeros son impares")