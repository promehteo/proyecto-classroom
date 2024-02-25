#biblioteca de encriptación
from cryptography.fernet import Fernet
import time
#se usa para borrar el archivo sin encriptar
import os

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
        nombre_ususario = input('por favor ingrese nombre: ')
        validar_nombre_usuario = validar_nombre(nombre_ususario)

        while validar_nombre_usuario != True:
            print("por favor vuelva a ingresar su nombre, su nombre debe contar con entre 3 a 20 letras")
            nombre_ususario = input('por favor ingrese nuevamente su nombre: ')
            validar_nombre_usuario = validar_nombre(nombre_ususario)
        
        sertificar_nombre = input ('''el nombre que a ingresiado es: '''+ nombre_ususario+ ''' .
        si este no es su nombre o se a esquibocado al escribirlo pulse "0", 
        si el nombre que ingreso es valido pulse una tecla que no sea "0"''')
    
    sertificar_apellido = "0"
    while sertificar_apellido == "0" :
        apellido_usuario = input('por favor ingrese apellido: ')
        validar_nombre_apellido = validar_nombre(apellido_usuario)

        while validar_nombre_apellido != True:
            print("por favor vuelva a ingresar su apellido, su apellido debe contar con entre 3 a 20 letras")
            apellido_usuario = input('por favor ingrese nuevamene su apellido: ')
            validar_nombre_apellido = validar_nombre(apellido_usuario)

        sertificar_apellido = input ('''el apellido que a ingresiado es: '''+ apellido_usuario+ ''' .
        si este no es su apellido o se a esquibocado al escribirlo pulse "0", 
        si el apellido que ingreso es valido pulse una tecla que no sea "0"''')

    sertificar_cedula = "0"
    while sertificar_cedula == "0" :
        cedula_ususario = input('por favor ingrese cedula: ')
        validar_nombre_cedula = validar_cedula(cedula_ususario)

        while validar_nombre_cedula != True:
            print("por favor vuelva a ingresar su cedula, su cedula debe contar con 8 numeros")
            cedula_ususario = input('por favor ingrese nuevamente su cedula: ')
            validar_nombre_cedula = validar_cedula(cedula_ususario)
        
        sertificar_cedula = input ('''el apellido que a ingresiado es: '''+ cedula_ususario+ ''' 
        .si esta no es su cedula o se a esquibocado al escribirla pulse 0, 
        si la cedula que ingreso es valido pulse una tecla que no sea 0''')

#crea un archivo de texto con el nombre "datos de usuario", en donde almacena los datos dados por los alumnos
    with open('datos_usuario.txt', 'w') as file:
        file.write(f"Nombre: {nombre_ususario}, Apellido: {apellido_usuario}, Cédula: {cedula_ususario}")

def menu_principal ():
    print("!aqui va algo no se que poner!")
    print('''para corte 1, pulse 1
    para corte 2, pulse 2
    para corte 3, pulse 3
    para corte 4, pulse 4    ''')
    corte_selecionado = int(input(""))

    if corte_selecionado == 1:
        primer_corte()
    elif corte_selecionado == 2:
        segundo_corte()
    elif corte_selecionado == 3:
        terecer_corte()
    elif corte_selecionado == 4:
        cuarto_corte()

    else:
        print("por favor selecione una opcion valida")

inicio_seccion ()

def primer_corte ():
    print("selecciono primer corte")

def segundo_corte ():
    print("selecciono segundo corte")

def terecer_corte ():
    print("selecciono tercero corte")

def cuarto_corte ():
    print("selecciono cuarto corte")