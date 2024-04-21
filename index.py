#Librería para comprimir los datos con contraseña (similiar a la encriptación)
import pyzipper
#Librería que se usará para controlar el tiempo
import time
#Librería para enviar los correos de forma automática
import smtplib
#Librería para quitar los acentos
from unidecode import unidecode
#Librería empleada para interactuar con el sistema opertivo a nivel de consola
import os
#Librería que nos ayuda a crear el modal del temporizador
import tkinter as tk
#Librería que nos permitió integrar el reloj al código, permite que el reloj se ejecute "aparte" del menú
import threading
#Libreria usada para crear el modal de cerrar sesión
from tkinter import messagebox
#Libreria empleada para detectar que teclas se precionan
import signal

#Librerías del correo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#variables globales
preguntas = ["Pregunta 1", "Pregunta 2", "Pregunta 3", "Pregunta 4", "Pregunta 5", "Pregunta 6", "Pregunta 7", "Pregunta 8", "Pregunta 9", "Pregunta 10"]
examen_iniciado = False
corriendo = True
usuario = []
seguro_crito = True
respuestas_examen = []
seguro_print = False
#mensaje_abierto = True

def modal_salir():
    #crea la base del modal
    window = tk.Tk()
    window.withdraw()

    # Crear un cuadro de diálogo modal
    result = messagebox.askokcancel("Finalizar evalucion", "salir de la evaluación perjudicará tu nota ¿Estás seguro que deseas salir?")
    if result:
        global corriendo
        corriendo = False
        salir_programa()
        #cerrar_mensaje_bienvenida()

    window.mainloop()

#Esta función muestra una ventana emergente con un mensaje de bienvenida al usuario. La ventana se mantiene abierta
#hasta que el usuario la cierra.
def mostrar_bienvenida():
    global mensaje_bienvenida
    #Se crea una nueva ventana utilizando la clase tk.Tk()
    mensaje_bienvenida = tk.Tk()
    #Se configura la geometría de la ventana a una posición específica (-50, 20) en la pantalla.
    mensaje_bienvenida.geometry("-50+20")
    #Se define un protocolo para que la ventana no se cierre cuando el usuario haga clic en la X.
    mensaje_bienvenida.protocol("WM_DELETE_WINDOW", lambda: None)
    boton_bienvenida = tk.Button(mensaje_bienvenida, text="Proyecto classroom",)
    boton_bienvenida.pack()
    mensaje_bienvenida.mainloop()

#def cerrar_mensaje_bienvenida():
    #global mensaje_abierto
    #mensaje_abierto = False
    #mensaje_bienvenida.destroy()
    #salir_programa()

threading.Thread(target=mostrar_bienvenida).start()

#Define la función signal_handler que se encargará de manejar la señal SIGINT
def signal_handler(sig, frame):
    print("")
    #Crea un nuevo hilo (t) y le asigna la función modal_salir como objetivo e inicia la ejecución del hilo "t" para que la
    #función modal_salir se ejecute en segundo plano, permitiendo la gestión adecuada del cierre sin bloquear la respuesta a la señal.
    t = threading.Thread(target=modal_salir)
    t.start()

#Asigna la función signal_handler como la encargada de manejar la señal SIGINT. De esta forma, cuando se
#presione CTRL+C, se ejecutará la función signal_handler en lugar de finalizar el programa directamente
signal.signal(signal.SIGINT, signal_handler)

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

def salir_programa():
    global respuestas_examen
    global seguro_crito
    global corriendo
    
    #Comprueba si el examen se inició (examen_iniciado) y si las respuestas se guardaron de forma segura (seguro_escrito)
    if examen_iniciado and seguro_crito:
        #Borra la pantalla
        borrar_pantalla()
        #Extrae el nombre, apellido y cédula del usuario del arreglo usuario
        nombre_ususario = usuario[0]
        apellido_usuario = usuario[1]
        cedula_ususario = usuario[2]
        #llama a encriptación
        print("Evaluación finalizada")
        encriptacion(nombre_ususario, apellido_usuario, cedula_ususario, respuestas_examen)
        #Actualiza la variable seguro_escrito a False para indicar que ya no hay necesidad de guardar las respuestas.
        seguro_crito = False
        #Actualiza la variable corriendo a False para indicar que el programa debe finalizar
        corriendo = False

    if seguro_print == False:
        print("Terminando el programa...")
        seguro_crito = True
    exit()

