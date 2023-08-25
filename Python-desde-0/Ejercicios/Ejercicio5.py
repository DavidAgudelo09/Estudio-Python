# Escribe un programa en Python que permita al usuario 
# ingresar una cantidad en dólares y luego calcule y 
# muestre su equivalente en euros utilizando una tasa de cambio predefinida.
dolar = float(input("Digite la cantidad de dolares que desea cambiar a euros: "))
euro = float(0.93)
tasa = dolar * euro
print(f"La cantidad de {dolar} dolares, equivale a {tasa} euros")