# Ejercicio 4

# Obtener el precio final que se tiene que pagar si se aplica el 36% de descuento del total de la compra.

precioinicial = float(input("Digite el total a pagar: "))

descuento = precioinicial * (36/100)

preciofinal = precioinicial - descuento

print(f"El precio con descuento seria de: {preciofinal:.2f}")