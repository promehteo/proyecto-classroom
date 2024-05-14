import opciones.administrador as administrador
import opciones.index as index

index.borrar_pantalla()

print("Bienvenido a MENU CLASSROOM, por favor selecione una opcion")
print("1.- alumno")
print("2.- profesor")

def menu():
        
    while True:

        seleccion_usuario = administrador.input_modificado()

        if seleccion_usuario == "1":
            index.ejecutar_mein_alumno()
            break

        elif seleccion_usuario == "2":
            administrador.ejecutar_mein_administrador()
            break

        else:
            print("Por favor selecione una opcion valida")

def main():
    menu()

if __name__ == "__main__":
    main()

print("Gracias por usar nuestro codigo")


