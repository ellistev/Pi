import requests
import json
import calendar
from datetime import datetime, timedelta

_token = "token"
_domain = "atca"

date = str(calendar.timegm((datetime.now() + timedelta(-30))
    .utctimetuple()))

print date