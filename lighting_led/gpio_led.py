'''
Ejemplo de encender y apagar un LED con un retardo de 1 segundo.
Fuente: https://www.raspberrypi.org/learning/physical-computing-with-python/worksheet/
Fecha: mar dic  6 19:12:24 COT 2016
Version: 1.0
'''

from gpiozero import LED
from time import sleep

# Usando el GP17 controlamos el LED
led = LED(17)

# En un ciclo infinito
while True:
    # Enciende el LED
    led.on()
    # Espera 1 segundo
    sleep(1)
    # Apaga el LED
    led.off()
    # Espera 1 segundo
    sleep(1)


'''
Ejecutar: python gpio_led.py
'''
