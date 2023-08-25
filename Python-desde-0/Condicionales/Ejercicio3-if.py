# Escribe un programa en Python que solicite al usuario
# ingresar su peso en kilogramos y su altura en metros, 
# y luego calcule y muestre su Índice de Masa Corporal (IMC).
kg = float(input("Por favor digite su peso kg: "))
al = float(input("Por favor digite su altura mt: "))
IMC = kg / (al**2)
if IMC < 18.5:
    print("Te encuentras dentro del rango de peso insuficiente")
elif IMC > 18.5 and IMC < 24.9:
    print("Te encuentras dentro del rango de peso normal o saludable")
elif IMC > 25.0 and IMC < 29.9:
    print("Te encuentras dentro del rango de sobre peso")
elif IMC > 30.0:
    print("Te encuentras dentro del rango de obesidad")
else:
    print("No he identificado tu rango")
print(f"Su peso {kg} y su altura {al} tiene un índice de masa corporal de: {IMC:.2f}")