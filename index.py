#Librería para comprimir los datos con contraseña (similiar a la encriptacion)
import pyzipper
#Librería que se usará para controlar el tiempo
import time
#Librería para enviar los correos de forma automática
import smtplib
#Librería para quitar los acentos
from unidecode import unidecode
#Libreria empleada para interactuar con el sistema opertivo a nivel de consola
import os

def borrar_pantalla():
    sistema_operativo = os.name

    if sistema_operativo == 'posix':
        os.system('clear')
    elif sistema_operativo == 'nt':
        os.system('cls')

def temporizador(segundos):
    while segundos: 
        mins = segundos // 60
        secs = segundos % 60
        tiempo_restante = f'{mins: 02d}:{secs:02d}'
        print(tiempo_restante, end='\r')
        time.sleep(1)
        segundos -= 1
        if segundos == 80:
            print("se te esta acabando el tiempo")

        elif segundos == 60:
            print("se te esta acabando el tiempo")

#validar solo numeros
def validar_solo_numeros(dato_input):
    tipo = dato_input.isdigit()
    if tipo == True:
        dato_valido_input = True
        return dato_valido_input

#Validar_alfanumerico
def validar_alfanumerico(dato_input):

    #Extrae la longitud del dato
    caracteres = len(dato_input)

    #Esta es la parte encargada de detectar números y letras 
    tipo = dato_input.isalnum()
    if tipo == True:
        if caracteres >= 2 and caracteres <= 12:
            dato_valido_input = True
            return dato_valido_input

#Validar_nombre fue creado para validar el nombre 
def validar_nombre(dato_input):

    #Extrae la longitud del dato
    caracteres = len(dato_input)

    #Esta es la parte encargada de detectar letras 
    tipo = dato_input.isalpha()
    if tipo == True:
        if caracteres >= 3 and caracteres <= 20:
            dato_valido_input = True
            return dato_valido_input

#Validar_cedula fue creado para validar la cedula
def validar_cedula(dato_input):
        
    #Extrae la longitud del dato
    caracteres = len(dato_input)

    #Esta es la parte encargada de detectar números
    tipo = dato_input.isdigit()
    if tipo == True:
        if caracteres == 8:
            dato_valido_input = True
            return dato_valido_input

#############!!!!!!!!!!!!!!!!!!!

