
#!/usr/bin/python
from __future__ import division
import Adafruit_DHT
import time

def avg_min_max(data):
    """Given a list, return a tuple of the mean, min, and max."""
    return sum(data) / len(data), min(data), max(data)

# Configuration
sensor = Adafruit_DHT.DHT22
gpio = 10
count = 5

date = time.gmtime()
humid_temp_data = [Adafruit_DHT.read_retry(sensor, gpio) for _ in range(count)]
humid_stats = avg_min_max([humid for humid, _ in humid_temp_data])
temp_stats = avg_min_max([temp for _, temp in humid_temp_data])

with open("MainLog.txt", "a") as file:
    file.write(time.strftime("%Y-%m-%d %H:%M:%S: ", date))
    file.write("{0},{1},{2} | {3},{4},{5}\n".format(*(humid_stats + temp_stats)))

