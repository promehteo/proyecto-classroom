import time

import tkinter as tk

import threading

def temporizador(segundos, label, root):
    while segundos: 
        mins = segundos // 60
        secs = segundos % 60
        tiempo_restante = f'{mins:02d}:{secs:02d}'
        label.config(text=tiempo_restante)
        time.sleep(1)
        segundos -= 1
        if segundos == 80:
            print("se te esta acabando el tiempo")
        elif segundos == 60:
            print("se te esta acabando el tiempo")
    root.destroy() 

def iniciar_temporizador():
    root = tk.Tk()
    root.title("Temporizador")

    # Deshabilitar el botón de cierre
    root.protocol("WM_DELETE_WINDOW", lambda: None)

    label = tk.Label(root, text="", width=10)
    label.pack()

    segundos = 10
    threading.Thread(target=temporizador, args=(segundos, label, root)).start()

    root.mainloop()

threading.Thread(target=iniciar_temporizador).start()