'''
Ejemplo de imprimir un mensaje cuando un boton es presionado.
Fuente: https://www.raspberrypi.org/learning/physical-computing-with-python/worksheet/
Fecha: mar dic  6 20:11:21 COT 2016
Version: 1.0
'''

from gpiozero import Button

# Usando el GP2 controlamos el boton
button = Button(2)

# El programa espera hasta que el boton sea presionado
button.wait_for_press()

# El programa imprime un mensaje
print('Se Presiona El Boton')


'''
Ejecutar: python gpio_button.py
'''
