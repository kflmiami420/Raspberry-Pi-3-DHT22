#!/usr/bin/python
#dht22 on pin 10 because all my pcb proto boards are on pin 10 now  

import sys
import Adafruit_DHT

while True:

    humidity, temperature = Adafruit_DHT.read_retry(22, 10)
    temperature = temperature * 9/5.0 + 32
    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
