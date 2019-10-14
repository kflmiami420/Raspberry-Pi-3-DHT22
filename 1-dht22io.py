



# Revised October 14 2019 by: KFLMiami420 
# Raspberry Pi Zero W DHT22 HAT


import time
import Adafruit_DHT
from Adafruit_IO import Client, Feed

DHT_DATA_PIN = 10
LOOP_Delay = 35
ADAFRUIT_IO_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # Insert where the xxxx  are your Key
ADAFRUIT_IO_USERNAME = 'xxxxxxxxxxxxxxxxxxxxxxxx'  # Insert where the xxx  are your username
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try: # if we already have the feeds, assign them.
    temperature_feed = aio.feeds('temperature')
    humidity_feed = aio.feeds('humidity')

except RequestError: # if we don't, create and assign them.
    temperature_feed = aio.create_feed(Feed(name='temperature'))
    humidity_feed = aio.create_feed(Feed(name='humidity'))

dht22_sensor = Adafruit_DHT.DHT22

while True:
 
    humidity, temperature = Adafruit_DHT.read_retry(dht22_sensor, DHT_DATA_PIN)
    temperature = temperature * 9/5.0 + 32   # Temp Conversion C to F
    humidity = humidity + 7                  # Humidity Correction for sensor deviation or error


#    print('Temp={0:0.1f}*F Humidity={1:0.1f}%'.format(temperature, humidity))
    print('sending DHT22 data to adafruit io...')
    print('Temperature: %0.1f F' % temperature)
    aio.send(temperature_feed.key, '{0:.2f} F'.format(temperature))
    print("Humidity: %0.1f %%" % humidity)
    aio.send(humidity_feed.key, '{0:.2f} %   '.format(humidity))

    time.sleep(100)
