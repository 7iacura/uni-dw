class Meteo:
    def __init__(self,row):
        import datetime
        import pytz
        date = datetime.datetime.fromtimestamp(int(row['time']), tz=pytz.timezone('US/Eastern'))
        self.data = date.date()
        self.ora = date.time()
        self.apparentTemperature = row['apparentTemperature']
        try:
            self.cloudCover = row['cloudCover']
        except Exception:
            self.cloudCover = None
        self.dewPoint = row['dewPoint']
        self.humidity = row['humidity']
        self.precipIntensity = row['precipIntensity']
        self.precipProbability = row['precipProbability']
        self.pressure = row['pressure']
        self.summary = row['summary']
        self.temperature = row['temperature']
        self.visibility = row['visibility']
        self.windBearing = row['windBearing']
        self.windSpeed = row['windSpeed']


    def store(self,cursor):
        import datetime
        date = datetime.datetime.now()
        add_meteo = ("INSERT INTO weather "
                     "(data,ora,apparentTemperature,cloudCover,dewPoint,humidity,precipIntensity,precipProbability,pressure,summary,temperature,visibility,windBearing,windSpeed,created_at) "
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data_meteo = (self.data,
                      self.ora,
                      self.apparentTemperature,
                      self.cloudCover,
                      self.dewPoint,
                      self.humidity,
                      self.precipIntensity,
                      self.precipProbability,
                      self.pressure,
                      self.summary,
                      self.temperature,
                      self.visibility,
                      self.windBearing,
                      self.windSpeed,
                      date)

        cursor.execute(add_meteo, data_meteo)

        return cursor.lastrowid


