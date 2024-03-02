#libreria time se emplea para poder medir tiempo y crear cronometros
import time

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

temporizador(100)