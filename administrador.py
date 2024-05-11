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

def validacion (valor,min,max):
    tipo = False
    valor_logitud = len(valor)

    #correo 
    if "@gmail.com" in valor or "@hotmail.com" in valor:
        tipo = 4
    #peromite todos los tipos de datos
    elif valor and not valor.isdigit() and not valor.isalnum() and not valor.isalpha():
        tipo = 5
    #solo numeros
    elif valor.isdigit():
        tipo = 1
    #solo numeros con letras
    elif valor.isalnum():
        tipo = 2
    #solo letras
    elif valor.isalpha():
        tipo = 3

    if valor_logitud >= min and valor_logitud <= max and tipo:
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
        writer.writerow([datos_examen[0], datos_examen[1], datos_examen[2], datos_examen[3], datos_examen[4]])


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
                selecion_usuario = input_modificado()

                if selecion_usuario.isdigit():
                    selecion_usuario = int(selecion_usuario)

                    if selecion_usuario == 1:
                        borrar_pantalla()
                        print("Ingrese en minutos la duracion de la evalucion. Por ejemplo: 300")

                        while True:
                            minutos = input_modificado()
                            minutos_procesados = validacion(minutos,1,4)

                            if minutos_procesados == 1:
                                segundo_minutos = int(minutos) * 60
                                datos_examen[0] = segundo_minutos
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
                                print("El dato que a ingresado es invalido, solo se perminten numeros con minimo 1 y maximo 4 caracteres")

                    elif selecion_usuario == 2:

                        borrar_pantalla()
                        print("Ingrese la contraseña del corte que presentaran sus alumnos. Por ejemplo: Asdrubal2767")

                        while True:
                            datos_examen[1] = input_modificado()

                            contrasena_procesada = validacion(datos_examen[1],1,20)

                            if contrasena_procesada == 2:
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
                                print("El dato que a ingresado es invalido, solo se perminten letras y numeros con minimo 1 y maximo 20 caracteres")
                    ##

                    elif selecion_usuario == 3:
                            
                        borrar_pantalla()
                        print("Ingrese la contraseña del zip que se enviara a su correo. Por ejemplo: corte3matematicas")

                        while True:
                            datos_examen[2] = input_modificado()

                            procesada_contraseña_zip = validacion(datos_examen[2],1,20)

                            if procesada_contraseña_zip == 2:
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
                                print("El dato que a ingresado es invalido, solo se perminten letras y numeros con minimo 1 y maximo 20 caracteres")


                    elif selecion_usuario == 4:

                        borrar_pantalla()
                        print("Ingrese el correo al cual se enviara el zip. Por ejemplo: profealex9@gmail.com")
                        
                        while True:
                            datos_examen[3] = input_modificado()

                            procesada_correo = validacion(datos_examen[3],1,30)
                            print("numero", procesada_correo)

                            if procesada_correo == 4:
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

                                if correo_examen_usuario == "si":
                                    break

                            else:
                                print('El dato que a ingresado es invalido, su correo debe contener "@gmail.com" o "@hotmail.com" y maximo 30 caracteres')


                    elif selecion_usuario == 5:
                        while True:
                            borrar_pantalla()
                            print("Elija la acción que desea realizar:")
                            print("1.- Agregar nueva pregunta")
                            print("2.- Volver al menú principal")

                            accion_pregunta = input_modificado()

                            if accion_pregunta == "1":
                                while True:
                                    print("Seleccione el tipo de pregunta múltiple(1) o teórico/práctico(2): ")
                                    while True:
                                        tipo_pregunta = input_modificado()
                                        if tipo_pregunta == "1" or tipo_pregunta == "2":
                                            break
                                        else:
                                            print("solo se permite 1 y 2, por favor reingrese el valor")

                                    if tipo_pregunta.isdigit():
                                        
                                        tipo_pregunta = int(tipo_pregunta)

                                        if tipo_pregunta == 1:
                                            while True:
                                                print("Ingrese el enunciado de la pregunta: ")
                                                pregunta_enunciado = input_modificado()
                                                pregunta_enunciado_procesado = validacion(pregunta_enunciado,1,200)
                                                opciones = []
                                                if pregunta_enunciado_procesado == 5 or pregunta_enunciado_procesado == 2 or pregunta_enunciado_procesado == 1 or pregunta_enunciado_procesado == 3: 
                                                    while True:
                                                        print("Escriba una opcion, si desea dejar de agregar opciones pulse enter sin escribir nada")
                                                        nueva_opcion = input_modificado()
                                                        nueva_opcion_procesado = validacion(nueva_opcion,1,200)

                                                        if nueva_opcion_procesado == 5 or nueva_opcion_procesado == 2 or nueva_opcion == "" or nueva_opcion == " ":
                                                            if nueva_opcion.strip():
                                                                opciones.append(nueva_opcion)
                                                            elif len(opciones) < 2:
                                                                print("Se necesitan al menos dos opciones para una pregunta de opción múltiple.")
                                                            else: 
                                                                break
                                                        else:
                                                            print("El dato que a ingresado es invalido, la opcion del enunciado debe tener minimo 1 caracter y maximo 200 caracteres")


                                                    print("Las opciones registradas son las siguientes: ")
                                                    for opciones_buscar in opciones:
                                                        indice = opciones.index(opciones_buscar)
                                                        print("Indice: ", indice)
                                                        print("Pregunta: ", opciones_buscar)
                                                        print("-----------------------------")

                                                    print("ingrese el indice de la pregunta correcta")

                                                    while True:
                                                        indice_respuesta_correcta = input_modificado()

                                                        indice_respuesta_correcta_validado = validacion(indice_respuesta_correcta,1,2)
                                                        if indice_respuesta_correcta_validado == 1:    

                                                            if int(indice_respuesta_correcta) < len(opciones):
                                                                respuesta_correcta = opciones[int(indice_respuesta_correcta)]
                                                                break
                                                            else:
                                                                print("La opción correcta debe ser una de las opciones disponibles. Por favor ingrese el indice de la pregunta correcta")
                                                        else: 
                                                            print("Introdusca un numero y un indice valido")

                                                        
                                                    print("Ingrese los puntos por responder correctamente: ")

                                                    while True:
                                                        puntos_respuesta_correcta = input_modificado()
                                                        
                                                        if puntos_respuesta_correcta.isdigit():

                                                            puntos_respuesta_correcta = int(puntos_respuesta_correcta)
                                                            
                                                            # Add the question to the datos_examen list
                                                            datos_examen[4].append({
                                                                "enunciado": pregunta_enunciado,
                                                                "opciones": opciones,
                                                                "respuesta_correcta": respuesta_correcta,
                                                                "puntos_respuesta_correcta": puntos_respuesta_correcta
                                                            })

                                                    
                                                            break

                                                        else:
                                                            print("Solo se permiten numeros, reingrese la punteracion")
                                                    
                                                    break

                                                else: 
                                                    print("El dato que a ingresado es invalido, el enunciado de la pregunta debe de tener minimo 1 caracter y maximo 200 caracteres")

                                            
                                    ####

                                        elif tipo_pregunta == 2:
                                            print("Ingrese el enunciado de la pregunta: ")
                                            while True:
                                                pregunta_enunciado = input_modificado()
                                                pregunta_enunciado_procesado = validacion(pregunta_enunciado,1,200)
                                                if pregunta_enunciado_procesado == 5 or pregunta_enunciado_procesado == 2 or pregunta_enunciado == 1 or pregunta_enunciado == 3:
                                                    print("La pregunta se almacenará como una pregunta teórica/práctica sin opciones.")

                                                    # Add the question to the datos_examen list
                                                    datos_examen[4].append({
                                                        "enunciado": pregunta_enunciado,
                                                        "opciones" : []
                                                    })
                                                    break
                                                else:
                                                    print("El dato que a ingresado es invalido, el enunciado de la pregunta debe de tener minimo 1 caracter y maximo 200 caracteres")

                                        else:
                                            print("Por favor elija una opcion correcta")

                                        imprimir_csv(datos_examen)
                                    
                                    else:
                                        print("solo se permiten numeros")


                                    print("¿Desea agregar otra pregunta? si/no")
                                    continuar_agregando_preguntas = input_modificado()

                                    while True:
                                        if continuar_agregando_preguntas == "si":
                                            break
                                        elif continuar_agregando_preguntas == "no":
                                            break
                                        else:
                                            print("Por favor seleciones una opcion valida. si/no")

                                    if continuar_agregando_preguntas == "no":
                                        break
                    
                            elif accion_pregunta == "2":
                                break

                            else:
                                print("opcion invalida. Intente nuevamente.")

                    elif selecion_usuario == 6:
                        borrar_pantalla()
                        imprimir_preguntas_teoricas = datos_examen[4]
                        print(f"El tiempo de evaluación no está especificado." if datos_examen[0] is None else f"Duración de la evaluación: {datos_examen[0] / 60} minutos")
                        print(f"La contraseña del corte que sera presentado por los alumno no esta especificada." if datos_examen[1] is None else f"Contraseña del corte que sera presentado por los alumno: {datos_examen[1]}")
                        print(f"La contraseña del zip no esta especificada." if datos_examen[2] is None else f"Contraseña del zip: {datos_examen[2]}")
                        print(f"El correo al cual se enviara el zip no esta especificado." if datos_examen[3] is None else f"Correo al que se enviara el zip: {datos_examen[3]}")
                        if not datos_examen[4]:
                            print(f"No se a ingresado ninguna pregunta:")
                        else:
                            print("Lista de preguntas \n")
                            print("PREGUNTAS TEORICAS")
                            for datos in imprimir_preguntas_teoricas:
                                if 'respuesta_correcta' in datos:
                                    print("Enunciado: ", datos['enunciado'])
                                    print("Opciones: ")
                                    for opciones in datos['opciones']:
                                        print("")
                                        print("1.- ",opciones)
                                        print("")
                                    print("Respuesta correcta: ", datos['respuesta_correcta'])
                                    print("Puntos por respuesta correcta: ", datos['puntos_respuesta_correcta'])
                                    print("-------------------------------")
                                print("-------------------------------")

                            print("PREGUNTAS PRACTICAS")
                            for datos in imprimir_preguntas_teoricas:
                                if not 'respuesta_correcta' in datos:
                                    print("Enunciado: ", datos['enunciado'])
                                    print("-------------------------------")
                                print("-------------------------------")
                                
                        print("-------------------------------")
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
