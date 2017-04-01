
from datetime import datetime, timedelta





def getSunrisePst(results):
    sunrise = results['sunrise']
    today = datetime.today()
    sunrise_datetime = datetime.strptime(sunrise, '%I:%M:%S %p')
    sunrise_today = datetime(day=today.day+1, month=today.month, year=today.year, hour=sunrise_datetime.hour,minute=sunrise_datetime.minute,second=sunrise_datetime.second)
    sunrise_today = sunrise_today - timedelta(hours=7) #8 in winter
    return sunrise_today



def getSunsetPst(results):
    sunset = results['sunset']
    today = datetime.today()
    sunset_datetime = datetime.strptime(sunset, '%I:%M:%S %p')
    sunset_today = datetime(day=today.day+2, month=today.month, year=today.year, hour=sunset_datetime.hour,minute=sunset_datetime.minute,second=sunset_datetime.second)
    sunset_today = sunset_today - timedelta(hours=7) #8 in winter
    return sunset_today



