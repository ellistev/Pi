
from datetime import datetime, timedelta
from getsunrise import getSunrisePst
from requests import get
import json
from threading import Timer
from datetime import datetime, timedelta
from sendSms import sendMessage
from transmit import transmit_code




def getSunrisePst(results):
    sunrise = results['sunrise']
    today = datetime.today()
    sunrise_datetime = datetime.strptime(sunrise, '%I:%M:%S %p')
    sunrise_today = datetime(day=today.day+1, month=today.month, year=today.year, hour=sunrise_datetime.hour,minute=sunrise_datetime.minute,second=sunrise_datetime.second)
    sunrise_today = sunrise_today - timedelta(hours=7)
    return sunrise_today



def getSunsetPst(results):
    sunset = results['sunset']
    today = datetime.today()
    sunset_datetime = datetime.strptime(sunset, '%I:%M:%S %p')
    sunset_today = datetime(day=today.day+2, month=today.month, year=today.year, hour=sunset_datetime.hour,minute=sunset_datetime.minute,second=sunset_datetime.second)
    sunset_today = sunset_today - timedelta(hours=7)
    return sunset_today



sunsetapi = 'http://api.sunrise-sunset.org/json?date=today&'
my_lat = 49.2326938
my_lon = -123.0110784

sunsetapiCall = sunsetapi + 'lat=' + str(my_lat) + '&lng=' + str(my_lon)

#get sunrise sunset data
results = get(sunsetapiCall).json()['results']
sunriseTime = getSunrisePst(results)
print('sunrise')
print(sunriseTime)

#get sunrise sunset data
results = get(sunsetapiCall).json()['results']
sunsetTime = getSunsetPst(results)
print('sunset')
print(sunsetTime)

delta_t = sunriseTime - datetime.today()
print(delta_t.seconds)

#sendMessage(str(sunriseTime))
#on = Timer(delta_t.seconds-7200, TurnOnLights)
#on.start()
