#libreria time se emplea para poder medir tiempo y crear cronometros
import time

import tkinter as tk

def temporizador(segundos):
    while segundos: 
        mins = segundos // 60
        secs = segundos % 60
        tiempo_restante = f'{mins: 02d}:{secs:02d}'
        label.config(text=tiempo_restante)
        time.sleep(1)
        segundos -= 1
        if segundos == 80:
            print("se te esta acabando el tiempo")
        elif segundos == 60:
            print("se te esta acabando el tiempo")
        root.update()

root = tk.Tk()
label = tk.Label(root, text="")
label.pack()
temporizador(120)  # Ejemplo con 120 segundos
root.mainloop()
