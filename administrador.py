#Librería usada para imprimir los datos en el csv
import csv
#Librería utilizada para quitar los acentos
from unidecode import unidecode
#Librería empleada para interactuar con el sistema opertivo a nivel de consola
import os
#Librería que se usará para controlar el tiempo
import time

#Contraseña del programa
passwort = "alertaprofesores2024/"

#define los nombres de las columnas
column_names = ['tiempo', 'contrasena','contrasena zip','correo','preguntas teoricas']
tiempo_evaluacion = None
contrasena_corte = None
contrasena_zip = None
correo_zip = None
base_pregunta = None
preguntas_teoricas = []

datos_examen = [tiempo_evaluacion, contrasena_corte, contrasena_zip, correo_zip, preguntas_teoricas]
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
    #se definen las validaciones con numeros ya que así es más faciles llamarlas
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

    while True:
        try:
             #Solicita la entrada del usuario y la convierte a minúsculas
            user_input = input(prompt).lower()

             #Normaliza la entrada eliminando caracteres especiales
            normalized_input = unidecode(user_input)

            #Verifica si se han especificado caracteres permitidos
            if allowed_characters:

                for char in normalized_input:
                    if char not in allowed_characters:
                        # Si el caracter no está en los permitidos lanza un error indicando el caracter inválido
                        raise ValueError(f"Caracter invalido: '{char}'")

            #Si la entrada es válida, la retorna
            return normalized_input

        #Captura los errores de valor
        except ValueError as e:
            #muestra el mensaje de error
            print(f"Error: {e}")

            # Si se han especificado caracteres permitidos
            if allowed_characters:
                 #Muestra los caracteres válidos al usuario
                print(f"Los caracteres validos son: {allowed_characters}")

def mostrar_preguntas(preguntas):
    print("Lista de preguntas:")
    #obtiene el indice y contenido de cada pregunta
    for i, pregunta in enumerate(preguntas):
        #muestra el indice y enunciado de la pregunta
        print(f"{i}: {pregunta['enunciado']}")
        #si la pregunta tiene respuesta correcta entoces es de opcion múltiple
        if 'respuesta_correcta' in pregunta:
            print("  (Pregunta de opción múltiple)")
            print("  Opciones:")
            #Obtiene el indice y contenido de las opciones y las muestra
            for j, opcion in enumerate(pregunta['opciones']):
                print(f"    {j + 1}. {opcion}")
            #muestra la respuesta correcta y el valor si responder bien
            print(f"  Respuesta correcta: {pregunta['respuesta_correcta']}")
            print(f"  Puntos por respuesta correcta: {pregunta['puntos_respuesta_correcta']}")
        #si la pregunta no tiene opciones entonces de practica
        else:
            print("  (Pregunta práctica)")
        print("-------------------------------")

def imprimir_csv(datos_examen):
    # Abre el archivo CSV en modo escritura
    with open('mi_archivo.csv', 'w', newline='') as csvfile:   

        #Escribir en el csv
        writer = csv.writer(csvfile)

        # Escribe los encabezados en la primera fila
        writer.writerow(column_names)

        #Puedes agregar filas de datos aquí
        writer.writerow([datos_examen[0], datos_examen[1], datos_examen[2], datos_examen[3], datos_examen[4]])

