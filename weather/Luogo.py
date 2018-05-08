
class Luogo:
    def __init__(self,borough,zip,latitude,longitude):
        self.borough = borough
        self.zip = zip
        self.latitude = latitude
        self.longitude = longitude
        if zip == "":
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
        if self.latitude == 0 and self.longitude == 0:
            return 0

        exist_luogo = "SELECT * FROM luogo where latitudine = " +str(self.latitude) + " and longitudine = " +str(self.longitude)
        cursor.execute(exist_luogo)
        exist = False
        for luogo in cursor:
            id = luogo[0]
            quartiere = luogo[1]
            zip = luogo[2]
            exist = True

        if not exist:
            add_scatenante = "INSERT INTO luogo (quartiere,zip,latitudine,longitudine)VALUES ('"+str(self.borough)+"',"+str(self.zip)+","+str(self.latitude)+","+str(self.longitude)+")"
            id = cursor.lastrowid
            cursor.execute(add_scatenante)
        else:
            if self.borough != "" and self.borough != quartiere:
                update = "UPDATE luogo set quartiere = '"+self.borough+"' where id = "+str(id)
                cursor.execute(update)
            if self.zip != 0 and int(self.zip) != int(zip):
                update = "UPDATE luogo set zip = " + str(self.zip) + " where id = "+str(id)
                cursor.execute(update)

        return id










