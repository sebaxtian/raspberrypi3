# Sensor de Temperatura y Humedad DHT11

Para usar el Sensor DHT11 seguir las instrucciones de instalación de:<br><br>
*Adafruit Python DHT Sensor Library*
https://github.com/adafruit/Adafruit_Python_DHT
<br><br>

>La libreria AdafruitDHT ha sido probada en Python2.6/2.7


<br>

1. Instalar dependencias de Python para compilar extensiones:
````
sudo apt-get update
sudo apt-get install build-essential python-dev
````

<br>

2. Descargar el archivo .ZIP de la libreria AdafruitDHT<br>
https://github.com/adafruit/Adafruit_Python_DHT/archive/master.zip

<br>

3. Descomprimir el archivo .ZIP descargado y se instala la libreria en Python
````
sudo python setup.py install
````

<br>

4. Probar la libreria:
Dentro de la carpeta generada al descomprimir archivo .ZIP se encuentra una carpeta "examples"

Ejecutar el programa AdafruitDHT.py de la siguiente forma:
````
python AdafruitDHT.py 11 4
````

La respuesta del programa debe ser algo similar a esto:
````
Temp=25.0*  Humidity=46.0%
````

