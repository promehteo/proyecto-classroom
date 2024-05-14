import random
import string

def generar_usuario():
    usuario = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return usuario

def solicitar_contrasena():
    contrasena = input("Por favor ingresa una contraseña con al menos 8 caracteres, incluyendo letras, dígitos y caracteres especiales: ")
    return contrasena

nuevo_usuario = generar_usuario()
nueva_contrasena = solicitar_contrasena()

print("Nuevo usuario creado:", nuevo_usuario)
print("Contraseña ingresada:", nueva_contrasena)