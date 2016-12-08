'''
Ejemplo de usar TwythonStreamer para escuchar el flujo de Tweets
filtrando los que tengan un termino o paralabra en particular.
Fuente: https://www.raspberrypi.org/learning/getting-started-with-the-twitter-api/worksheet/
Fecha: mié dic  7 23:27:49 COT 2016
Version: 1.0
'''

import os
import sys

# Path donde se encuentra archivo auth.py con las API KEYS
authpath = '/home/pi/Documents/Twitter'
sys.path.append(os.path.abspath(authpath))

# Importa clase TwythonStreamer de libreria Twython para usar API de Streamer de Twitter
from twython import TwythonStreamer

# Importa las variables con las llaves de autorizacion de aplicacion Twitter
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# Crea la clase MyStreamer que hereda de TwythonStreamer
class MyStreamer(TwythonStreamer):
    # Sobre escribe metodo on_success el cual se ejecuta cuando encuentra Tweets que contengan el termino o palabra
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text']
            # Imprime en la salida estandar del sistema el usuario y el tweet
            print("@%s: %s" % (username, tweet))

# Crea un objeto de clase MyStreamer
stream = MyStreamer (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# Inicia el seguimento del stream para el termino {raspberry pi}
stream.statuses.filter(track='raspberry pi')


'''
Ejecutar: python3 twitter.py
          python twitter.py
'''
