import os
import datetime
import sys
import time
from urllib import urlencode
import Adafruit_DHT
import urllib2

from config import Config

sensor = Adafruit_DHT.DHT22

gpio_pin = 05

MEASUREMENT_INTERVAL = .5

WEATHER_UPLOAD = True

WU_URL = "http://weatherstation.wunderground.com/weatherstation/updateweatherstation.php"

SINGLE_HASH = "#"
HASHES = "################################################################"
SLASH_N = "\n"

def c_to_f(input_temp):
    return (input_temp * 1.8) + 32

def main():

    last_minute = datetime.datetime.now().minute

    if last_minute == 0:
        last_minute = 59
    else:
        last_minute -= 1

    while 1:

        current_minute = datetime.datetime.now().minute

        if current_minute != last_minute:

            last_minute = current_minute

            if (current_minute == 0) or ((current_minute % MEASUREMENT_INTERVAL) == 0):

                now = datetime.datetime.now()
                print("\n%d minute mark (%d @ %s)" % (MEASUREMENT_INTERVAL, current_minute, str(now)))

                humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio_pin)

                if humidity is not None and temperature is not None:
                    temp_c = round(temperature, 1)
                    temp_f = round(c_to_f(temperature), 1)
                    humidity = round(humidity, 2)
                    print("Temp: %sF (%sC), Humidity: %s%%" % (temp_f, temp_c, humidity))

                    if WEATHER_UPLOAD:

                        print("Uploading data to Weather Underground")

                        weather_data = {
                            "action": "updateraw",
                            "ID": wu_station_id,
                            "PASSWORD": wu_station_key,
                            "dateutc": "now",
                            "tempf": str(temp_f),
                            "humidity": str(humidity)
                        }
                        try:
                            upload_url = WU_URL + "?" + urlencode(weather_data)
                            response = urllib2.urlopen(upload_url)
                            html = response.read()
                            print("Server response:", html)

                            response.close()
                        except:
                            print("Exception:", sys.exc_info()[0], SLASH_N)
                    else:
                        print("Skipping Weather Underground upload")

                else:
                    print('Unable to obtain sensor reading')

        time.sleep(1)

    print("Leaving main()")

print(SLASH_N + HASHES)
print(SINGLE_HASH, "Pi Weather Station (Simple Sensor DHT22 )  ", SINGLE_HASH)
print(SINGLE_HASH, "--------", SINGLE_HASH)
print(HASHES)

if (MEASUREMENT_INTERVAL is None) or (MEASUREMENT_INTERVAL > 60):
    print("The application's 'MEASUREMENT_INTERVAL' cannot be empty or greater than 60")
    sys.exit(1)

#  Read Weather Underground Configuration Parameters

print("\nInitializing Weather Underground configuration")
wu_station_id = Config.STATION_ID
wu_station_key = Config.STATION_KEY
if (wu_station_id is None) or (wu_station_key is None):
    print("Missing values from the Weather Underground configuration file\n")
    sys.exit(1)


print("Successfully read Weather Underground configuration values")
print("Station ID:", wu_station_id)
print("Initialization complete!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:



