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
        if caracteres < 2:
            print("el nombre de usuario debe de tener por lo menos 2 caracteres")
        elif caracteres > 12:
            print("debe contener menos de 12 caracteres")
        else:
            print("bienvenido",dato_input)
            dato_valido_input = True
            return dato_valido_input
    else:
        print("no se admiten caracteres especiales en este campo")

#validar_nombre fue creado para validar el nombre 
def validar_nombre(dato_input):

    #extrae la longitud del dato
    caracteres = len(dato_input)

    #esta es la parte encargada de detectar letras 
    tipo = dato_input.isalpha()
    if tipo == True:
        if caracteres < 3:
            print("el nombre de usuario debe de tener por lo menos 3 caracteres")
        elif caracteres > 20:
            print("debe contener menos de 20 caracteres")
        else:
            print("bienvenido",dato_input)
            dato_valido_input = True
            return dato_valido_input
    else:
        print("solo se admite texto en este campo")

#validar_cedula fue creado para validar la cedula
def validar_cedula(dato_input):
        
    #extrae la longitud del dato
    caracteres = len(dato_input)

    #esta es la parte encargada de detectar numeros
    tipo = dato_input.isdigit()
    if tipo == True:
        if caracteres != 7:
            print("la cedula debe contar con 7 caracteres")
        else:
            print("bienvenido",dato_input)
            dato_valido_input = True
            return dato_valido_input
    else:
        print("solo se admiten numeros en este campo")
#############!!!!!!!!!!!!!!!!!!!