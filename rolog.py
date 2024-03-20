import time
import threading

def temporizador(segundos):
    while segundos: 
        mins = segundos // 60
        secs = segundos % 60
        tiempo_restante = f'{mins: 02d}:{secs:02d}'
        print(tiempo_restante, end='\r')
        time.sleep(1)
        segundos -= 1
        if segundos == 80:
            print("se te esta acabando el tiempo")

        elif segundos == 60:
            print("se te esta acabando el tiempo")

# Crear un hilo para ejecutar el temporizador
t = threading.Thread(target=temporizador, args=(100,))

# Iniciar el hilo
t.start()

#termine_el_examen