
class Luogo:
    def __init__(self,borough,zip,latitude,longitude):
        self.borough = borough
        self.zip = zip
        self.latitude = latitude
        self.longitude = longitude
        if zip.strip() == "":
            self.zip = 0
        if latitude == "":
            self.latitude = 0
        if longitude == "":
            self.longitude = 0




    def store(self,cursor):
        import datetime
        from pprint import pprint


        tomorrow = datetime.date
        time = datetime.time

        import datetime
        date = datetime.datetime.now()
        exist_luogo = "SELECT * FROM luogo where latitudine = " +str(self.latitude) + " and longitudine = " +str(self.longitude)
        cursor.execute(exist_luogo)
        exist = False
        for luogo in cursor:
            id = luogo[0]
            quartiere = luogo[1]
            zip = luogo[2]
            exist = True

        if not exist:
            add_scatenante = "INSERT INTO luogo (quartiere,zip,latitudine,longitudine,created_at)VALUES (%s,%s,%s,%s,%s)"
            data_scatenante = (self.borough,self.zip,self.latitude,self.longitude,date)
            cursor.execute(add_scatenante,data_scatenante)
            id = cursor.lastrowid

        else:
            if self.borough != "" and self.borough != quartiere:
                update = "UPDATE luogo set quartiere = '"+self.borough+"' where id = "+str(id)
                cursor.execute(update)
            if self.zip != 0 and int(self.zip) != int(zip):
                update = "UPDATE luogo set zip = " + str(self.zip) + " where id = "+str(id)
                cursor.execute(update)

        return id