def inicio_seccion ():
    borrar_pantalla()
    print('''Bienvenido al PROYECTO CLASSROOM, para iniciar primero inserte sus datos''')

    #Esta parte del codigo es la encargada de pedirle los datos personales al usuario y hacerlo CERTIFICAR
    #que estén correctos (Alejandro escribe mal la variables a proposito para que se vean más originales)
    while True:
        nombre_ususario = input('Por favor ingrese su nombre (solo primer nombre): ')
        validar_nombre_usuario = validar_nombre(nombre_ususario)
        #Con el "while" hacemos los bucles para que se le vuelva a preguntar al usuario por alguno de sus
        #datos en caso de algún error
        while validar_nombre_usuario != True:
            print("Por favor vuelva a ingresar su nombre, su nombre debe contar con entre 3 a 20 letras ")
            nombre_ususario = input('Por favor ingrese nuevamente su nombre (solo primer nombre): ')
            validar_nombre_usuario = validar_nombre(nombre_ususario)
        
        print('''El nombre que ha ingresado es: '''+ nombre_ususario +'''.
esta seguro que este es su nombre? si/no ''')
        sertificar_nombre = input ("").lower()
        sertificar_nombre_procesado = unidecode(sertificar_nombre)

        while sertificar_nombre_procesado != "no" and sertificar_nombre_procesado != "si":
            print('''Por favor seleccione una opción válida, solo se pemite "si" o "no"''')
            sertificar_nombre = input().lower()
            sertificar_nombre_procesado = unidecode(sertificar_nombre)

        if sertificar_nombre_procesado == "si":
            break
    
    while True :
        apellido_usuario = input('Por favor ingrese su apellido: ')
        validar_apellido_usuario = validar_nombre(apellido_usuario)

        while validar_apellido_usuario != True:
            print("Por favor vuelva a ingresar su apellido, su apellido debe contar con entre 3 a 20 letras ")
            apellido_usuario = input('por favor ingrese nuevamene su apellido: ')
            validar_apellido_usuario = validar_nombre(apellido_usuario)

        print('''El apellido que ha ingresado es: '''+ apellido_usuario +'''.
esta seguro que este es su apellido? si/no ''')
        sertificar_apellido = input ("").lower()
        sertificar_apellido_procesado = unidecode(sertificar_apellido)

        while sertificar_apellido_procesado != "no" and sertificar_apellido_procesado != "si":
            print('''Por favor seleccione una opción válida, solo se pemite "si" o "no"''')
            sertificar_apellido = input().lower()
            sertificar_apellido_procesado = unidecode(sertificar_apellido)

        if sertificar_apellido_procesado == "si":
            break
        

    while True :
        cedula_ususario = input('Por favor ingrese su cédula: ')
        validar_cedula_usuario = validar_cedula(cedula_ususario)

        while validar_cedula_usuario != True:
            print("Por favor vuelva a ingresar su cédula, su cédula debe contar con 8 números ")
            cedula_ususario = input('Por favor ingrese nuevamente su cedula: ')
            validar_cedula_usuario = validar_cedula(cedula_ususario)

        print('''El cedula que ha ingresado es: '''+ cedula_ususario +'''.
esta seguro que este es su cedula? si/no ''')
        sertificar_cedula = input ().lower()
        sertificar_cedula_procesado = unidecode(sertificar_cedula)
        
        while sertificar_cedula_procesado != "no" and sertificar_cedula_procesado != "si":
            print('''Por favor seleccione una opción válida, solo se pemite "si" o "no"''')
            sertificar_cedula = input().lower()
            sertificar_cedula_procesado = unidecode(sertificar_cedula)

        if sertificar_cedula_procesado == "si":
            break
    
    print("usuario registrado: ",nombre_ususario, apellido_usuario)

    time.sleep(1)

    borrar_pantalla()

    return nombre_ususario, apellido_usuario, cedula_ususario 
    #El "return" nos permite usar las variables de "nombre_ususario, apellido_usuario, cedula_ususario"
    #en la siguiente función

