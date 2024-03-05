import signal

def handler(signal, frame):
    try:
        respuesta = input("¿Está seguro que quiere salir del programa? (y/n): ")
        if respuesta.lower() == 'y':
            print("Saliendo del programa...")
            exit(0)
        else:
            print("Continuando la ejecución.")
    except EOFError:
        print("\nContinuando la ejecución.")

signal.signal(signal.SIGINT, handler)

while True:
    pass  