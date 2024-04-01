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
#Libreria que nos ayuda a crear el modal del temporizador
import tkinter as tk
#Libreria que nos permitio integrar el relog al codigo, permite que el relog se ejecute "aparte" del menu
import threading
#Libreria usada para crear el modal de cerrar seccion
from tkinter import messagebox
#Libreria empleada para detectar que teclas se precionan
import signal

#Librerias del correo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

preguntas = ["Pregunta 1", "Pregunta 2", "Pregunta 3", "Pregunta 4", "Pregunta 5", "Pregunta 6", "Pregunta 7", "Pregunta 8", "Pregunta 9", "Pregunta 10"]
examen_iniciado = False
corriendo = True
usuario = []
seguro_crito = True
respuestas_examen = []
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

def mostrar_bienvenida():
    global mensaje_bienvenida
    mensaje_bienvenida = tk.Tk()
    mensaje_bienvenida.geometry("-50+20")
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

def signal_handler(sig, frame):
    print("")
    t = threading.Thread(target=modal_salir)
    t.start()

signal.signal(signal.SIGINT, signal_handler)

def borrar_pantalla():
    sistema_operativo = os.name

    if sistema_operativo == 'posix':
        os.system('clear')
    elif sistema_operativo == 'nt':
        os.system('cls')

def salir_programa():
    global respuestas_examen
    global seguro_crito
    global corriendo
    
    borrar_pantalla()
    if examen_iniciado and seguro_crito:
        nombre_ususario = usuario[0]
        apellido_usuario = usuario[1]
        cedula_ususario = usuario[2]
        encriptacion(nombre_ususario, apellido_usuario, cedula_ususario, respuestas_examen)
        seguro_crito = False
        corriendo = False
        borrar_pantalla()
        print("Evaluación finalizada")

    print("Terminando el programa...")
    exit()

def temporizador_asyncrono(segundos):
    global corriendo
    while segundos and corriendo: 
        time.sleep(1)
        segundos -= 1
    salir_programa()

def temporizador(segundos, label, root):
    global corriendo
    while segundos and corriendo: 
        mins = segundos // 60
        secs = segundos % 60
        tiempo_restante = f'{mins:02d}:{secs:02d}'
        label.config(text=tiempo_restante)
        time.sleep(1)
        segundos -= 1
        if segundos == 600:
            tk.messagebox.showinfo("Alerta de tiempo", "Te faltan 10 minutos")
        elif segundos == 300:  
            tk.messagebox.showinfo("Alerta de tiempo", "Te faltan 5 minutos")
        elif segundos == 60: 
            tk.messagebox.showinfo("Alerta de tiempo", "Te faltan 1 minuto!!")
    root.destroy()

def iniciar_temporizador():
    global corriendo
    corriendo = True
    root = tk.Tk()
    root.geometry("+50+20")
    root.title("Temporizador")

    # Deshabilitar el botón de cierre para que el alumno no cierre el cronometro por accidente
    root.protocol("WM_DELETE_WINDOW", lambda: None)

    label = tk.Label(root, text="", width=10)
    label.pack()

    segundos = 30
    threading.Thread(target=temporizador, args=(segundos, label, root)).start()

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

    def inicio_seccion_nombre():
        try:
            borrar_pantalla()
            print('''Bienvenido al PROYECTO CLASSROOM, para iniciar primero inserte sus datos''')

            #Esta parte del codigo es la encargada de pedirle los datos personales al usuario y hacerlo CERTIFICAR
            #que estén correctos (Alejandro escribe mal la variables a proposito para que se vean más originales)
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
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    # Adjuntar archivo
    attachment = open(file_path, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= ' + file_path)

    msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_addr, password)
        text = msg.as_string()
        server.sendmail(from_addr, to_addr, text)
        server.quit()
        print("Correo con su evaluacion enviado exitosamente")
    except:
        print("No se ha podido enviar su evaluación, por favor hágalo usted mismo")

