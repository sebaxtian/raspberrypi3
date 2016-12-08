'''
Este es un ejemplo de usar el API de Twitter con la
libreria Twython desde una aplicacion de Twitter.
Fuente: https://www.raspberrypi.org/learning/getting-started-with-the-twitter-api/worksheet/
Fecha: mié dic  7 22:07:39 COT 2016
Version: 1.0
'''

import os
import sys

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

# Define un mensaje para enviar un Tweet
message = "Hello world!"

# Usando el API update_status se envia un Tweet con el mensaje
twitter.update_status(status=message)

# Imprime en la salida estandar del sistema el mensaje
print("Tweeted: %s" % message)


'''
Ejecutar: python3 twitter.py
          python twitter.py
'''
