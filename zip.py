#Librería para comprimir los datos con contraseña (similiar a la encriptacion)
import pyzipper
#Librería que se usará para controlar el tiempo
import time
#Librería para enviar los correos de forma automática
import smtplib
#Librería para quitar los acentos
from unidecode import unidecode
#Libreria empleada para interactuar con el sistema opertivo a nivel de consola
import os
#Libreria que nos ayuda a crear el modal del temporizador
import tkinter as tk
#Libreria que nos permitio integrar el relog al codigo, permite que el relog se ejecute "aparte" del menu
import threading
#Libreria usada para crear el modal de cerrar seccion
from tkinter import messagebox
#Libreria empleada para detectar que teclas se precionan
import signal

#Librerias del correo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#


def encriptacion(nombre_ususario, apellido_usuario, cedula_ususario, respuestas_examen, preguntas=None):
    # Se crea el nombre del archivo .txt
    nombre_archivo_txt = f"{nombre_ususario}_{apellido_usuario}_{cedula_ususario}.txt"
    # Se crea el nombre del archivo .zip
    nombre_archivo_zip = f"{nombre_ususario}_{apellido_usuario}_{cedula_ususario}.zip"

    # Guarda las respuestas en el archivo de texto
    with open(nombre_archivo_txt, 'w') as archivo_txt:
        for i, respuesta in enumerate(respuestas_examen, start=1):
            archivo_txt.write(f"Pregunta {i}: {respuesta}\n")

        # Verificar si hay una respuesta para la pregunta práctica
        if preguntas is not None:
            if len(respuestas_examen) > len(preguntas) - 1:
                archivo_txt.write("\nRespuesta a la pregunta práctica:\n")
                archivo_txt.write(respuestas_examen[-1])  # Agregar la respuesta práctica al archivo de texto

    # Guarda el archivo de texto en un archivo ZIP con contraseña
    with pyzipper.AESZipFile(nombre_archivo_zip, 'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zf:
        # Contraseña del archivo ZIP (se puede cambiar)
        contraseña_profesor = b"profemirtha123"
        zf.setpassword(contraseña_profesor)
        
        # Escribe solo las preguntas respondidas en el archivo ZIP
        for i, respuesta in enumerate(respuestas_examen, start=1):
            pregunta = preguntas[i-1]
            zf.writestr(f"Pregunta_{i}.txt", f"Pregunta: {pregunta['enunciado']}\nRespuesta: {respuesta}")

    # Elimina el archivo de texto para que sea inaccesible para el alumno
    os.remove(nombre_archivo_txt)

respuestas_examen =[]

encriptacion("nombre_ususario", "apellido_usuario", "cedula_ususario", respuestas_examen)