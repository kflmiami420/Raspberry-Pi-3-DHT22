# Raspberry-Pi-3-DHT22-Temp-Sensor
2018 Raspberry Pi 3 DHT22 Temp Sensor  Scripts 



to get the DHT22 working on a raspberry pi 


sudo apt-get install git-core

       Note: If you get an error installing Git, run sudo apt-get update and try it again.

      To install the Adafruit DHT11 library:

    1. Enter this at the command prompt to download the library:

git clone https://github.com/adafruit/Adafruit_Python_DHT.git

       2. Change directories with:

cd Adafruit_Python_DHT

        3. Now enter this:

sudo apt-get install build-essential python-dev

        4. Then install the library with:

sudo python setup.py install

OUTPUT TO AN SSH TERMINAL
This Python program will output the temperature and humidity readings to an SSH terminal:

sudo apt-get install build-essential python-dev


type on the root  

nano dht22.py and copy and paste the lines below in the file

------------------------------------------------------
#!/usr/bin/python
import sys
import Adafruit_DHT

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)

