#Librería para comprimir los datos con contraseña (similiar a la encriptacion)
import pyzipper
#Librería que se usará para controlar el tiempo
import time
#Librería para enviar los correos de forma automática
import smtplib
#Librería para quitar los acentos
from unidecode import unidecode

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
    print('''Bienvenido al PROYECTO CLASSROOM, para iniciar primero inserte sus datos''')

    #Esta parte del codigo es la encargada de pedirle los datos personales al usuario y hacerlo CERTIFICAR
    #que estén correctos (Alejandro escribe mal la variables a proposito para que se vean más originales)
    sertificar_nombre = "0"
    while sertificar_nombre == "0" :
        nombre_ususario = input('Por favor ingrese su nombre (solo primer nombre): ')
        validar_nombre_usuario = validar_nombre(nombre_ususario)
        #Con el "while" hacemos los bucles para que se le vuelva a preguntar al usuario por alguno de sus
        #datos en caso de algún error
        while validar_nombre_usuario != True:
            print("Por favor vuelva a ingresar su nombre, su nombre debe contar con entre 3 a 20 letras ")
            nombre_ususario = input('Por favor ingrese nuevamente su nombre (solo primer nombre): ')
            validar_nombre_usuario = validar_nombre(nombre_ususario)
        
        sertificar_nombre = input ('''El nombre que ha ingresado es: '''+ nombre_ususario+'''.
        Si este no es su nombre o ha cometido un error al escribirlo presione "0", 
        si el nombre que ingreso es valido pulse una tecla que no sea "0" ''')
    
    sertificar_apellido = "0"
    while sertificar_apellido == "0" :
        apellido_usuario = input('Por favor ingrese su apellido: ')
        validar_nombre_apellido = validar_nombre(apellido_usuario)

        while validar_nombre_apellido != True:
            print("Por favor vuelva a ingresar su apellido, su apellido debe contar con entre 3 a 20 letras ")
            apellido_usuario = input('por favor ingrese nuevamene su apellido: ')
            validar_nombre_apellido = validar_nombre(apellido_usuario)

        sertificar_apellido = input ('''El apellido que ha ingresado es: '''+ apellido_usuario+'''.
       Si este no es su apellido o ha cometido un error al escribirlo presione "0", 
       si el apellido que ingresó es valido pulse una tecla que no sea "0" ''' )

    sertificar_cedula = "0"
    while sertificar_cedula == "0" :
        cedula_ususario = input('Por favor ingrese su cédula: ')
        validar_nombre_cedula = validar_cedula(cedula_ususario)

        while validar_nombre_cedula != True:
            print("Por favor vuelva a ingresar su cédula, su cédula debe contar con 8 números ")
            cedula_ususario = input('Por favor ingrese nuevamente su cedula: ')
            validar_nombre_cedula = validar_cedula(cedula_ususario)
        
        sertificar_cedula = input ('''La cédula que ha ingresiado es: '''+ cedula_ususario+'''.
        Si esta no es su cédula o ha cometido un error al escribirla presione "0", 
        si la cedula que ingresó es valida pulse una tecla que no sea "0" ''' )

        #El "return" nos permite usar las variables de "nombre_ususario, apellido_usuario, cedula_ususario"
        #en la siguiente función
        return nombre_ususario, apellido_usuario, cedula_ususario 