#esta es la llamada a la funcion que manda el correo
#                                                      aqui va el corrio del proyecto-  correo de la profesora        -   esto no lo toques  -  el archivo que va a enviar
#send_email('Asunto del correo', 'Mensaje del correo', 'proyectoclassroom8@gmail.com', 'alejandrofenomeno72@gmail.com', 'msht ekje bofg aplb', 'relog2.py')


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

    threading.Thread(target=iniciar_temporizador).start()

    # Crear un hilo para ejecutar el temporizador
    t = threading.Thread(target=temporizador_asyncrono, args=(31,))

    # Iniciar el hilo
    t.start()

    preguntas = [
        {
            "enunciado": "pregunta 1, ¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]
        },
        {
            "enunciado": "pregunta 2, ¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]
        },
        {
            "enunciado": "pregunta 3, ¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]
        },
        # Agregar más preguntas de opción múltiple aquí
        {
            "enunciado": "Pregunta práctica: Haz una calculadora usando Python y pega el código aquí",
            "opciones": []  # No hay opciones para esta pregunta
        }
    ]

    return realizar_examen(preguntas)

def segundo_corte ():
    print("Bienvenido al segundo cohorte.")
    print("Tiene 1 hora para terminar esta prueba. Si sale del programa antes de finalizar, su nota será perjudicada.")
    input("Pulse enter para iniciar la evaluación.")

    threading.Thread(target=iniciar_temporizador).start()

    # Crear un hilo para ejecutar el temporizador
    t = threading.Thread(target=temporizador_asyncrono, args=(31,))

    # Iniciar el hilo
    t.start()

    preguntas = [
        {
            "enunciado": "pregunta 1, ¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]
        },
        {
            "enunciado": "pregunta 2, ¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]
        },
        {
            "enunciado": "pregunta 3, ¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]
        },
        # Agregar más preguntas de opción múltiple aquí
        {
            "enunciado": "Pregunta práctica: Haz una calculadora usando Python y pega el código aquí",
            "opciones": []  # No hay opciones para esta pregunta
        }
    ]
    return realizar_examen(preguntas)

def terecer_corte ():
    print("Bienvenido al tercer cohorte.")
    print("Tiene 1 hora para terminar esta prueba. Si sale del programa antes de finalizar, su nota será perjudicada.")
    input("Pulse enter para iniciar la evaluación.")

    threading.Thread(target=iniciar_temporizador).start()

    # Crear un hilo para ejecutar el temporizador
    t = threading.Thread(target=temporizador_asyncrono, args=(31,))

    # Iniciar el hilo
    t.start()

    preguntas = [
        {
            "enunciado": "pregunta 1, ¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]
        },
        {
            "enunciado": "pregunta 2, ¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]
        },
        {
            "enunciado": "pregunta 3, ¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]
        },
        # Agregar más preguntas de opción múltiple aquí
        {
            "enunciado": "Pregunta práctica: Haz una calculadora usando Python y pega el código aquí",
            "opciones": []  # No hay opciones para esta pregunta
        }
    ]
    return realizar_examen(preguntas)

def cuarto_corte ():
    print("Bienvenido al cuarto cohorte.")
    print("Tiene 1 hora para terminar esta prueba. Si sale del programa antes de finalizar, su nota será perjudicada.")
    input("Pulse enter para iniciar la evaluación.")

    threading.Thread(target=iniciar_temporizador).start()

    # Crear un hilo para ejecutar el temporizador
    t = threading.Thread(target=temporizador_asyncrono, args=(31,))

    # Iniciar el hilo
    t.start()

    preguntas = [
        {
            "enunciado": "pregunta 1, ¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]
        },
        {
            "enunciado": "pregunta 2, ¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]
        },
        {
            "enunciado": "pregunta 3, ¿Cuál de las siguientes opciones es la correcta?",
            "opciones": ["Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta 4"]
        },
        # Agregar más preguntas de opción múltiple aquí
        {
            "enunciado": "Pregunta práctica: Haz una calculadora usando Python y pega el código aquí",
            "opciones": []  # No hay opciones para esta pregunta
        }
    ]
    return realizar_examen(preguntas)

def main():

    #Hace global la variable en donde se almacenan los datos del usuario para que cualquier funcion pueda acceder a ellos
    global usuario

    #obtiene los datos personales del usuario
    nombre_ususario, apellido_usuario, cedula_ususario = inicio_seccion()

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