def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."

def menu():
    print("Calculadora:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print("Resultado:", suma(num1, num2))
        elif opcion == "2":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print("Resultado:", resta(num1, num2))
        elif opcion == "3":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print("Resultado:", multiplicacion(num1, num2))
        elif opcion == "4":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número (distinto de cero): "))
            print("Resultado:", division(num1, num2))
        elif opcion == "5":
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    main()
#termine_el_examen