import requests
from pprint import pprint
import datetime
from datetime import timedelta

import json
date = datetime.datetime.strptime("01/01/15", "%m/%d/%y")
day = date.day
month = date.month
year = date.year
while year <= 2017:
    yearStr = str(year)
    monthStr = str(month) if month > 10 else '0'+str(month)
    dayStr = str(day) if day > 10 else '0'+str(day)
    url = 'https://api.darksky.net/forecast/72a133efd53a82f8b026b3730c921135/40,-74,' + yearStr + '-' + monthStr + '-' + dayStr + 'T00:00:00'
    response = requests.get(url)
    data = json.loads(str(response.content)[2:-1])
    for weather in data['hourly']['data']:
        pprint(weather)
        exit(3)
    date = date + timedelta(days=1)
    day = date.day
    month = date.month
    year = date.year
exit(0)



