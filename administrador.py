import csv
from unidecode import unidecode
import os

passwort = "empanada"

# Define los nombres de las columnas
column_names = ['tiempo', 'corte', 'contrasena','contrasena zip','correo','pregunta base','preguntas teoricas']
tiempo_evaluacion = None
corte_evaluacion = None
contrasena_corte = None
contrasena_zip = None
correo_zip = None
base_pregunta = None
preguntas_teoricas = []

datos_examen = [tiempo_evaluacion, corte_evaluacion, contrasena_corte, contrasena_zip, correo_zip, base_pregunta ,preguntas_teoricas]
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
        writer.writerow([datos_examen[0], datos_examen[1], datos_examen[2], datos_examen[3], datos_examen[4], datos_examen[5], datos_examen[6]])


def menu_administrador():
    borrar_pantalla()
    print('''Bienvenido al PROYECTO CLASSROOM DOCENTE, para iniciar primero inserte la contraseña''')
    contrasena_usuario = input_modificado()
    if contrasena_usuario == passwort:
        while True:
            print("MENU")
            print("Acontinuacion podra modificar los parametros de su evaluacion, tenga en cuenta que debe rellenar todos los parametros para su evaluacion presentados a continuacion y que deben ser rellenados correctamente o de lo contrario podria surgir fallos a la hora de la precentacion de la evaluacion")
            print('''
    1.- Duracion de la evalucion
    2.- Corte que precentaran los alumnos
    3.- Contraseña del corte que sera presentado por los alumno
    4.- Contraseña del zip que sera enviado al correo
    5.- Correo al que se enviara el zip
    6.- preguntas teoricas
    7.- Ver(en esta opcion podra ver todos los datos que a ingresado asta el momento)
    8.- Imprimir(genera el archivo csv que contiene los parametros para la evalucion)''')
            selecion_usuario= int(input_modificado())

            if selecion_usuario == 1:
                borrar_pantalla()
                print("Ingrese en minutos la duracion de la evalucion. Por ejemplo: 300")
                minutos = int(input_modificado())
                segundo_minutos = minutos * 60
                datos_examen[0] = segundo_minutos

            elif selecion_usuario == 2:
                borrar_pantalla()
                print("ingrese cual de los 4 cortes presentaran los alumnos. Por ejemplo: 3")
                datos_examen[1] = int(input_modificado())

            elif selecion_usuario == 3:
                borrar_pantalla()
                print("Ingrese la contraseña del corte que presentaran sus alumnos. Por ejemplo: Asdrubal2767")
                datos_examen[2] = input_modificado()

            ##

            elif selecion_usuario == 4:
                borrar_pantalla()
                print("Ingrese la contraseña del zip que se enviara a su correo. Por ejemplo: corte3matematicas")
                datos_examen[3] = input_modificado()

            elif selecion_usuario == 5:
                borrar_pantalla()
                print("Ingrese el correo al cual se enviara el zip. Por ejemplo: profealex9@gmail.com")
                datos_examen[4] = input_modificado()

            elif selecion_usuario == 6:
                borrar_pantalla()
                print("Selecione cual de las preguntas teoricas va a modificar")
                print("1.-Pregunta 1")
                print("2.-Pregunta 2")
                print("3.-Pregunta 3")
                print("4.-Pregunta 4")
                pregunta_modificar = input_modificado()

                if int(pregunta_modificar) == 1:
                    print("Pregunta 1")
                    print("Ingrese la pregunta")
                    datos_examen[5] = input_modificado()
                    print("ingrese la opcion 1")
                    teoria_pregunta1 = input_modificado()
                    datos_examen[6].append(teoria_pregunta1)
                    print("ingrese la opcion 2")
                    teoria_pregunta2 = input_modificado()
                    datos_examen[6].append(teoria_pregunta2)
                    print("ingrese la opcion 3")
                    teoria_pregunta3 = input_modificado()
                    datos_examen[6].append(teoria_pregunta3)
                    print("ingrese la opcion 4")
                    teoria_pregunta4 = input_modificado()
                    datos_examen[6].append(teoria_pregunta4)

                elif pregunta_modificar == 2:
                    print("Pregunta 2")
                    print("Ingrese la pregunta")
                elif pregunta_modificar == 3:
                    print("Pregunta 3")
                    print("Ingrese la pregunta")
                elif pregunta_modificar == 4:
                    print("Pregunta 4")
                    print("Ingrese la pregunta")


            elif selecion_usuario == 7:
                borrar_pantalla()
                imprimir_preguntas_teoricas = datos_examen[6]
                print(f"El tiempo de evaluación no está especificado." if datos_examen[0] is None else f"Duración de la evaluación: {datos_examen[0] / 60} minutos")
                print(f"El corte que precentaran los alumnos no esta especificado." if datos_examen[1] is None else f"Corte que precentaran los alumnos: {datos_examen[1]}")
                print(f"La contraseña del corte que sera presentado por los alumno no esta especificada." if datos_examen[2] is None else f"Contraseña del corte que sera presentado por los alumno: {datos_examen[2]}")
                print(f"La contraseña del zip no esta especificada." if datos_examen[3] is None else f"Contraseña del zip: {datos_examen[3]}")
                print(f"El correo al cual se enviara el zip no esta especificado." if datos_examen[4] is None else f"Correo al que se enviara el zip: {datos_examen[4]}")
                print(f"Preguntas teoricas: {imprimir_preguntas_teoricas[0]}, {imprimir_preguntas_teoricas[1]}, {imprimir_preguntas_teoricas[2]}, {imprimir_preguntas_teoricas[3]}")

            elif selecion_usuario == 8:
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
