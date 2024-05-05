import csv
from unidecode import unidecode
import os

passwort = "empanada"

# Define los nombres de las columnas
column_names = ['tiempo', 'contrasena','contrasena zip','correo','preguntas teoricas']
tiempo_evaluacion = None
contrasena_corte = None
contrasena_zip = None
correo_zip = None
base_pregunta = None
preguntas_teoricas = []

datos_examen = [tiempo_evaluacion, contrasena_corte, contrasena_zip, correo_zip ,preguntas_teoricas]
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

def input_modificado(prompt="", allowed_characters=""):
    """Captures user input, normalizes it, and validates against allowed characters.

    Args:
        prompt (str, optional): The prompt message to display to the user. Defaults to an empty string.
        allowed_characters (str, optional): A string containing the allowed characters for input. Defaults to an empty string (no restrictions).

    Returns:
        str: The normalized and validated user input.
    """

    while True:
        try:
            # Capture user input
            user_input = input(prompt).lower()

            # Normalize using unidecode
            normalized_input = unidecode(user_input)

            # Validate against allowed characters
            if allowed_characters:
                for char in normalized_input:
                    if char not in allowed_characters:
                        raise ValueError(f"Invalid character: '{char}'")

            # Return valid input
            return normalized_input

        except ValueError as e:
            print(f"Error: {e}")
            # Provide guidance to the user about allowed characters if applicable
            if allowed_characters:
                print(f"Allowed characters: {allowed_characters}")

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
    while True:
        contrasena_usuario = input_modificado()
        if contrasena_usuario.strip() == passwort:
            while True:
                borrar_pantalla()
                print("MENU")
                print("Acontinuacion podra modificar los parametros de su evaluacion, tenga en cuenta que debe rellenar todos los parametros para su evaluacion presentados a continuacion y que deben ser rellenados correctamente o de lo contrario podria surgir fallos a la hora de la precentacion de la evaluacion")
                print('''
        1.- Duracion de la evalucion
        2.- Contraseña del corte que sera presentado por los alumno
        3.- Contraseña del zip que sera enviado al correo
        4.- Correo al que se enviara el zip
        5.- Editar preguntas
        6.- Ver(en esta opcion podra ver todos los datos que a ingresado asta el momento)
        7.- Imprimir(genera el archivo csv que contiene los parametros para la evalucion)''')
                selecion_usuario= int(input_modificado())

                if selecion_usuario == 1:
                    borrar_pantalla()
                    print("Ingrese en minutos la duracion de la evalucion. Por ejemplo: 300")

                    while True:
                        minutos = input_modificado()
                        minutos_procesados = validacion(1,minutos,1,4)
                        segundo_minutos = int(minutos) * 60
                        datos_examen[0] = segundo_minutos

                        print(minutos_procesados)

                        if minutos_procesados:
                            print("El tiempo que a ingresado es de: ", datos_examen[0] / 60 ," minutos")
                            print("Esta seguro que de que esa sera la duracion para el examen? si/no")

                            while True:

                                respues_examen_usuario = input_modificado()

                                if respues_examen_usuario == "si":
                                    break
                                elif respues_examen_usuario == "no":
                                    print("Por favor reingrese el tiempo para el corte")
                                    break
                                else:
                                    print("por favor elija una opcion valida")

                            if respues_examen_usuario == "si":
                                break

                        else:
                            print("El dato que a ingresado es invalido, solo se perminten letras con minimo 1 y maximo 4 caracteres")

                elif selecion_usuario == 2:

                    borrar_pantalla()
                    print("Ingrese la contraseña del corte que presentaran sus alumnos. Por ejemplo: Asdrubal2767")

                    while True:
                        datos_examen[1] = input_modificado()

                        contrasena_procesada = validacion(2,datos_examen[1],1,10)

                        if contrasena_procesada:
                            print("La contraseña del corte que a ingresado es: ", datos_examen[1])
                            print("Esta seguro que de que esa sera la contraseña para el corte? si/no")

                            while True:

                                contrasena_examen_usuario = input_modificado()

                                if contrasena_examen_usuario == "si":
                                    break
                                elif contrasena_examen_usuario == "no":
                                    print("Por favor reingrese la contraseña del corte")
                                    break
                                else:
                                    print("por favor elija una opcion valida")

                            if  contrasena_examen_usuario == "si":
                                break

                        else:
                            print("El dato que a ingresado es invalido, solo se perminten letras y numeros con minimo 1 y maximo 10 caracteres")
                ##

                elif selecion_usuario == 3:
                        
                    borrar_pantalla()
                    print("Ingrese la contraseña del zip que se enviara a su correo. Por ejemplo: corte3matematicas")

                    while True:
                        datos_examen[2] = input_modificado()

                        procesada_contraseña_zip = validacion(2,datos_examen[2],1,10)

                        if procesada_contraseña_zip:
                            print("La contraseña del zip que a ingresado es: ", datos_examen[2])
                            print("Esta seguro que de que esa sera la contraseña del zip que contendra la evaluacion? si/no")

                            while True:

                                contrasena_zip_examen_usuario = input_modificado()

                                if contrasena_zip_examen_usuario == "si":
                                    break
                                elif contrasena_zip_examen_usuario == "no":
                                    print("Por favor reingrese la contraseña del zip")
                                    break
                                else:
                                    print("por favor elija una opcion valida")

                            if  contrasena_zip_examen_usuario == "si":
                                break

                        else:
                            print("El dato que a ingresado es invalido, solo se perminten letras y numeros con minimo 1 y maximo 10 caracteres")


                elif selecion_usuario == 4:

                    borrar_pantalla()
                    print("Ingrese el correo al cual se enviara el zip. Por ejemplo: profealex9@gmail.com")
                    
                    while True:
                        datos_examen[3] = input_modificado()

                        procesada_correo = validacion(2,datos_examen[3],1,10)

                        if procesada_correo :
                            print("El correo que a ingresado es: ",datos_examen[3])
                            print("Esta seguro que de que esa sera el correo al cual se enviara el zip que contiene la contraseña? si/no")


                            while True:
                                    
                                correo_examen_usuario = input_modificado()

                                if correo_examen_usuario == "si":
                                    break
                                elif correo_examen_usuario == "no":
                                    print("Por favor reingrese el correo al cual se enviara el zip")
                                    break
                                else:
                                    print("por favor elija una opcion valida")

                            if  contrasena_examen_usuario == "si":
                                break

                        else:
                            print("El dato que a ingresado es invalido, solo se perminten letras y numeros con minimo 1 y maximo 10 caracteres")


                elif selecion_usuario == 5:
                    borrar_pantalla()
                    while True:
                        print("Elija la acción que desea realizar:")
                        print("1.- Agregar nueva pregunta")
                        print("2.- Modificar pregunta existente")
                        print("3.- Volver al menú principal")

                        accion_pregunta = input_modificado()

                        if accion_pregunta == "1":
                            # Add new question logic
                            print("Seleccione el tipo de pregunta múltiple(1) o teórico/práctico(2): ")
                            tipo_pregunta = input_modificado()
                            if int(tipo_pregunta) == 1:
                                print("Ingrese el enunciado de la pregunta: ")
                                pregunta_enunciado = input_modificado()

                                opciones = []
                                while True:
                                    print("Ingrese una opción (presione Enter luego de escribir una opcion para guardarla o presione enter sin escribir nada cuando ya no quiera agregar más preguntas para finalizar): ")
                                    nueva_opcion = input_modificado()
                                    if nueva_opcion.strip():
                                        opciones.append(nueva_opcion)
                                    else:
                                        break

                                if len(opciones) < 2:
                                    print("Se necesitan al menos dos opciones para una pregunta de opción múltiple.")
                                    continue

                                print("Ingrese la opción correcta (copiela y peguela de nuevo aqui exactamente igual a como la escribió en las opciones): ")
                                respuesta_correcta = input_modificado()
                                if respuesta_correcta not in opciones:
                                    print("La opción correcta debe ser una de las opciones disponibles.")
                                    continue

                                print("Ingrese los puntos por responder correctamente: ")
                                puntos_respuesta_correcta = int(input_modificado())

                                # Add the question to the datos_examen list
                                datos_examen[4].append({
                                    "tipo": "múltiple",
                                    "enunciado": pregunta_enunciado,
                                    "opciones": opciones,
                                    "respuesta_correcta": respuesta_correcta,
                                    "puntos_respuesta_correcta": puntos_respuesta_correcta
                                })

                            elif int(tipo_pregunta) == 2:
                                print("Ingrese el enunciado de la pregunta: ")
                                pregunta_enunciado = input_modificado()
                                print("La pregunta se almacenará como una pregunta teórica/práctica sin opciones.")

                                # Add the question to the datos_examen list
                                datos_examen[4].append({
                                    "tipo": "teórico/práctico",
                                    "enunciado": pregunta_enunciado
                                })

                            imprimir_csv(datos_examen)

                            print("¿Desea agregar otra pregunta? si/no")
                            continuar_agregando_preguntas = input_modificado()


                        elif accion_pregunta == "2":
                            print("Selecione cual de las preguntas teoricas va a modificar")
                            print("1.-Pregunta 1")
                            print("2.-Pregunta 2")
                            print("3.-Pregunta 3")
                            print("4.-Pregunta 4")
                            pregunta_modificar = input_modificado()

                            if int(pregunta_modificar) == 1:
                                # Modificar pregunta 1
                                pregunta_1 = datos_examen[4][0]
                                if pregunta_1["tipo"] == "múltiple":
                                    # Modificar pregunta de opción múltiple
                                    print("Enunciado actual:", pregunta_1["enunciado"])
                                    print("Ingrese el nuevo enunciado (o presione Enter para mantener el actual): ")
                                    nuevo_enunciado = input_modificado()
                                    if nuevo_enunciado:
                                        pregunta_1["enunciado"] = nuevo_enunciado

                                    print("Opciones actuales:")
                                    for i, opcion in enumerate(pregunta_1["opciones"]):
                                        print(f"{i + 1}. {opcion}")

                                    print("Ingrese el número de la opción que desea modificar (o presione Enter para no modificar): ")
                                    opcion_modificar = input_modificado()
                                    if opcion_modificar:
                                        try:
                                            indice_opcion = int(opcion_modificar) - 1
                                            if 0 <= indice_opcion < len(pregunta_1["opciones"]):
                                                print("Ingrese la nueva opción: ")
                                                nueva_opcion = input_modificado()
                                                pregunta_1["opciones"][indice_opcion] = nueva_opcion
                                            else:
                                                print("Número de opción inválido.")
                                        except ValueError:
                                            print("El número de opción debe ser un número entero.")

                                    respuesta_correcta_actual = pregunta_1["respuesta_correcta"]
                                    print(f"Respuesta correcta actual: {respuesta_correcta_actual}.\nIngrese la nueva respuesta correcta (o presione Enter para mantener la actual): ")
                                    nueva_respuesta_correcta = input_modificado()
                                    if nueva_respuesta_correcta:
                                        if nueva_respuesta_correcta not in pregunta_1["opciones"]:
                                            print("La nueva respuesta correcta debe ser una de las opciones disponibles.")
                                        else:
                                            pregunta_1["respuesta_correcta"] = nueva_respuesta_correcta

                                    puntos_respuesta_correcta_actual = pregunta_1["puntos_respuesta_correcta"]
                                    try:
                                        print(f"Puntos por responder correctamente actuales: {puntos_respuesta_correcta_actual}.\nIngrese los nuevos puntos (o presione Enter para mantener los actuales): ")
                                        nuevos_puntos_respuesta_correcta = int(input_modificado())
                                        pregunta_1["puntos_respuesta_correcta"] = nuevos_puntos_respuesta_correcta
                                    except ValueError:
                                        print("El número de puntos debe ser un número entero.")

                                elif pregunta_1["tipo"] == "teórico/práctico":
                                # Modificar pregunta teórica/práctica
                                    print("Enunciado actual:", pregunta_1)
                        elif accion_pregunta == "3":
                            break
                        else:
                            print("Opción inválida. Intente nuevamente.")


                elif selecion_usuario == 6:
                    borrar_pantalla()
                    imprimir_preguntas_teoricas = datos_examen[4]
                    print(f"El tiempo de evaluación no está especificado." if datos_examen[0] is None else f"Duración de la evaluación: {datos_examen[0] / 60} minutos")
                    print(f"La contraseña del corte que sera presentado por los alumno no esta especificada." if datos_examen[1] is None else f"Contraseña del corte que sera presentado por los alumno: {datos_examen[1]}")
                    print(f"La contraseña del zip no esta especificada." if datos_examen[2] is None else f"Contraseña del zip: {datos_examen[2]}")
                    print(f"El correo al cual se enviara el zip no esta especificado." if datos_examen[3] is None else f"Correo al que se enviara el zip: {datos_examen[3]}")
                    print(f"Preguntas teoricas: {datos_examen[4]}")
                    input("Pulse enter para regresar al menu")

                elif selecion_usuario == 7:
                    borrar_pantalla()
                    imprimir_csv(datos_examen)
                    print("Archivo csv con los datos de la evaluacion impreso correctamente")
                    input("Pulse enter para regresar al menu")

                else: print("Selecione una opcion valida")

        else: 
            print("Contraseña incorrecta,por favor reingrese la contraseña")



def main():

    menu_administrador()

if __name__ == "__main__":
     main()

#La función "main()" nos ayuda a hacer que cada una de las demás funciones se ejecute en el orden que deben y en la forma
#en la que deben hacerlo ya que "if __name__ == "__main__"" nos permite hacer seguir a las funciones el orden de ejecución
#pautado por el programador, activandose cuando el script se ejecuta como el programa principal
