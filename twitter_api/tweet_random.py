'''
Ejemplo de enviar un Tweet aleatorio apartir de una
lista de mensaje, uso de citas de Carl Sagan.
Fuente: https://www.raspberrypi.org/learning/getting-started-with-the-twitter-api/worksheet/
Fecha: mié dic  7 22:23:30 COT 2016
Version: 1.0
'''

import os
import sys
import random

# Path donde se encuentra archivo auth.py con las API KEYS
authpath = '/home/pi/Documents/Twitter'
sys.path.append(os.path.abspath(authpath))

# Importa libreria Twython para usar API de Twitter
from twython import Twython

# Importa las variables con las llaves de autorizacion de aplicacion Twitter
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# Crea objeto con libreria Twython para usar API Twitter
twitter = Twython (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# Define una lista de mensajes, citas de Carl Sagan
messages = [
    '"El precio que pagamos por la previsión del futuro es la desazón que ello engendra" #CarlSagan',
    '"La curiosidad y el afán de resolver dilemas constituyen el sello distintivo de nuestra especie" #CarlSagan',
    '"Afirmaciones extraordinarias requieren siempre de evidencia extraordinaria" #CarlSagan',
    '"Una mota solitaria en la inmensa oscuridad cósmica" #CarlSagan',
    '"Si fuéramos los únicos en este Universo, sería un gran desperdicio de espacio" #CarlSagan',
    '"La primera gran virtud del hombre fue la duda, y el primer gran defecto la fe" #CarlSagan',
    '"Si quieres hacer un pastel de manzana desde el principio, primero debes crear el Universo." #CarlSagan',
    '"Somos polvo de estrellas." #CarlSagan',
    '"La Biblioteca de Alejandría Fue el primer verdadero instituto de investigación del mundo" #CarlSagan'
]

# Selecciona un mensaje aleatorio
message = random.choice(messages)

# Usando el API update_status se envia un Tweet con el mensaje
twitter.update_status(status=message)

# Imprime en la salida estandar del sistema el mensaje
print("Tweeted: %s" % message)


'''
Ejecutar: python3 twitter.py
          python twitter.py
'''