def encriptacion (nombre_ususario, apellido_usuario, cedula_ususario, respuestas):
        
     #Se crea el archivo que lleva por nombre los datos del usuario
        nombre_archivo = f"{nombre_ususario}_{apellido_usuario}_{cedula_ususario}.zip"

    #Guarda las respuestas en el archivo ZIP con contraseña
        with pyzipper.AESZipFile(nombre_archivo, 'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zf:

        #Contraseña de los archivos ZIP (se puede cambiar)
            contraseña_profesor = b"profemirtha123"
            zf.setpassword(contraseña_profesor)
    
        #Pone todas las respuestas en una sola cadena
            respuestas_concatenadas = "\n".join(respuestas)
    
        #Escribe todas las respuestas en un solo archivo dentro del ZIP
            zf.writestr(f"{nombre_ususario}_{apellido_usuario}_{cedula_ususario}.txt", respuestas_concatenadas)

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
    #personales lleguen a su correo (al de usted) de forma instantanea

#Aquí empezamos con el menú de los exámenes
def menu_principal ():
    validar_corte = "no"
    while validar_corte == "no":
        print("!SELECCIONE EL COHORTE QUE VA A PRESENTAR!")
        print('''        Para corte 1, pulse 1
        Para corte 2, pulse 2
        Para corte 3, pulse 3
        Para corte 4, pulse 4 ''')
        corte_selecionado = int(input(""))

        if corte_selecionado == 1:
            while True:
                #Con el ".lower" se asegura que sin importar como escriban el "si/no" sea tomado como bueno igual
                validar_corte_info = input("¿Está seguro que este es el cohorte que va a presentar? si/no ").lower()
                validar_corte = unidecode(validar_corte_info)
                if validar_corte == "si":
                    primer_corte()
                    break

                elif validar_corte == "no":
                    break

                else:
                    print('''Por favor seleccione una opción válida, solo se pemite "si" o "no" ''')
                    validar_corte = False
                
        elif corte_selecionado == 2:
            segundo_corte()
        elif corte_selecionado == 3:
            terecer_corte()
        elif corte_selecionado == 4:
            cuarto_corte()

        else:
            print("Por favor selecione una opción válida ")
        #Se le da a escoger al usuario qué cohorte va a presentar, se le hace que valide por si se equivoca
        #y lo manda a corregir si no selecciona ninguno
            
def primer_corte ():
    print("Seleccionó el primer cohorte")
    print("Tiene X tiempo para terminar esta prueba. Si sale del programa antes finalizar su nota será perjudicada")

    divicion_estetica = input("Pulse cualquier tecla para iniciar la evaluación ")

    print("enunciado")
    print("¿Cuál de las respuestas es la correcta?:")
    print("Respuesta 1")
    print("Respuesta 2")
    print("Respuesta 3")
    print("Respuesta 4")

    #este bucle while sertifica que la repuesta sea un numero y que el usuario este seguro de su decicion
    while True:
        respuesta_uno_corte_uno_procesado = input("")
        if respuesta_uno_corte_uno_procesado.isdigit():
            respuesta_uno_corte_uno = int(respuesta_uno_corte_uno_procesado)
            print(f"Su respuesta fue: {respuesta_uno_corte_uno}")
            while True:
                validar_respuesta_uno_corte_uno_procesado = input("Esta seguro de su respuesta? si/no ").lower()
                validar_respuesta_uno_corte_uno = unidecode(validar_respuesta_uno_corte_uno_procesado)

                if validar_respuesta_uno_corte_uno == "no":
                    print("Por favor vuelva a seleccionar su respuesta ")
                    break
                elif validar_respuesta_uno_corte_uno == "si":
                    break
                else:
                    print('''Por favor seleccione una opción válida, solo se pemite "si" o "no" ''')
                
            if validar_respuesta_uno_corte_uno == "si":
                break
        else:
            print("por favor seleccione una opcion valida")

    print("enunciado")
    print("la respuesta correcta es:")
    print("pregunta 1")
    print("pregunta 2")
    print("pregunta 3")
    print("pregunta 4")
    while True:
        respuesta_dos_corte_uno_procesado = input("")
        if respuesta_dos_corte_uno_procesado.isdigit():
            respuesta_dos_corte_uno = int(respuesta_dos_corte_uno_procesado)
            print(f"Su respuesta fue: {respuesta_dos_corte_uno}")
            while True:
                validar_respuesta_dos_corte_uno_procesado = input("Esta seguro de su respuesta? si/no ").lower()
                validar_respuesta_dos_corte_uno = unidecode(validar_respuesta_dos_corte_uno_procesado)

                if validar_respuesta_dos_corte_uno == "no":
                    print("Por favor vuelva a seleccionar su respuesta ")
                    break
                elif validar_respuesta_dos_corte_uno == "si":
                    break
                else:
                    print('''Por favor seleccione una opción válida, solo se pemite "si" o "no" ''')
                
            if validar_respuesta_dos_corte_uno == "si":
                break
        else:
            print("por favor seleccione una opcion valida")

    print("enunciado")
    print("la respuesta correcta es:")
    print("pregunta 1")
    print("pregunta 2")
    print("pregunta 3")
    print("pregunta 4")
    while True:
        respuesta_tres_corte_uno_procesado = input("")
        if respuesta_tres_corte_uno_procesado.isdigit():
            respuesta_tres_corte_uno = int(respuesta_tres_corte_uno_procesado)
            print(f"Su respuesta fue: {respuesta_tres_corte_uno}")
            while True:
                validar_respuesta_tres_corte_uno_procesado = input("Esta seguro de su respuesta? si/no ").lower()
                validar_respuesta_tres_corte_uno = unidecode(validar_respuesta_tres_corte_uno_procesado)

                if validar_respuesta_tres_corte_uno == "no":
                    print("Por favor vuelva a seleccionar su respuesta ")
                    break
                elif validar_respuesta_tres_corte_uno == "si":
                    break
                else:
                    print('''Por favor seleccione una opción válida, solo se pemite "si" o "no" ''')
                
            if validar_respuesta_tres_corte_uno == "si":
                break
        else:
            print("por favor seleccione una opcion valida")

    print("enunciado")
    print("la respuesta correcta es:")
    print("pregunta 1")
    print("pregunta 2")
    print("pregunta 3")
    print("pregunta 4")
    while True:
        respuesta_cuatro_corte_uno_procesado = input("")
        if respuesta_cuatro_corte_uno_procesado.isdigit():
            respuesta_cuatro_corte_uno = int(respuesta_cuatro_corte_uno_procesado)
            print(f"Su respuesta fue: {respuesta_cuatro_corte_uno}")
            while True:
                validar_respuesta_cuatro_corte_uno_procesado = input("Esta seguro de su respuesta? si/no ").lower()
                validar_respuesta_cuatro_corte_uno = unidecode(validar_respuesta_cuatro_corte_uno_procesado)

                if validar_respuesta_cuatro_corte_uno == "no":
                    print("Por favor vuelva a seleccionar su respuesta ")
                    break
                elif validar_respuesta_cuatro_corte_uno == "si":
                    break
                else:
                    print('''Por favor seleccione una opción válida, solo se pemite "si" o "no" ''')
                
            if validar_respuesta_cuatro_corte_uno == "si":
                break
        else:
            print("por favor seleccione una opcion valida")

    print("enunciado")
    print("la respuesta correcta es:")
    print("pregunta 1")
    print("pregunta 2")
    print("pregunta 3")
    print("pregunta 4")
    while True:
        respuesta_cinco_corte_uno_procesado = input("")
        if respuesta_cinco_corte_uno_procesado.isdigit():
            respuesta_cinco_corte_uno = int(respuesta_cinco_corte_uno_procesado)
            print(f"Su respuesta fue: {respuesta_cinco_corte_uno}")
            while True:
                validar_respuesta_cinco_corte_uno_procesado = input("Esta seguro de su respuesta? si/no ").lower()
                validar_respuesta_cinco_corte_uno = unidecode(validar_respuesta_cinco_corte_uno_procesado)

                if validar_respuesta_cinco_corte_uno == "no":
                    print("Por favor vuelva a seleccionar su respuesta ")
                    break
                elif validar_respuesta_cinco_corte_uno == "si":
                    break
                else:
                    print('''Por favor seleccione una opción válida, solo se pemite "si" o "no" ''')
                
            if validar_respuesta_cinco_corte_uno == "si":
                break
        else:
            print("por favor seleccione una opcion valida")

    print("la evaluacion a finalizado")

def segundo_corte ():
    print("selecciono segundo corte")

def terecer_corte ():
    print("selecciono tercero corte")

def cuarto_corte ():
    print("selecciono cuarto corte")
#En esta función (menu_principal ()) estarán definidos los 4 cohortes/examenes que podrán presentar los alumnos,
#esta parte aún no está terminada así que es probable que tenga errores, así como también puede estar
#sujeta a cambios, actualmente es en esta función en la que estamos trabajando

def main():

    #obtiene los datos personales del usuario
    nombre_ususario, apellido_usuario, cedula_ususario = inicio_seccion()

    #lleva al usuario a seleccionar el corte a presentar
    menu_principal()

    #obtiene las respuestas del usuario
    respuestas = ["respuesta1", "respuesta2", "respuesta3", "respuesta4"]

    #comprime/encripta los datos
    encriptacion(nombre_ususario, apellido_usuario, cedula_ususario, respuestas)

if __name__ == "__main__":
     main()

#La función "main()" nos ayuda a hacer que cada una de las demás funciones se ejecute en el orden que deben y en la forma
#en la que deben hacerlo ya que "if __name__ == "__main__"" nos permite hacer seguir a las funciones el orden de ejecución
#pautado por el programador, activandose cuando el script se ejecuta como el programa principal