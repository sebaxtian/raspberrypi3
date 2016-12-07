'''
Ejemplo de encender un LED durante 3 segundos despues de presionar un boton.
Fuente: https://www.raspberrypi.org/learning/physical-computing-with-python/worksheet/
Fecha: mar dic  6 21:06:10 COT 2016
Version: 1.0
'''

from gpiozero import LED, Button
from time import sleep

# Usando el GP17 controlamos el LED
led = LED(17)
# Usando el GP2 controlamos el Boton
button = Button(2)

# El programa espera hasta que el boton sea presionado
button.wait_for_press()

# Se enciende el LED
led.on()

# Espera 3 segundos
sleep(3)

# Se apaga el LED
led.off()


'''
Ejecutar: python gpio_control_1.py
'''