def temporizador_asyncrono(segundos):
    #La función define una variable global corriendo como accesible dentro de la función.
    global corriendo
    #Se inicia un bucle while que se ejecuta mientras la variable segundos sea mayor que 0 y la variable corriendo sea True.
    while segundos and corriendo:
        #Se utiliza la función time.sleep(1) para suspender la ejecución del programa durante un segundo.
        #Se decrementa la variable segundos en 1. 
        time.sleep(1)
        #Al final del bucle, se comprueba si la variable segundos es menor o igual a 0.
        #Si es así, se ejecuta la función salir_programa para finalizar el programa de forma segura.
        segundos -= 1
    salir_programa()

def temporizador(segundos, label, root):
    #La función define una variable global corriendo como accesible dentro de la función.
    global corriendo
    #Se inicia un bucle while que se ejecuta mientras la variable segundos sea mayor que 0 y la variable corriendo sea True.
    while segundos and corriendo: 
        mins = segundos // 60
        secs = segundos % 60
        tiempo_restante = f'{mins:02d}:{secs:02d}'
        label.config(text=tiempo_restante)
        time.sleep(1)
        segundos -= 1
        #se crean alertas simples para que el alumno se percate de cuando se le esta acabando el tiempo
        if segundos == 600:
            tk.messagebox.showinfo("Alerta de tiempo", "Te faltan 10 minutos")
        elif segundos == 300:  
            tk.messagebox.showinfo("Alerta de tiempo", "Te faltan 5 minutos")
        elif segundos == 60: 
            tk.messagebox.showinfo("Alerta de tiempo", "Te faltan 1 minuto!!")
    root.destroy()

def iniciar_temporizador():
    global corriendo
    #Se establece la variable corriendo a True para indicar que el programa está en ejecución.
    corriendo = True
    #Se crea una ventana emergente usando la biblioteca tkinter
    root = tk.Tk()
    #Se configura la ventana emergente con la posición, tamaño y título.
    root.geometry("+50+20")
    root.title("Temporizador")

    # Deshabilitar el botón de cierre para que el alumno no cierre el cronometro por accidente
    root.protocol("WM_DELETE_WINDOW", lambda: None)

    label = tk.Label(root, text="", width=10)
    label.pack()

    segundos = 3600
    #Se crea un hilo nuevo usando la función threading.Thread para ejecutar la función temporizador en segundo plano.
    #Se le pasa a la función temporizador como argumentos la cantidad de segundos, la etiqueta label y la ventana root.
    #Se inicia la ejecución del hilo llamando a start().
    threading.Thread(target=temporizador, args=(segundos, label, root)).start()

    #Se inicia el bucle principal de la ventana emergente (root.mainloop()) para mostrar la ventana y esperar a
    #que el usuario interactúe con ella.
    root.mainloop()

# Para detener el temporizador, llama a la función detener_temporizador
# detener_temporizador()


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

