import requests
from pprint import pprint
import datetime
from datetime import timedelta
import mysql.connector
from Meteo import Meteo
import json

#709703159f539e81ecf8019a7d184627
#72a133efd53a82f8b026b3730c921135

passwordSQL = 'passMysql'

date = datetime.datetime.strptime("09/20/17", "%m/%d/%y")
day = date.day
month = date.month
year = date.year
cnx = mysql.connector.connect(user='root', password=passwordSQL,
                                  host='localhost',
                                  database='meteo')
cursor = cnx.cursor()
while year <= 2017:
    yearStr = str(year)
    monthStr = str(month) if month >= 10 else '0'+str(month)
    dayStr = str(day) if day >= 10 else '0'+str(day)
    url = 'https://api.darksky.net/forecast/72a133efd53a82f8b026b3730c921135/40,-74,' + yearStr + '-' + monthStr + '-' + dayStr + 'T00:00:00'
    response = requests.get(url)
    data = json.loads(str(response.content)[2:-1].replace("\\", ""))
    print(url)
    print(str(response.content)[2:-1])
    for weather in data['hourly']['data']:
        try:
            w = Meteo(weather)
            w.store(cursor)
            cnx.commit()
        except Exception as e:
            print(e)

    date = date + timedelta(days=1)
    day = date.day
    month = date.month

    year = date.year
cursor.close()
cnx.close()



