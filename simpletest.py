#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
# Re edited October 2019 by : KFLMiami420
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

humidity, temperature = Adafruit_DHT.read_retry(22, 10)

temperature = temperature * 9/5.0 + 32
humidity = humidity + 7

if humidity is not None and temperature is not None:
    print('DHT22 Sensor Temperature={0:0.1f}F  Humidity={1:0.1f}%'.format(tempe$

   # print('Temp    ={ :0.1f}F'.format(temperature)) 
   # print('Humidity={1:0.1f}%'.format(humidity))
else:
    print('Failed to get reading. Try again!')
    sys.sleep(1)