def inicio_seccion ():

    #Esta parte del codigo es la encargada de pedirle los datos personales al usuario y hacerlo CERTIFICAR
    #que estén correctos (Alejandro escribe mal la variables a proposito para que se vean más originales)
    def inicio_seccion_nombre():
        try:
            borrar_pantalla()
            print('''Bienvenido al PROYECTO CLASSROOM, para iniciar primero inserte sus datos''')
            while True:
                print("Por favor ingrese su nombre (solo primer nombre): ")
                nombre_ususario = input('')
                validar_nombre_usuario = validar_nombre(nombre_ususario)
                while validar_nombre_usuario != True:
                    print("Su nombre debe contar con entre 3 a 20 caracteres letras ")
                    print("Por favor ingrese nuevamente su nombre (solo primer nombre):")
                    nombre_ususario = input("")
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
            return nombre_ususario
        except EOFError:
            return inicio_seccion_nombre()
    nombre_ususario=inicio_seccion_nombre()

    def inicio_seccion_apellido():
        try:
            while True :
                print("Por favor ingrese su apellido (solo primer apellido): ")
                apellido_usuario = input('')
                validar_apellido_usuario = validar_nombre(apellido_usuario)

                while validar_apellido_usuario != True:
                    print("Su apellido debe contar con entre 3 a 20 caracteres solo letras ")
                    print("por favor ingrese nuevamene su apellido (solo primer apellido): ")
                    apellido_usuario = input("")
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
            return apellido_usuario
        except EOFError:
            return inicio_seccion_apellido()
    apellido_usuario = inicio_seccion_apellido()
            
    def inicio_seccion_cedula():
        try:
            while True :
                print("Por favor ingrese su cédula: ")
                cedula_ususario = input('')
                validar_cedula_usuario = validar_cedula(cedula_ususario)

                while validar_cedula_usuario != True:
                    print("Su cédula debe contar con 8 caracteres solo números ")
                    print("Por favor ingrese nuevamente su cedula: ")
                    cedula_ususario = input("")
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
            return cedula_ususario
        except EOFError:
            return inicio_seccion_cedula()
    cedula_ususario = inicio_seccion_cedula()
        
    print("usuario registrado: ",nombre_ususario, apellido_usuario)

    time.sleep(1)

    return nombre_ususario, apellido_usuario, cedula_ususario 
    #El "return" nos permite usar las variables de "nombre_ususario, apellido_usuario, cedula_ususario"
    #en la siguiente función


