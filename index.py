# las funciones presentadas a continuacion no esta siendo usada dentro del codigo, se deben implementar.
################!!!!!!!!!!!!!
# deben almacenar la funcion dentro de la variable para poder octener el valor retornado

#validar_alfanumerico fue creado en caso de que se nesecite en un futuro
def validar_alfanumerico(dato_input):

    #extrae la longitud del dato
    caracteres = len(dato_input)

    #esta es la parte encargada de detectar numeros y letras 
    tipo = dato_input.isalnum()
    if tipo == True:
        if caracteres > 2 and caracteres < 12:
            dato_valido_input = True
            return dato_valido_input

#validar_nombre fue creado para validar el nombre 
def validar_nombre(dato_input):

    #extrae la longitud del dato
    caracteres = len(dato_input)

    #esta es la parte encargada de detectar letras 
    tipo = dato_input.isalpha()
    if tipo == True:
        if caracteres > 3 and caracteres < 20:
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
    print('''bienbenido a proyecto classroom
          para iniciar primero inserte sus datos''')
    
    nombre_ususario = input('nombre: ')
    validar_nombre_usuario = validar_nombre(nombre_ususario)

    while validar_nombre_usuario != True:
        print("por favor vuelva a ingresar su nombre, su nombre debe contar con entre 3 a 20 letras")
        nombre_ususario = input('nombre: ')
        validar_nombre_usuario = nombre_ususario
    
    apellido_usuario = input('apellido: ')
    validar_nombre_apellido = apellido_usuario

    while validar_nombre_apellido != True:
        print("por favor vuelva a ingresar su apellido, su apellido debe contar con entre 3 a 20 letras")
        apellido_usuario = input('apellido: ')
        validar_nombre_apellido = validar_nombre(apellido_usuario)

    cedula_ususario = input('cedula: ')
    validar_nombre_cedula = cedula_ususario

    while validar_nombre_cedula != True:
        print("por favor vuelva a ingresar su cedula, su cedula debe contar con 8 numeros")
        cedula_ususario = input('cedula: ')
        validar_nombre_cedula = validar_cedula(cedula_ususario)

    
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

menu_principal()

def primer_corte ():
    print("selecciono primer corte")

def segundo_corte ():
    print("selecciono segundo corte")

def terecer_corte ():
    print("selecciono tercero corte")

def cuarto_corte ():
    print("selecciono cuarto corte")