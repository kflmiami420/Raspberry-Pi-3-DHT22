#no 2.7.4                   File: example.py

#!/usr/bin/python
import sys
import Adafruit_DHT

while True:

    humidity, temperature = Adafruit_DHT.read_retry(22, 4)
    temperature = temperature * 9/5.0 + 32
    print 'Temperature: {0:0.1f} F Humidity: {1:0.1f} %'.format(temperature, hu$