def encriptacion(nombre_ususario, apellido_ususario, cedula_ususario, respuestas_examen):
    # Crear el nombre del archivo ZIP
    nombre_archivo_zip = "{}_{}_{}.zip".format(nombre_ususario, apellido_ususario, cedula_ususario)

    # Crear el nombre del archivo de texto
    nombre_archivo_txt = nombre_archivo_zip[:-4] + ".txt"

    # Escribir las respuestas en el archivo de texto
    with open(nombre_archivo_txt, "w") as archivo_txt:
        for pregunta, respuesta in zip(preguntas, respuestas_examen):
            archivo_txt.write("{}: {}\n".format(pregunta, respuesta))

    # Crear un archivo ZIP encriptado con contraseña
    with pyzipper.AESZipFile(nombre_archivo_zip, "w", compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as archivo_zip:
        archivo_zip.setpassword(b"profemirtha123")  # Establecer la contraseña
        archivo_zip.write(nombre_archivo_txt)

    # Eliminar el archivo de texto
    os.remove(nombre_archivo_txt)

    def send_email(subject, message, from_addr, to_addr, password, file_path):
        #La función crea un mensaje MIME multiparte (MIMEMultipart) utilizando la biblioteca email.
        msg = MIMEMultipart()
        #Se establecen los encabezados del mensaje:
        #From: Dirección del remitente.
        #To: Dirección del destinatario.
        #Subject: Asunto del correo electrónico.
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = subject

        #Se agrega el cuerpo del mensaje como texto plano (MIMEText) al mensaje principal.
        msg.attach(MIMEText(message, 'plain'))

        # Adjuntar archivo
        attachment = open(file_path, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename= ' + file_path)

        msg.attach(part)

        try:
            # Iniciar sesión en el servidor de correo y enviar el correo, se usa una excepciónen caso de que el envio falle 
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_addr, password)
            text = msg.as_string()
            server.sendmail(from_addr, to_addr, text)
            server.quit()
            print("Su evaluación fue enviada al correo de la profesora exitosamente")
        except:
            print("No se ha podido enviar su evaluación, por favor envielo usted mismo al correo de la profesora")

    #esta es la llamada a la funcion que manda el correo
    #                                                      aqui va el corrio del proyecto-  correo de la profesora        -   esto no lo toques  -  el archivo que va a enviar
    send_email('Asunto del correo', 'Mensaje del correo', 'proyectoclassroom8@gmail.com', 'mirthaapariciocortez@gmail.com', 'msht ekje bofg aplb', nombre_archivo_zip)


#Aquí empezamos con el menú de los exámenes
def menu_principal():
    try:
        validar_corte = "no"
        borrar_pantalla()
        print("!COHORTES DISPONIBLES!")
        print('''Para cohorte 1, pulse 1
Para cohorte 2, pulse 2
Para cohorte 3, pulse 3
Para cohorte 4, pulse 4 ''')

        while validar_corte == "no":
            print("Seleccione el cohorte que va a presentar")
            corte_seleccionado = input("")
            validar_numeros_corte = validar_solo_numeros(corte_seleccionado)

            if validar_numeros_corte:
                corte_procesado = int(corte_seleccionado)
                if corte_procesado == 1:
                    contraseña = input("Ingrese la contraseña para el primer cohorte: ")
                    if contraseña == "helado123":
                        while True:
                            print("¿Está seguro que este es el cohorte que va a presentar? si/no ")
                            validar_corte_info = input("").lower()
                            validar_corte = unidecode(validar_corte_info)
                            if validar_corte == "si":
                                borrar_pantalla()
                                return primer_corte()  # Devolver las respuestas del examen

                            elif validar_corte == "no":
                                break

                            else:
                                print('''Por favor seleccione una opción válida, solo se permite "si" o "no" ''')
                                validar_corte = "no"
                    else:
                        print("Contraseña incorrecta para el primer cohorte. Inténtelo de nuevo.")
                elif corte_procesado == 2:
                    contraseña = input("Ingrese la contraseña para el segundo cohorte: ")
                    if contraseña == "Python321":
                        while True:
                            print("¿Está seguro que este es el cohorte que va a presentar? si/no ")
                            validar_corte_info = input("").lower()
                            validar_corte = unidecode(validar_corte_info)
                            if validar_corte == "si":
                                borrar_pantalla()
                                return segundo_corte()  # Devolver las respuestas del examen

                            elif validar_corte == "no":
                                break

                            else:
                                print('''Por favor seleccione una opción válida, solo se permite "si" o "no" ''')
                                validar_corte = "no"
                    else:
                        print("Contraseña incorrecta para el segundo cohorte. Inténtelo de nuevo.")
                elif corte_procesado == 3:
                    contraseña = input("Ingrese la contraseña para el tercer cohorte: ")
                    if contraseña == "tortadechocolate":
                        while True:
                            print("¿Está seguro que este es el cohorte que va a presentar? si/no ")
                            validar_corte_info = input("").lower()
                            validar_corte = unidecode(validar_corte_info)
                            if validar_corte == "si":
                                borrar_pantalla()
                                return terecer_corte()  # Devolver las respuestas del examen

                            elif validar_corte == "no":
                                break

                            else:
                                print('''Por favor seleccione una opción válida, solo se permite "si" o "no" ''')
                                validar_corte = "no"
                    else:
                        print("Contraseña incorrecta para el tercer cohorte. Inténtelo de nuevo.")
                elif corte_procesado == 4:
                    contraseña = input("Ingrese la contraseña para el cuarto cohorte: ")
                    if contraseña == "casa54321":
                        while True:
                            print("¿Está seguro que este es el cohorte que va a presentar? si/no ")
                            validar_corte_info = input("").lower()
                            validar_corte = unidecode(validar_corte_info)
                            if validar_corte == "si":
                                borrar_pantalla()
                                return cuarto_corte()  # Devolver las respuestas del examen

                            elif validar_corte == "no":
                                break

                            else:
                                print('''Por favor seleccione una opción válida, solo se permite "si" o "no" ''')
                                validar_corte = "no"
                    else:
                        print("Contraseña incorrecta para el cuarto cohorte. Inténtelo de nuevo.")
                else:
                    print("Opcion no valida,intentelo nuevamente")
            else:
                print("Solo se permiten numeros,intentelo nuevamente")
    except EOFError:
        return menu_principal()
            
def presentar_pregunta(enunciado, opciones):
    print(enunciado)
    if opciones:  # Si hay opciones, es una pregunta de opción múltiple
        for i, opcion in enumerate(opciones, start=1):
            print(f"{i}. {opcion}")

def validar_respuesta(opciones):
    while True:
        respuesta = input("Seleccione su respuesta (ingrese el número correspondiente): ")
        try:
            respuesta_numero = int(respuesta)
            if 1 <= respuesta_numero <= len(opciones):
                return respuesta_numero
            else:
                print("Por favor, ingrese un número válido.")
        except ValueError:
            # Si la conversión a entero falla, la respuesta no es un número
            print("Por favor, ingrese un número válido.")

def realizar_examen(preguntas):
    global examen_iniciado
    global respuestas_examen
    respuestas_examen = []  # Lista para almacenar todas las respuestas del examen
    examen_iniciado = True
    for pregunta in preguntas:

        def en_evaluacion():
            try:
                borrar_pantalla()
                presentar_pregunta(pregunta["enunciado"], pregunta.get("opciones", []))
                
                if pregunta["opciones"]:
                    # Pregunta de opción múltiple
                    while True:
                        respuesta = validar_respuesta(pregunta["opciones"])
                        print(f"Su respuesta fue: {pregunta['opciones'][respuesta - 1]}")  # Mostrar la respuesta seleccionada

                        # Confirmación de la respuesta
                        confirmacion = input("¿Está seguro de su respuesta? (si/no): ").lower()
                        while confirmacion not in ["si", "no"]:
                            print("Por favor, seleccione una opción válida.")
                            confirmacion = input("¿Está seguro de su respuesta? (si/no): ").lower()

                        if confirmacion == "si":
                            respuestas_examen.append(pregunta['opciones'][respuesta - 1])  # Agregar la respuesta a la lista de respuestas
                            break  # Salir del bucle si el usuario confirma su respuesta
                        elif confirmacion == "no":
                            print("Por favor, vuelva a ingresar su respuesta.")
                            continue  # Repetir la pregunta si el usuario decide cambiar su respuesta
                else:
                    #Pregunta práctica
                    print ("Pegue su respuesta, presione 'enter', luego escriba '#termine_el_examen' y vuelva a pulsar 'enter' para terminar, no escriba")
                    print ("nada más ya que puede afectar su código, en caso de que le salga un recuadro preguntando que si está seguro de pegar tantas")
                    respuesta = input("líneas en la terminal, presione en la opción 'pegar', de lo contrario se modificará su codigo y su nota se verá afectada: ")
                    respuesta_completa = respuesta  # Inicialmente, la respuesta completa es igual a la primera línea
                    
                    # Permitir al usuario ingresar múltiples líneas hasta que escriba '#termine_el_examen'
                    while respuesta.strip().lower() != "#termine_el_examen":
                        respuesta = input()  # Pedir la siguiente línea de código
                        respuesta_completa += "\n" + respuesta  # Agregar la nueva línea a la respuesta completa
                    
                    respuestas_examen.append(respuesta_completa)  # Agregar la respuesta completa a la lista de respuestas
            #Si se produce un error EOFError (se presiona Ctrl+D), se vuelve a llamar a la función en_evaluacion para reiniciar el proceso.
            #Se llama a la función en_evaluacion de forma recursiva para continuar con la siguiente pregunta (si la hay).
            except EOFError:
                return en_evaluacion()
        en_evaluacion()

    print("La evaluación ha finalizado.")
    return respuestas_examen  # Devuelve todas las respuestas al finalizar el examen

def primer_corte():
    def texto_antes_evalucion():
        try:
            borrar_pantalla()
            print("Bienvenido al primer cohorte.")
            print("Tiene 1 hora para terminar esta prueba. Si sale del programa antes de finalizar, su nota será perjudicada.")
            input("Pulse enter para iniciar la evaluación.")
        except EOFError:
            return texto_antes_evalucion()
    texto_antes_evalucion()

    #crea un hilo nuevo para ejecutar la función iniciar_temporizador en segundo plano.
    threading.Thread(target=iniciar_temporizador).start()

    # Crear un hilo para ejecutar el temporizador
    t = threading.Thread(target=temporizador_asyncrono, args=(3601,))

    # Iniciar el hilo
    t.start()

    preguntas = [
        {
            "enunciado": "¿Cuál de los siguientes es un estándar de calidad comúnmente utilizado en el diseño de algoritmos y programas?",
            "opciones": ["ISO 9001", "IEEE 754", "ANSI C", "PEP 8"]
        },
        {
            "enunciado": "¿Qué tipo de estructura de control se utiliza para ejecutar un bloque de código repetidamente hasta que se cumple una condición?",
            "opciones": ["Estructura condicional", "Ciclo Mientras", "Ciclo Para", "Selección múltiple"]
        },
        {
            "enunciado": "¿Cuál de las siguientes opciones describe mejor la documentación de algoritmos y programas?",
            "opciones": ["Comentarios detallados en el código fuente", "Notas escritas a mano al final del documento", "Ninguna documentación es necesaria", "Publicación en un blog personal"]
        },
        {
            "enunciado": "¿Qué tipo de estructura de control se utiliza para realizar una acción si se cumple una condición o una acción diferente si no se cumple?",
            "opciones": ["Estructura de control iterativa", "Ciclo Para", "Estructura condicional doble", "Ciclo Repetir"]
        },
        # Agregar más preguntas de opción múltiple aquí
        {
            "enunciado": "Pregunta práctica: Diseña un algoritmo en pseudocódigo que calcule el promedio de tres números ingresados por el usuario y muestra el resultado",
            "opciones": []  # No hay opciones para esta pregunta
        }
    ]

    return realizar_examen(preguntas)

def segundo_corte ():
    print("Bienvenido al segundo cohorte.")
    print("Tiene 1 hora para terminar esta prueba. Si sale del programa antes de finalizar, su nota será perjudicada.")
    input("Pulse enter para iniciar la evaluación.")

    #crea un hilo nuevo para ejecutar la función iniciar_temporizador en segundo plano.
    threading.Thread(target=iniciar_temporizador).start()

    # Crear un hilo para ejecutar el temporizador
    t = threading.Thread(target=temporizador_asyncrono, args=(3601,))

    # Iniciar el hilo
    t.start()

    preguntas = [
        {
            "enunciado": "Cuál de las siguientes opciones describe mejor una función en programación?",
            "opciones": ["Una secuencia de comandos que se ejecuta automáticamente cuando se inicia un programa.", "Un bloque de código reutilizable que realiza una tarea específica.", "Una estructura de datos que almacena información sobre un objeto.", "Un tipo de variable que almacena una colección de valores."]
        },
        {
            "enunciado": "¿Cuál es la diferencia principal entre una variable local y una variable global en un programa?",
            "opciones": ["Las variables locales solo se pueden utilizar en una función específica, mientras que las globales se pueden usar en todo el programa.", "Las variables locales se pueden modificar en cualquier parte del programa, mientras que las globales no se pueden modificar.", "Las variables globales solo se pueden utilizar en una función específica, mientras que las locales se pueden usar en todo el programa.", "No hay diferencia, los términos se utilizan indistintamente."]
        },
        {
            "enunciado": "¿Cuál es la función utilizada para obtener la longitud de una cadena en Python?",
            "opciones": ["length()", "len()", "size()", "count()"]
        },
        {
            "enunciado": "¿Cuál de las siguientes operaciones no se puede realizar con cadenas de caracteres en Python?",
            "opciones": ["Concatenación", "División", "Búsqueda de subcadenas", "Extracción de caracteres por índice"]
        },
        # Agregar más preguntas de opción múltiple aquí
        {
            "enunciado": "Pregunta práctica: Escribe una función en Python llamada “reverso_cadena” que tome una cadena como argumento y devuelva la cadena invertida. Por ejemplo, si la cadena de entrada es 'hola', la función debería devolver 'aloh'.",
            "opciones": []  # No hay opciones para esta pregunta
        }
    ]
    return realizar_examen(preguntas)

def terecer_corte ():
    print("Bienvenido al tercer cohorte.")
    print("Tiene 1 hora para terminar esta prueba. Si sale del programa antes de finalizar, su nota será perjudicada.")
    input("Pulse enter para iniciar la evaluación.")

    #crea un hilo nuevo para ejecutar la función iniciar_temporizador en segundo plano.
    threading.Thread(target=iniciar_temporizador).start()

    # Crear un hilo para ejecutar el temporizador
    t = threading.Thread(target=temporizador_asyncrono, args=(3601,))

    # Iniciar el hilo
    t.start()

    preguntas = [
        {
            "enunciado": "¿Cuál de los siguientes métodos se utiliza para buscar un elemento específico en un arreglo? ",
            "opciones": ["Búsqueda binaria", "Ordenamiento por selección", "Búsqueda secuencial", "Ordenamiento por inserción"]
        },
        {
            "enunciado": "¿Cómo se conocen comúnmente los arreglos en programación?",
            "opciones": ["Listas", "Matrices", "Vectores", "Arrays"]
        },
        {
            "enunciado": "¿Qué es un arreglo en programación?",
            "opciones": ["Una colección de variables del mismo tipo accesibles con un índice", "Una función especializada en la búsqueda de elementos", "Un tipo de bucle utilizado para iterar sobre colecciones", "Una estructura de datos que almacena información en pares clave-valor"]
        },
        # Agregar más preguntas de opción múltiple aquí
        {
            "enunciado": "Pregunta práctica: Implementa una función en lenguaje Python que reciba como entrada un arreglo de números enteros y determine si existe un par de elementos en el arreglo cuya suma sea igual a un valor objetivo dado. Si se encuentra dicho par, la función debe devolver los índices de los elementos. Si no se encuentra ningún par, la función debe retornar un mensaje indicando que no existe tal par",
            "opciones": []  # No hay opciones para esta pregunta
        }
    ]
    return realizar_examen(preguntas)

def cuarto_corte ():
    print("Bienvenido al cuarto cohorte.")
    print("Tiene 1 hora para terminar esta prueba. Si sale del programa antes de finalizar, su nota será perjudicada.")
    input("Pulse enter para iniciar la evaluación.")

    #crea un hilo nuevo para ejecutar la función iniciar_temporizador en segundo plano.
    threading.Thread(target=iniciar_temporizador).start()

    # Crear un hilo para ejecutar el temporizador
    t = threading.Thread(target=temporizador_asyncrono, args=(3601,))

    # Iniciar el hilo
    t.start()

    preguntas = [
        {
            "enunciado": "¿Qué es un archivo en el contexto de la informática?",
            "opciones": ["Un programa de software", "Una unidad de almacenamiento", "Una colección de datos almacenados y accesibles digitalmente", "Un tipo de hardware"]
        },
        {
            "enunciado": "¿Cuál de las siguientes opciones describe mejor la estructura de un archivo de texto?",
            "opciones": ["Secuencia de bytes sin formato específico", "Secuencia de caracteres organizados generalmente en líneas", "Conjunto de imágenes y gráficos", "Bloques de datos cifrados"]
        },
        {
            "enunciado": "¿Qué tipo de archivo está diseñado principalmente para ser interpretado por un programa en lugar de ser leído directamente por un humano?",
            "opciones": ["Archivo de texto", "Archivo de datos", "Archivo de imagen", "Archivo de audio"]
        },
        # Agregar más preguntas de opción múltiple aquí
        {
            "enunciado": "Pregunta práctica: En el contexto de una aplicación de gestión de biblioteca, se requiere implementar una funcionalidad que permita registrar la información de nuevos libros y recuperar los datos cuando sea necesario. Escribe un script en Python que realice las siguientes tareas: Creación de un archivo de texto llamado `libros.txt` que almacenará los datos de los libros, Función para agregar libros: Define una función `agregar_libro(titulo, autor, año)` que reciba el título, el autor y el año de publicación de un libro y lo guarde en el archivo `libros.txt`. Cada libro debe registrarse en una nueva línea y los datos deben estar separados por comas, Función para leer libros: Define una función `leer_libros()` que lea el archivo `libros.txt` y muestre en consola la lista de libros registrados, cada uno con su respectivo título, autor y año de publicación.",
            "opciones": []  # No hay opciones para esta pregunta
        }
    ]
    return realizar_examen(preguntas)

def main():

    #Hace global la variable en donde se almacenan los datos del usuario para que cualquier funcion pueda acceder a ellos
    global usuario

    #obtiene los datos personales del usuario
    nombre_ususario, apellido_usuario, cedula_ususario = inicio_seccion()

    #Hace una lista con los datos del usuario 
    usuario = [nombre_ususario, apellido_usuario , cedula_ususario]

    #lleva al usuario a seleccionar el cohorte a presentar
    respuestas_examen = menu_principal()

    #Comprime/encripta los datos
    salir_programa()

if __name__ == "__main__":
     main()

#La función "main()" nos ayuda a hacer que cada una de las demás funciones se ejecute en el orden que deben y en la forma
#en la que deben hacerlo ya que "if __name__ == "__main__"" nos permite hacer seguir a las funciones el orden de ejecución
#pautado por el programador, activandose cuando el script se ejecuta como el programa principal
