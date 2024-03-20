import tkinter as tk
from tkinter import messagebox

def create_modal():
    window = tk.Tk()
    window.withdraw()  # Ocultar la ventana principal

    # Crear un cuadro de diálogo modal
    result = messagebox.askokcancel("Finalisar evalucion", "salir de la evaluacion perjudicara tu nota ¿estas seguro que desea continuar?")
    if result:
        print("Has seleccionado 'Aceptar'")
    else:
        print("Has seleccionado 'Cancelar'")

    window.mainloop()

create_modal()