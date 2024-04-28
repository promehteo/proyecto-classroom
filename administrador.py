import csv
from unidecode import unidecode
import os

# Define los nombres de las columnas
column_names = ['tiempo', 'contrasena', 'contrasena zip']

def borrar_pantalla():
    #La función define una variable llamada sistema_operativo para almacenar el nombre del sistema operativo actual
    sistema_operativo = os.name

    #Se utiliza una instrucción if para verificar el nombre del sistema operativo
    if sistema_operativo == 'posix':
        #Si el sistema operativo es POSIX (Linux, macOS), se ejecuta el comando clear para limpiar la pantalla
        os.system('clear')
    elif sistema_operativo == 'nt':
        #Si el sistema operativo es Windows, se ejecuta el comando cls para limpiar la pantalla
        os.system('cls')

def validacion (tipo,valor,min,max):
    valor_logitud = len(valor)
    #solo numeros
    if valor.isdigit():
        tipo = 1
    #solo numeros con letras
    elif valor.isalnum():
        tipo = 2
    #solo letras
    elif valor.isalpha():
        tipo = 3
    else: print('Ha ingresado un valor incorrecto')

    if valor_logitud > min and valor_logitud < max:
        return tipo

def input_modificado ():

    valor = input("").lower()
    valor = unidecode(valor)
    return valor

def menu_administrador():
    borrar_pantalla()
    print('''Bienvenido al PROYECTO CLASSROOM DOCENTE, para iniciar primero inserte la contraseña''')
    contraseña_usuario = input_modificado()
    if validacion (2,contraseña_usuario,4,10):
        print("bienvenido, aqui podra asignar las pautas para su examen")
        print("limite de tiempo")
        limite_tiempo = input_modificado()
        print("contraseña")
        contraseña_corte = input_modificado()
        print("contraseña del zip?")
        contraseña_zip = input_modificado()

        # Abre el archivo CSV en modo escritura
        with open('mi_archivo.csv', 'w', newline='') as csvfile:

            

            writer = csv.writer(csvfile)

            # Escribe los encabezados en la primera fila
            writer.writerow(column_names)

            # Puedes agregar filas de datos aquí
            writer.writerow([limite_tiempo, contraseña_corte, contraseña_zip])


def main():

    menu_administrador()

if __name__ == "__main__":
     main()

#La función "main()" nos ayuda a hacer que cada una de las demás funciones se ejecute en el orden que deben y en la forma
#en la que deben hacerlo ya que "if __name__ == "__main__"" nos permite hacer seguir a las funciones el orden de ejecución
#pautado por el programador, activandose cuando el script se ejecuta como el programa principal
