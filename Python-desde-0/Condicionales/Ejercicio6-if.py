# Escribe un programa en Python que solicite al usuario 
# ingresar una contraseña y luego determine si cumple con ciertos requisitos de validación.
def validar_contrasena(contrasena):
    # Requisitos mínimos
    longitud_minima = 8
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    
    # Verificar longitud mínima
    if len(contrasena) < longitud_minima:
        return False
    
    # Verificar otros requisitos
    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
        if caracter.islower():
            tiene_minuscula = True
        if caracter.isdigit():
            tiene_numero = True
    
    # Verificar si cumple con todos los requisitos
    if tiene_mayuscula and tiene_minuscula and tiene_numero:
        return True
    else:
        return False

# Solicitar contraseña al usuario
contrasena_usuario = input("Ingresa tu contraseña: ")

# Validar contraseña
if validar_contrasena(contrasena_usuario):
    print("Contraseña válida. ¡Bien hecho!")
else:
    print("La contraseña no cumple con los requisitos de validación.")