'''
Ejemplo de usar un boton para encender y apagar un LED.
Fuente: https://www.raspberrypi.org/learning/physical-computing-with-python/worksheet/
Fecha: mar dic  6 21:19:23 COT 2016
Version: 1.0
'''

from gpiozero import LED, Button
from time import sleep

# Usando el GP17 controlamos el LED
led = LED(17)

# Usando el GP2 controlamos el Boton
button = Button(2)

# En un ciclo infinito
while True:
    # El programa espera hasta que el boton sea presionado
    button.wait_for_press()
    # Cambia el estado del LED de apagado a encendido o viceversa
    led.toggle()


'''
Una desventaja de usar la funcion wait_for_press() es que bloquea
la continuidad de ejecucion del programa.
Ejecutar: python gpio_control_2.py
'''