#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import sys

import Adafruit_DHT
import urllib
import urllib2
import json
import time

# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
        '22': Adafruit_DHT.DHT22,
        '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
  sensor = sensor_args[sys.argv[1]]
  pin = sys.argv[2]
else:
  print 'usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#'
  print 'example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4'
  sys.exit(1)

eventArray = []
count = 0

var = 1
while var == 1:

  # Try to grab a sensor reading. Read sensor values 9 times to get more precision
  # Store readings in a list
  humidityArray = []
  temperatureArray = []

  for x in range (0, 8):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    humidityArray.append(humidity)
    temperatureArray.append(temperature)	
  
  # Sort the list and take the median of the readings
  humidityArray.sort()
  temperatureArray.sort()
  humidity = humidityArray[4]
  temperature = temperatureArray[4]

  if humidity is not None and temperature is not None:
    #print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)

    # These variables below will be edited according to your IVEN account
    ######################################################################
    req = urllib2.Request('http://api.iven.io/api/v1/events/12345678')
    req.add_header('API-KEY', 'b708d05bc4452adc24d6e7f5341123d16b94b54e')
    req.add_header('Content-Type', 'application/json')
    sleepTime = 60
    ######################################################################

    # Get the current UNIX timestamp
    ts = int(time.time())

    # Create an event object with current variables
    eventObject = {
      "message": {
          	"header": "Temperature / Humidity",
          	"body": "Temperature / Humidity received"
          },
          
          "timestamp": ts,
          
          "dataArray": [
              {"key": "temperature", "value": temperature},
              {"key": "humidity", "value": humidity}]
      	}
    
    # Put event object in an event array. Then create an object
    # which is veryclose to be a JSON.
    eventArray.append(eventObject)
    data = {
      "events": eventArray
    }

    # Try to send the POST request to IVEN
    # If an exception occurs (connection break, server down) 
    # current data will be saved to a file.
    # When the connection establishes again the collected
    # data will be sent in an array.
    try:
      link = urllib2.urlopen(req, json.dumps(data))
      if link.getcode() is 200:
        del eventArray[:]

      if count is not 0:
        eventFile = open('events', 'r')
        eventArray = []
        for line in eventFile:
          eventArray.append(json.loads(line))
        data = {
        "events": eventArray
        }
        eventFile.close()
        link = urllib2.urlopen(req, json.dumps(data))
        count = 0
        f = open('events', 'w')
        f.close()
    except Exception:
      f = open('events', 'a')
      f.write(json.dumps(eventObject))
      f.write('\n')
      f.close()
      count = count+1
      print 'Exception'

  else:
    print 'Failed to get reading. Try again!'

  time.sleep(sleepTime)
