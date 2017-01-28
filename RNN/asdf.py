import requests
import json
import calendar
from datetime import datetime, timedelta

_token = "xoxp-4083208737-20033966023-132915462035-078b6cfaf873bbbda75324a72c8fa706"
_domain = "atca"

date = str(calendar.timegm((datetime.now() + timedelta(-30))
    .utctimetuple()))

print date