def menu_administrador():
    borrar_pantalla()
    print('''Bienvenido al PROYECTO CLASSROOM DOCENTE, para iniciar primero inserte la contraseña''')
    while True:
        #si el input es igual a la contraseña deja pasar
        contrasena_usuario = input_modificado()
        if contrasena_usuario.strip() == passwort:
            while True:
                borrar_pantalla()
                print("MENU")
                print("Acontinuacion podra modificar los parametros de su evaluacion, tenga en cuenta que debe rellenar todos los parametros para su evaluacion presentados a continuacion y que deben ser rellenados correctamente o de lo contrario podria surgir fallos a la hora de la precentacion de la evaluacion")
                print('''
        1.- Duracion de la evalucion
        2.- Contraseña del cohorte que sera presentado por los alumno
        3.- Contraseña del zip que sera enviado al correo
        4.- Correo al que se enviara el zip
        5.- Agregar o eliminar preguntas
        6.- Ver(en esta opcion podra ver todos los datos que a ingresado hasta el momento)
        7.- Guardar cambios (SI NO PRESIONA AQUI NO SE GUARDARAN LOS PARAMETROS DEL EXAMEN)
        
        NOTA: LUEGO DE SALIR DEL PROGRAMA NO PODRÁ MODIFICAR EL EXAMEN YA PARAMETRIZADO, SI QUIERE HACERLO TENDRA QUE ESTABLECER CADA PARAMETRO DE NUEVO DESDE 0.
        SE RECOMIENDA PULSAR LA OPCION "6" ANTES DE SALIR PARA VERIFICAR QUE TODO ESTÉ BIEN''')
                selecion_usuario = input_modificado()

                if selecion_usuario.isdigit():
                    selecion_usuario = int(selecion_usuario)

                    #si el usuario presiona 1 lo lleva para acá y así con cada "if selecion_usuario"
                    if selecion_usuario == 1:
                        borrar_pantalla()
                        print("Ingrese en minutos la duracion de la evalucion. Por ejemplo: 300")

                        while True:
                            #le pide los minutos al usurio mediante el input_modificado
                            minutos = input_modificado()
                            #se verifica que pase la validacion
                            minutos_procesados = validacion(minutos,1,4)

                            if minutos_procesados == 1:
                                #debido a que el tiempo se mide en segundos, entonces el valor que ingrese el profesor se multiplicará por 60 para que sean minutos
                                segundo_minutos = int(minutos) * 60
                                #ahora "datos_examen[0]" contiene los minutos
                                datos_examen[0] = segundo_minutos
                                print("El tiempo que a ingresado es de: ", datos_examen[0] / 60 ," minutos")
                                print("Esta seguro que de que esa sera la duracion para el examen? si/no")

                                while True:

                                    respues_examen_usuario = input_modificado()

                                    if respues_examen_usuario == "si":
                                        break
                                    elif respues_examen_usuario == "no":
                                        print("Por favor reingrese el tiempo para el cohorte")
                                        break
                                    else:
                                        print("por favor elija una opcion valida")

                                if respues_examen_usuario == "si":
                                    break

                            else:
                                print("El dato que a ingresado es invalido, solo se perminten numeros con minimo 1 y maximo 4 caracteres")

                    elif selecion_usuario == 2:

                        borrar_pantalla()
                        print("Ingrese la contraseña del cohorte que presentaran sus alumnos. Por ejemplo: Asdrubal2767")

                        while True:
                            #le pide la contraseña al usurio mediante el input_modificado
                            datos_examen[1] = input_modificado()
                            ##se verifica que pase la validacion
                            contrasena_procesada = validacion(datos_examen[1],1,20)

                            if contrasena_procesada == 2:
                                print("La contraseña del cohorte que a ingresado es: ", datos_examen[1])
                                print("Esta seguro que de que esa sera la contraseña para el cohorte? si/no")

                                while True:

                                    contrasena_examen_usuario = input_modificado()

                                    if contrasena_examen_usuario == "si":
                                        break
                                    elif contrasena_examen_usuario == "no":
                                        print("Por favor reingrese la contraseña del cohorte")
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
                            #aqui se le pide al usuario la contraseña
                            datos_examen[2] = input_modificado()

                            #se verifica que pase la validacion
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
                            #le pide el correo al profesor y lo almacena en "datos_examen[3]"
                            datos_examen[3] = input_modificado()

                            #lo valida
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
                            print("2.- Eliminar pregunta")
                            print("3.- Volver al menú principal")

                            #pide qué opcion se desea ejecutar
                            accion_pregunta = input_modificado()

                            if accion_pregunta == "1":
                                #aqui se le pide al usuario que escoja el tipo de pregunta que desea guardar
                                while True:
                                    print("Seleccione el tipo de pregunta múltiple(1) o tpráctica(2): ")
                                    while True:
                                        tipo_pregunta = input_modificado()
                                        if tipo_pregunta == "1" or tipo_pregunta == "2":
                                            break
                                        else:
                                            print("solo se permite 1 y 2, por favor reingrese el valor")

                                    if tipo_pregunta.isdigit():
                                        
                                        tipo_pregunta = int(tipo_pregunta)

                                        #si escoge una entonces es de opcion multiple
                                        if tipo_pregunta == 1:
                                            while True:
                                                print("Ingrese el enunciado de la pregunta: ")
                                                #se le pide enunciado y se valida
                                                pregunta_enunciado = input_modificado()
                                                pregunta_enunciado_procesado = validacion(pregunta_enunciado,1,200) #estos numeros del final indican los caracteres minimos y maximos
                                                #se empieza con las opciones
                                                opciones = []
                                                if pregunta_enunciado_procesado == 5 or pregunta_enunciado_procesado == 2 or pregunta_enunciado_procesado == 1 or pregunta_enunciado_procesado == 3: #la pregunta tiene que pasar las validaciones 1, 2, 3 y 5
                                                    while True:
                                                        print("Escriba una opcion, si desea dejar de agregar opciones pulse enter sin escribir nada")
                                                        #se solicita una opcion
                                                        nueva_opcion = input_modificado()
                                                        nueva_opcion_procesado = validacion(nueva_opcion,1,200)

                                                        if nueva_opcion_procesado == 5 or nueva_opcion_procesado == 2 or nueva_opcion_procesado == 1 or nueva_opcion_procesado == 3 or nueva_opcion == "" or nueva_opcion == " ": #la opcion tiene que pasar las mismas validaciones con la diferencia de que si está vacia y hay al menos 2 opciones se toma como que ya no habrán más opciones 
                                                            if nueva_opcion.strip():
                                                                opciones.append(nueva_opcion)
                                                            elif len(opciones) < 2: #cuenta que haya al menos 2 opciones
                                                                print("Se necesitan al menos dos opciones para una pregunta de opción múltiple.")
                                                            else: 
                                                                break
                                                        else:
                                                            print("El dato que ha ingresado es invalido, la opcion del enunciado debe tener minimo 1 caracter y maximo 200 caracteres")

                                                    #Aqui se muestran las opciones registradas con su indice
                                                    print("Las opciones registradas son las siguientes: ")
                                                    for opciones_buscar in opciones:
                                                        indice = opciones.index(opciones_buscar)
                                                        print("Indice: ", indice)
                                                        print("Respuesta: ", opciones_buscar)
                                                        print("-----------------------------")

                                                    print("ingrese el indice de la respuesta correcta")

                                                    while True:
                                                        #se le pide al usuario el indice de la respuesta correcta, se valida y se revisa que esté en las opciones
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
                                                        #se piden los puntos por responder correctamente y se verifica que solo se ingresen numeros
                                                        puntos_respuesta_correcta = input_modificado()
                                                        
                                                        if puntos_respuesta_correcta.isdigit():

                                                            puntos_respuesta_correcta = int(puntos_respuesta_correcta)

                                                            #por ultimo se añaden todos los datos a "datos_examen[4]"
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
                                        #si el usuario escoge 2 entonces una pregunta practica (sin opciones)
                                        elif tipo_pregunta == 2:
                                            print("Ingrese el enunciado de la pregunta: ")
                                            while True:
                                                #De igual forma se guarda el enunciado de la pregunta y se valida
                                                pregunta_enunciado = input_modificado()
                                                pregunta_enunciado_procesado = validacion(pregunta_enunciado,1,200)
                                                if pregunta_enunciado_procesado == 5 or pregunta_enunciado_procesado == 2 or pregunta_enunciado_procesado == 1 or pregunta_enunciado_procesado == 3:
                                                    print("La pregunta se almacenará como una pregunta teórica/práctica sin opciones.")

                                                    #Añade la pregunta a "datos_examen[4]" sin opciones
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

                                    #se le pregunta al usuario que si desea agregar otra pregunta
                                    print("¿Desea agregar otra pregunta? si/no")
                                    continuar_agregando_preguntas = input_modificado()

                                    while True:
                                        if continuar_agregando_preguntas == "si":
                                            break
                                        elif continuar_agregando_preguntas == "no":
                                            break
                                        else:
                                            print("Por favor seleciones una opcion valida. si/no")
                                            continuar_agregando_preguntas = input_modificado()

                                    if continuar_agregando_preguntas == "no":
                                        break
                            
                            #aqui empieza el eliminar pregunta
                            if accion_pregunta == "2": 

                                #primero, si no hay pues no hay, y se le avisa al usuario con un mensaje de 3 segundos y se va para atras
                                if not preguntas_teoricas:
                                    print("No hay preguntas para eliminar.")
                                    time.sleep(3)
                                else:
                                    while True:
                                        #muestra las preguntas con su respectivo indice con la funcion que definimos anteriormente
                                        mostrar_preguntas(preguntas_teoricas)
                                        print("Ingrese el índice de la pregunta que desea eliminar: ")
                                        indice_pregunta = input_modificado()
        
                                        #valida que el indice sea un número entero válido
                                        if indice_pregunta.isdigit():
                                            indice_pregunta = int(indice_pregunta)
            
                                            # verifica que el indice esté dentro de las preguntas existentes
                                            if 0 <= indice_pregunta < len(preguntas_teoricas):
                                                #elimina la pregunta del examen
                                                del preguntas_teoricas[indice_pregunta]
                                                print("Pregunta eliminada exitosamente.")
                                                break
                                            else:
                                                print("Índice de pregunta inválido. Por favor, intente de nuevo.")
                                        else:
                                            print("Entrada inválida. Por favor, ingrese un número entero.")


                            #si presiona 3 se va para atras
                            elif accion_pregunta == "3":
                                break

                            else:
                                print("opcion invalida. Intente nuevamente.")

                    #este es el apartado para ver lo que se ha hecho
                    elif selecion_usuario == 6:
                        borrar_pantalla()
                        imprimir_preguntas_teoricas = datos_examen[4]
                        print(f"El tiempo de evaluación no está especificado." if datos_examen[0] is None else f"Duración de la evaluación: {datos_examen[0] / 60} minutos")
                        print(f"La contraseña del cohorte que sera presentado por los alumno no esta especificada." if datos_examen[1] is None else f"Contraseña del cohorte que sera presentado por los alumno: {datos_examen[1]}")
                        print(f"La contraseña del zip no esta especificada." if datos_examen[2] is None else f"Contraseña del zip: {datos_examen[2]}")
                        print(f"El correo al cual se enviara el zip no esta especificado." if datos_examen[3] is None else f"Correo al que se enviara el zip: {datos_examen[3]}")
                        if not datos_examen[4]:
                            print(f"No se ha ingresado ninguna pregunta:")
                        else:
                            #se muestran las preguntas (con lineas para que se vean más bonitas y ordenadas)
                            print("Lista de preguntas \n")
                            print("-------------------------------")
                            print("PREGUNTAS DE OPCION MULTIPLE")

                            #se inicia un contador en 0 con las preguntas teoricas
                            almacen_contador_teoria = 0

                            for datos in imprimir_preguntas_teoricas:
                                #se revisa cuantas preguntas contienen "respuesta_correcta", así se revisa cual es pregunta teorica y cual es practica y se suman al contador
                                if 'respuesta_correcta' in datos:
                                    almacen_contador_teoria += 1
                                    #se muestran las preguntas teoricas con su enunciado, opciones enumerdas, opcion correcta y puntuacion por responder correctamente
                                    print(f"Pregunta {almacen_contador_teoria}.- Enunciado: ", datos['enunciado'])
                                    print("Opciones: ")
                                    for j,opciones in enumerate(datos['opciones']):
                                        print(f"{j + 1}.- ",opciones)
                                    print("Respuesta correcta: ", datos['respuesta_correcta'])
                                    print("Puntos por respuesta correcta: ", datos['puntos_respuesta_correcta'])
                                    print("-------------------------------")

                            print("PREGUNTAS PRACTICAS")
                            print("-------------------------------")
                            almacen_contador_practica = 0
                            #aqui se similiar, se inicia el contador en 0 y se revisa si la pregunta tiene "respuesta_correcta" al no tener pasa a ser pregunta practica y aumenta el contador
                            for datos in imprimir_preguntas_teoricas:
                                if not 'respuesta_correcta' in datos:
                                    almacen_contador_practica += 1
                                    print(f"Pregunta {almacen_contador_practica}.- Enunciado: ", datos['enunciado'])
                                    print("-------------------------------")


                        input("Pulse enter para regresar al menu")

                    elif selecion_usuario == 7:
                        #por ultimo, se guardan todos los datos en el csv cuando el usuario escoge la ultima opcion, usando la funcion "imprimir_csv" que definimos al principio
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