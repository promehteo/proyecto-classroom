import opciones.administrador as administrador
import opciones.index as index

print("Bienvenido a MENU CLASSROOM, por favor selecione una opcion")
print("1.- alumno")
print("2.- profesor")
seleccion_usuario = administrador.input_modificado()

if seleccion_usuario == "1":
    index.ejecutar_mein_alumno()

elif seleccion_usuario == "2":
    administrador.ejecutar_mein_administrador()




