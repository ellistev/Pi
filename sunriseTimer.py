from getsunrise import getSunrisePst
from requests import get
import json
from threading import Timer
from datetime import datetime, timedelta
from sendSms import sendMessage
from transmit import transmit_code

a_on = '1110101011100010111111000'  #works for 4 on
a_off= '1110101011100010111100110' #works for 4 off

def TurnOffLights():
    sendMessage("hello Master, I'm turning off christmas lights")
    transmit_code(a_off)
    return
    
def TurnOnLights():
    sendMessage("hello Master, I'm turning on christmas lights")
    transmit_code(a_on)
    off = Timer(7200, TurnOffLights)
    off.start()
    return

sunsetapi = 'http://api.sunrise-sunset.org/json?date=today&'
my_lat = 49.2326938
my_lon = -123.0110784

sunsetapiCall = sunsetapi + 'lat=' + str(my_lat) + '&lng=' + str(my_lon)

#get sunrise sunset data
results = get(sunsetapiCall).json()['results']
sunriseTime = getSunrisePst(results)
print('sunrise')
print(sunriseTime)

delta_t = sunriseTime - datetime.today()
print(delta_t.seconds)

sendMessage(str(sunriseTime))
on = Timer(delta_t.seconds-7200, TurnOnLights)
on.start()
