#biblioteca para comprimir los datos con contraseña (similiar a la encriptacion)
import pyzipper
#biblioteca que se usará para controlar el tiempo
import time
#libreria para enviar los correos de forma automatica
import smtplib
#libreria para quitar los acentos
from unidecode import unidecode
# las funciones presentadas a continuacion no esta siendo usada dentro del codigo, se deben implementar.
################!!!!!!!!!!!!!
# deben almacenar la funcion dentro de la variable para poder octener el valor retornado

#validar_alfanumerico fue creado en caso de que se necesite en un futuro
def validar_alfanumerico(dato_input):

    #extrae la longitud del dato
    caracteres = len(dato_input)

    #esta es la parte encargada de detectar numeros y letras 
    tipo = dato_input.isalnum()
    if tipo == True:
        if caracteres >= 2 and caracteres <= 12:
            dato_valido_input = True
            return dato_valido_input

#validar_nombre fue creado para validar el nombre 
def validar_nombre(dato_input):

    #extrae la longitud del dato
    caracteres = len(dato_input)

    #esta es la parte encargada de detectar letras 
    tipo = dato_input.isalpha()
    if tipo == True:
        if caracteres >= 3 and caracteres <= 20:
            dato_valido_input = True
            return dato_valido_input


#validar_cedula fue creado para validar la cedula
def validar_cedula(dato_input):
        
    #extrae la longitud del dato
    caracteres = len(dato_input)

    #esta es la parte encargada de detectar numeros
    tipo = dato_input.isdigit()
    if tipo == True:
        if caracteres == 8:
            dato_valido_input = True
            return dato_valido_input

#############!!!!!!!!!!!!!!!!!!!

def inicio_seccion ():
    print('''Bienvenido al proyecto classroom, para iniciar primero inserte sus datos''')

    sertificar_nombre = "0"
    while sertificar_nombre == "0" :
        nombre_ususario = input('Por favor ingrese su nombre (solo primer nombre): ')
        validar_nombre_usuario = validar_nombre(nombre_ususario)

        while validar_nombre_usuario != True:
            print("Por favor vuelva a ingresar su nombre, su nombre debe contar con entre 3 a 20 letras")
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
            print("Por favor vuelva a ingresar su apellido, su apellido debe contar con entre 3 a 20 letras")
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
            print("Por favor vuelva a ingresar su cédula, su cédula debe contar con 8 números")
            cedula_ususario = input('Por favor ingrese nuevamente su cedula: ')
            validar_nombre_cedula = validar_cedula(cedula_ususario)
        
        sertificar_cedula = input ('''La cédula que ha ingresiado es: '''+ cedula_ususario+'''.
        Si esta no es su cédula o ha cometido un error al escribirla presione "0", 
        si la cedula que ingresó es valida pulse una tecla que no sea "0" ''' )

        return nombre_ususario, apellido_usuario, cedula_ususario 

def encriptacion (nombre_ususario, apellido_usuario, cedula_ususario, respuestas):
        
    #se crea el archivo con los datos del usuario
        nombre_archivo = f"{nombre_ususario}_{apellido_usuario}_{cedula_ususario}.zip"

    # Guardar respuestas en el archivo ZIP con contraseña
        with pyzipper.AESZipFile(nombre_archivo, 'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zf:

        #Contraseña proporcionada por el profesor
            contraseña_profesor = b"profemirtha123"
            zf.setpassword(contraseña_profesor)
    
        # Concatenar todas las respuestas en una sola cadena
            respuestas_concatenadas = "\n".join(respuestas)
    
        # Escribir todas las respuestas en un solo archivo dentro del ZIP
            zf.writestr(f"{nombre_ususario}_{apellido_usuario}_{cedula_ususario}.txt", respuestas_concatenadas)

def main():
    #obtiene los datos personales del usuario
    nombre_ususario, apellido_usuario, cedula_ususario = inicio_seccion()

    #obtiene las respuestas del usuario
    respuestas = ["respuesta1", "respuesta2", "respuesta3", "respuesta4"]

    #comprime/encripta los datos
    encriptacion(nombre_ususario, apellido_usuario, cedula_ususario, respuestas)

#if __name__ == "__main__":
    #main()

def enviarCorreo ():
    
    #mensaje que se enviara
    mensaje = 'colocar aqui el mensaje'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    #datos para que la libreria pueda acceder a el correo del remitente
    server.login('correo','contraseña')

    # remitente, destinatario, mensaje
    server.send_message('correo del remitente','correo del destinatario',mensaje)

    #cierra secion
    server.quit()
    

######################
def menu_principal ():
    validar_corte = "no"
    while validar_corte == "no":
        print("!SELECCIONE EL CORTE QUE VA A PRESENTAR!")
        print('''para corte 1, pulse 1
        para corte 2, pulse 2
        para corte 3, pulse 3
        para corte 4, pulse 4    ''')
        corte_selecionado = int(input(""))

        if corte_selecionado == 1:
            while True:
                validar_corte_info = input("Esta seguro que este es el corte que va a presentar? si/no").lower()
                validar_corte = unidecode(validar_corte_info)
                if validar_corte == "si":
                    primer_corte()
                    break

                elif validar_corte == "no":
                    break

                else:
                    print("por favor selecciones una occion valida, solo se pernite si o no")
                    validar_corte = False
                
        elif corte_selecionado == 2:
            segundo_corte()
        elif corte_selecionado == 3:
            terecer_corte()
        elif corte_selecionado == 4:
            cuarto_corte()

        else:
            print("por favor selecione una opcion valida")

def primer_corte ():
    print("selecciono primer corte")
    print("tiene X tiempo para terminar esta prueba. Si sale de esta prueva su nota sera perjudicada")

    divicion_estetica = input("pulse cualquier tecla para iniciar la evaluacion")

    print("enunciado")
    print("la respuesta correcta es:")
    print("pregunta 1")
    print("pregunta 2")
    print("pregunta 3")
    print("pregunta 4")
    while True:
        respuesta_uno_corte_uno = int(input(""))
        validar_respuesta_uno_corte_uno = input(f"su respuesta fue: {respuesta_uno_corte_uno} . esta seguro de su respues? si/no")
        if validar_respuesta_uno_corte_uno == "no":
            print("porfavor vuelva a insertar su respues")
        elif validar_respuesta_uno_corte_uno == "si":
            break
        else:
            print("por favor selecciones una occion valida, solo se pernite si o no")

    print("enunciado")
    print("la respuesta correcta es:")
    print("pregunta 1")
    print("pregunta 2")
    print("pregunta 3")
    print("pregunta 4")
    respuesta_uno_corte_uno = input("")

    print("enunciado")
    print("la respuesta correcta es:")
    print("pregunta 1")
    print("pregunta 2")
    print("pregunta 3")
    print("pregunta 4")
    respuesta_uno_corte_uno = input("")

    print("enunciado")
    print("la respuesta correcta es:")
    print("pregunta 1")
    print("pregunta 2")
    print("pregunta 3")
    print("pregunta 4")
    respuesta_uno_corte_uno = input("")

    print("enunciado")
    print("la respuesta correcta es:")
    print("pregunta 1")
    print("pregunta 2")
    print("pregunta 3")
    print("pregunta 4")
    respuesta_uno_corte_uno = input("")

    print("la evaluacion a finalizado")



def segundo_corte ():
    print("selecciono segundo corte")

def terecer_corte ():
    print("selecciono tercero corte")

def cuarto_corte ():
    print("selecciono cuarto corte")

menu_principal()