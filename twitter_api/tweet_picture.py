'''
Ejemplo de enviar un Tweet con una Foto.
Fuente: https://www.raspberrypi.org/learning/getting-started-with-the-twitter-api/worksheet/
Fecha: mié dic  7 23:01:46 COT 2016
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
message = "Probando Tweet desde #Raspberry Pi 3 usando #Twython https://goo.gl/AKXj48"

# Abre el archivo de foto para enviar con el Tweet {This method is deprecated}
#with open('tweet_picture.png', 'rb') as photo:
#    twitter.update_status_with_media(status=message, media=photo)

# Abre el archivo de foto para enviar con el Tweet
photo = open('tweet_picture_1.png', 'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=message, media_ids=[response['media_id']])

# Imprime en la salida estandar del sistema el mensaje
print("Tweeted: %s" % message)


'''
Ejecutar: python3 twitter.py
          python twitter.py
'''
