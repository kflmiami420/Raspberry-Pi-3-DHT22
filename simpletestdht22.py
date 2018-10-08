
#Simple Test DHT22 read from pin 4
#converting celsius to Farenheiht
#print the actual temp from sensor if it read something


import sys

import Adafruit_DHT

# Parse command line parameters.
sensor = Adafruit_DHT.DHT22
# connected to GPIO pin #4')
pin = 4

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Un-comment the line below to convert the temperature to Fahrenheit.
temperature = temperature * 9/5.0 + 32

# If command instructs to find out if its not zero then print the actual number for Temp/Humid!
if humidity is not None and temperature is not None:
    print('KFLMIAMI426: Time: 00:00   Temp ={0:0.1f}F  Humidity ={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
