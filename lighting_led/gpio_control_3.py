'''
Ejemplo de usar un boton para encender y apagar un LED evitando bloquear el programa.
Fuente: https://www.raspberrypi.org/learning/physical-computing-with-python/worksheet/
Fecha: mar dic  6 21:29:43 COT 2016
Version: 1.0
'''

from gpiozero import LED, Button
from signal import pause

# Usando el GP17 controlamos el LED
led = LED(17)

# Usando el GP2 controlamos el Boton
button = Button(2)

# Evento de presionar el boton enciende el LED
button.when_pressed = led.on
# Evento de soltar el boton apaga el LED
button.when_released = led.off

# El programa imprime un mensaje
print('No bloquea la ejecucion del programa')

# Pausa el programa evita terminar el programa
pause()


'''
Ejecutar: python gpio_control_3.py
'''