def encriptacion(nombre_ususario, apellido_usuario, cedula_ususario, respuestas_examen):
    # Se crea el nombre del archivo .txt
    nombre_archivo_txt = f"{nombre_ususario}_{apellido_usuario}_{cedula_ususario}.txt"
    # Se crea el nombre del archivo .zip
    nombre_archivo_zip = f"{nombre_ususario}_{apellido_usuario}_{cedula_ususario}.zip"

    # Guarda las respuestas en el archivo de texto
    with open(nombre_archivo_txt, 'w') as archivo_txt:
        for i, respuesta in enumerate(respuestas_examen, start=1):
            archivo_txt.write(f"Pregunta {i}: {respuesta}\n")

    # Guarda el archivo de texto en un archivo ZIP con contraseña
    with pyzipper.AESZipFile(nombre_archivo_zip, 'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zf:
        # Contraseña del archivo ZIP (se puede cambiar)
        contraseña_profesor = b"profemirtha123"
        zf.setpassword(contraseña_profesor)
        
        # Escribe el archivo de texto en el archivo ZIP
        zf.write(nombre_archivo_txt)

    os.remove(nombre_archivo_txt) #borra el txt para que sea inaccesible para el alumno
    #Aún hay cosas que cambiar en esta función, debido a que para acabarla necesitamos terminar otras funciones
    #del proyecto

def enviarCorreo ():
    
    #Mensaje que se enviará
    mensaje = 'colocar aqui el mensaje'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    #Datos para que la librería pueda acceder a el correo del remitente
    server.login('correo','contraseña')

    #Remitente, destinatario, mensaje
    server.send_message('correo del remitente','correo del destinatario',mensaje)

    #Cierra sesión
    server.quit()  
    #Mismo caso aquí, aún faltan algunas cosas por cambiar ya que debemos terminar con otras cosas primero, pero como
    #resumen rápido, esta función hará que cada que un alumno termine un examen, sus respuestas junto con sus datos
    #personales lleguen a su correo (al de usted)

#Aquí empezamos con el menú de los exámenes
def menu_principal ():
    validar_corte = "no"
    
    print("!SELECCIONE EL COHORTE QUE VA A PRESENTAR!")
    print('''Para cohorte 1, pulse 1
Para cohorte 2, pulse 2
Para cohorte 3, pulse 3
Para cohorte 4, pulse 4 ''')

    while validar_corte == "no":
        corte_selecionado = input("")
        validar_numeros_corte=validar_solo_numeros(corte_selecionado)

        if validar_numeros_corte == True:
            corte_procesado = int(corte_selecionado)
            if corte_procesado == 1:
                while True:
                    #Con el ".lower" se asegura que sin importar como escriban el "si/no" sea tomado como bueno igual
                    validar_corte_info = input("¿Está seguro que este es el cohorte que va a presentar? si/no ").lower()
                    validar_corte = unidecode(validar_corte_info)
                    if validar_corte == "si":
                        borrar_pantalla()
                        primer_corte()
                        break

                    elif validar_corte == "no":
                        break

                    else:
                        print('''Por favor seleccione una opción válida, solo se pemite "si" o "no" ''')
                        validar_corte = False
                    
            elif corte_procesado == 2:
                while True:
                    #Con el ".lower" se asegura que sin importar como escriban el "si/no" sea tomado como bueno igual
                    validar_corte_info = input("¿Está seguro que este es el cohorte que va a presentar? si/no ").lower()
                    validar_corte = unidecode(validar_corte_info)
                    if validar_corte == "si":
                        borrar_pantalla()
                        segundo_corte()
                        break

                    elif validar_corte == "no":
                        break

                    else:
                        print('''Por favor seleccione una opción válida, solo se pemite "si" o "no" ''')
                        validar_corte = False
                
            elif corte_procesado == 3:
                while True:
                    #Con el ".lower" se asegura que sin importar como escriban el "si/no" sea tomado como bueno igual
                    validar_corte_info = input("¿Está seguro que este es el cohorte que va a presentar? si/no ").lower()
                    validar_corte = unidecode(validar_corte_info)
                    if validar_corte == "si":
                        borrar_pantalla()
                        terecer_corte()
                        break

                    elif validar_corte == "no":
                        break

                    else:
                        print('''Por favor seleccione una opción válida, solo se pemite "si" o "no" ''')
                        validar_corte = False
                
            elif corte_procesado == 4:
                while True:
                    #Con el ".lower" se asegura que sin importar como escriban el "si/no" sea tomado como bueno igual
                    validar_corte_info = input("¿Está seguro que este es el cohorte que va a presentar? si/no ").lower()
                    validar_corte = unidecode(validar_corte_info)
                    if validar_corte == "si":
                        borrar_pantalla()
                        cuarto_corte()
                        break

                    elif validar_corte == "no":
                        break

                    else:
                        print('''Por favor seleccione una opción válida, solo se pemite "si" o "no" ''')
                        validar_corte = False

            else:
                print("Por favor selecione una opción válida ")
            #Se le da a escoger al usuario qué cohorte va a presentar, se le hace que valide por si se equivoca
            #y lo manda a corregir si no selecciona ninguno
        else:
            print("solo se permiten numeros")
            
def presentar_pregunta(enunciado, opciones):
    print(enunciado)
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")

def validar_respuesta():
    while True:
        respuesta = input("Seleccione su respuesta (ingrese el número correspondiente): ")
        if respuesta.isdigit():
            caracteres = int(respuesta)
            if caracteres <= 4 and caracteres >= 1:
                return caracteres
            else:
                print("Por favor, ingrese un número válido.")
        else:
            print("Solo se permiten numeros")

respuestas_examen = []

def realizar_examen(preguntas):
    global respuestas_examen
    #temporizador(100) la funcion esta hay pero tuvimos problemas para implementarla
    for pregunta in preguntas:
        borrar_pantalla()
        confirmacion_procesada = "no"
        presentar_pregunta(pregunta["enunciado"], pregunta["opciones"])
        while confirmacion_procesada == "no":
            respuesta = validar_respuesta()
            print(f"Su respuesta fue: {respuesta}")
            while True:
                confirmacion = input("¿Está seguro de su respuesta? (si/no): ").lower()
                confirmacion_procesada = unidecode(confirmacion)
                if confirmacion_procesada == "no":
                    print("Por favor, vuelva a seleccionar su respuesta.")
                    # No necesitas llamar realizar_examen() de nuevo aquí
                    # Realiza cualquier acción adicional si el usuario quiere cambiar su respuesta
                    break
                elif confirmacion_procesada == "si":
                    respuestas_examen.append(respuesta)  # Agrega la respuesta a la lista de respuestas
                    break
                else:
                    print("Porfavor seleccione una opcion valida")

        
    print("La evaluación ha finalizado.")
    return respuestas_examen  # Devuelve todas las respuestas al finalizar el examen

def primer_corte ():
    print("Bienvenido al primer cohorte.")
    print("Tiene X tiempo para terminar esta prueba. Si sale del programa antes de finalizar, su nota será perjudicada.")
    input("Pulse cualquier tecla para iniciar la evaluación.")

    preguntas = [
        {
            "enunciado": "pregunta 1,¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]
            
        },
        {
            "enunciado": "pregunta 2,¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]
        },
        {
            "enunciado": "pregunta 3,¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]}
        # Agregar más preguntas aquí
    ]
    return realizar_examen(preguntas)

def segundo_corte ():
    print("Bienvenido al segundo cohorte.")
    print("Tiene X tiempo para terminar esta prueba. Si sale del programa antes de finalizar, su nota será perjudicada.")
    input("Pulse cualquier tecla para iniciar la evaluación.")

    preguntas = [
        {
            "enunciado": "pregunta 1,¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]
            
        },
        {
            "enunciado": "pregunta 2,¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]
        },
        {
            "enunciado": "pregunta 3,¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]}
        # Agregar más preguntas aquí
    ]
    return realizar_examen(preguntas)

def terecer_corte ():
    print("Bienvenido al tercer cohorte.")
    print("Tiene X tiempo para terminar esta prueba. Si sale del programa antes de finalizar, su nota será perjudicada.")
    input("Pulse cualquier tecla para iniciar la evaluación.")

    preguntas = [
        {
            "enunciado": "pregunta 1,¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]
            
        },
        {
            "enunciado": "pregunta 2,¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]
        },
        {
            "enunciado": "pregunta 3,¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]}
        # Agregar más preguntas aquí
    ]
    return realizar_examen(preguntas)

def cuarto_corte ():
    print("Bienvenido al cuarto cohorte.")
    print("Tiene X tiempo para terminar esta prueba. Si sale del programa antes de finalizar, su nota será perjudicada.")
    input("Pulse cualquier tecla para iniciar la evaluación.")

    preguntas = [
        {
            "enunciado": "pregunta  1,¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]
            
        },
        {
            "enunciado": "pregunta 2,¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]
        },
        {
            "enunciado": "pregunta 3,¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]}
        # Agregar más preguntas aquí
    ]
    return realizar_examen(preguntas)
#En esta función (menu_principal ()) estarán definidos los 4 cohortes/examenes que podrán presentar los alumnos,
#esta parte aún no está terminada así que es probable que tenga errores, así como también puede estar
#sujeta a cambios, actualmente es en esta función en la que estamos trabajando

def main():

    #obtiene los datos personales del usuario
    nombre_ususario, apellido_usuario, cedula_ususario = inicio_seccion()

    #lleva al usuario a seleccionar el cohorte a presentar
    menu_principal()

    #Comprime/encripta los datos
    encriptacion(nombre_ususario, apellido_usuario, cedula_ususario, respuestas_examen)

if __name__ == "__main__":
     main()

#La función "main()" nos ayuda a hacer que cada una de las demás funciones se ejecute en el orden que deben y en la forma
#en la que deben hacerlo ya que "if __name__ == "__main__"" nos permite hacer seguir a las funciones el orden de ejecución
#pautado por el programador, activandose cuando el script se ejecuta como el programa principal