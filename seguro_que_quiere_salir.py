import signal

def signal_handler(sig, frame):
    print('Ctrl+C fue presionado, pero no haré nada.')

signal.signal(signal.SIGINT, signal_handler)

def menu():
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Salir")

while True:
    menu()
    try:
        opcion = input("Elige una opción: ")
    except EOFError:
        print('Ctrl+C fue presionado, pero no haré nada.')
        continue
    if opcion == "1":
        print("Has elegido la opción 1.")
    elif opcion == "2":
        print("Has elegido la opción 2.")
    elif opcion == "3":
        print("Has elegido salir. Adiós!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")
