import os
import signal
import time
import threading
import tkinter as tk
from tkinter import messagebox

corriendo = True
mensaje_abierto = True

def modal_salir():
    #crea la base del modal
    window = tk.Tk()
    window.withdraw()

    # Crear un cuadro de diálogo modal
    result = messagebox.askokcancel("Finalisar evalucion", "salir de la evaluacion perjudicara tu nota ¿estas seguro que deseas salir?")
    if result:
        global corriendo
        corriendo = False
        cerrar_mensaje_bienvenida()
        salir_programa()

    window.mainloop()

def mostrar_bienvenida():
    global mensaje_bienvenida
    mensaje_bienvenida = tk.Tk()
    mensaje_bienvenida.protocol("WM_DELETE_WINDOW", lambda: None)
    boton_bienvenida = tk.Button(mensaje_bienvenida, text="Proyecto classroom",)
    boton_bienvenida.pack()
    mensaje_bienvenida.mainloop()

def cerrar_mensaje_bienvenida():
    global mensaje_abierto
    mensaje_abierto = False
    mensaje_bienvenida.destroy()

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
    borrar_pantalla()
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
            print("Faltan 10 minutos para terminar la evaluacion")
        elif segundos == 300:
            print("Faltan 5 minutos para terminar la evaluacion")
        elif segundos == 60:
            print("Solo falta 1 minuto para terminar la evaluacion")
    root.destroy()

def iniciar_temporizador():
    global corriendo
    corriendo = True
    root = tk.Tk()
    root.title("Temporizador")

    # Deshabilitar el botón de cierre para que el alumno no cierre el cronometro por accidente
    root.protocol("WM_DELETE_WINDOW", lambda: None)

    label = tk.Label(root, text="", width=10)
    label.pack()

    segundos = 3600
    threading.Thread(target=temporizador, args=(segundos, label, root)).start()

    root.mainloop()
