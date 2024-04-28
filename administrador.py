import csv
from unidecode import unidecode
import os

# Define los nombres de las columnas
column_names = ['tiempo', 'contrasena', 'contrasena zip']
tiempo_evaluacion = None
corte_evaluacion = None
contrasena_corte = None

datos_examen = [tiempo_evaluacion, corte_evaluacion, contrasena_corte]
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

def imprimir_csv(datos_examen):
    # Abre el archivo CSV en modo escritura
    with open('mi_archivo.csv', 'w', newline='') as csvfile:   

        writer = csv.writer(csvfile)

        # Escribe los encabezados en la primera fila
        writer.writerow(column_names)

        # Puedes agregar filas de datos aquí
        writer.writerow([datos_examen[0], datos_examen[1], datos_examen[2]])


def menu_administrador():
    borrar_pantalla()
    print('''Bienvenido al PROYECTO CLASSROOM DOCENTE, para iniciar primero inserte la contraseña''')
    contrasena_usuario = input_modificado()
    if validacion (2,contrasena_usuario,4,10):
        while True:
            print("MENU")
            print("Acontinuacion podra modificar los parametros de su evaluacion, tenga en cuenta que debe rellenar todos los parametros para su evaluacion presentados a continuacion y que deben ser rellenados correctamente o de lo contrario podria surgir fallos a la hora de la precentacion de la evaluacion")
            print('''
    1.- Duracion de la evalucion
    2.- Corte que precentaran los alumnos
    3.- Contraseña del corte que sera presentado por los alumno
    4.- Ver(en esta opcion podra ver todos los datos que a ingresado asta el momento)
    5.- Imprimir(genera el archivo csv que contiene los parametros para la evalucion)''')
            selecion_usuario= int(input_modificado())

            if selecion_usuario == 1:
                borrar_pantalla()
                print("Ingrese en minutos la duracion de la evalucion. Por ejemplo: 300")
                datos_examen[0] = input_modificado()

            elif selecion_usuario == 2:
                borrar_pantalla()
                print("ingrese cual de los 4 cortes presentaran los alumnos. Por ejemplo: 3")
                datos_examen[1] = input_modificado()

            elif selecion_usuario == 3:
                borrar_pantalla()
                print("Ingrese la contraseña del corte que presentaran sus alumnos. Por ejemplo: Asdrubal2767")
                datos_examen[2] = input_modificado()

            elif selecion_usuario == 4:
                borrar_pantalla()
                print(f"El tiempo de evaluación no está especificado." if datos_examen[0] is None else f"Duración de la evaluación: {datos_examen[0]}")
                print(f"El corte que precentaran los alumnos no esta especificado." if datos_examen[1] is None else f"Corte que precentaran los alumnos: {datos_examen[1]}")
                print(f"La contraseña del corte que sera presentado por los alumno no esta especificada." if datos_examen[2] is None else f"Contraseña del corte que sera presentado por los alumno: {datos_examen[2]}")

            elif selecion_usuario == 5:
                borrar_pantalla()
                imprimir_csv(datos_examen)

            else: print("Selecione una opcion valida")

    else: print("Contraseña incorrecta")



def main():

    menu_administrador()

if __name__ == "__main__":
     main()

#La función "main()" nos ayuda a hacer que cada una de las demás funciones se ejecute en el orden que deben y en la forma
#en la que deben hacerlo ya que "if __name__ == "__main__"" nos permite hacer seguir a las funciones el orden de ejecución
#pautado por el programador, activandose cuando el script se ejecuta como el programa principal
