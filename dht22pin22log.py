
#pin 10
#!/usr/bin/python
import time
import sys
import Adafruit_DHT

while True:

    data =  humidity, temperature = Adafruit_DHT.read_retry(22,10)
    temperature = temperature * 9/5.0 + 32
    layout = '{0:5d}:  {1},  {0:0.1f} deg F,  {1:0.1f} humidity %'
    counter = 1

    with open("dht22.log","a+") as f:
        f.write(layout.format(counter, data.timestamp, data.temperature,  data.humidity) + "\n")
    f.close()
    counter += 1
    time.sleep(5)
#    print 'Temp: {0:0.1f} F  Humidity: {1:0.1f} %'.format(temperature, humidity)

