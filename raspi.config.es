#
# Configuracion de Raspberry Pi 3 al Español
# 
# Fuente: https://wiki.bandaancha.st/C%C3%B3mo_espa%C3%B1olizar_tu_Raspberry_Pi
# Date: vie dic  2 15:32:35 COT 2016
# Version: 1.0
#


# Idioma
sudo dpkg-reconfigure locales

# Teclado
sudo dpkg-reconfigure keyboard-configuration

# Fecha y Hora
sudo dpkg-reconfigure tzdata

# Ajustar Fecha y Hora [MES][DIA][HORA][MINUTOS]
sudo date 12041548

# Si se tiene instalado xrdp para acceso remoto
# y el teclado no esta configurado al Español
# cuando se crea una sesion desde un cliente
# XRDP entonces hacer lo siguiente:

# 1. Crear una copia del archivo /etc/xrdp/km-0409.ini
sudo cp -rfv /etc/xrdp/km-0409.ini /etc/xrdp/km-0409.ini.bck

# 2. Borrar el archivo /etc/xrdp/km-0409.ini
sudo rm -rfv /etc/xrdp/km-0409.ini

# 3. Copiar el archivo de este repositorio [km-0409.ini] en /etc/xrdp/
sudo cp -rfv km-0409.ini /etc/xrdp/

