
class Incidente:
    def __init__(self,row):
        import datetime
        self.uniquekey= row[23]
        date = row[0].split('/')
        time = row[1].split(':')
        if int(time[1]) >= 30:
            time[0] = str(int(time[0]) + 1)
        time[1] = '00'
        if time[0] == '24':
            time[0] = '00'
        self.date = datetime.date(int(date[2]),int(date[0]),int(date[1]))
        self.ore = datetime.time(int(time[0]),int(time[1]))
        self.latitudine = row[4]
        self.longitudine = row[5]
        self.personeFerite = row[10]
        self.personeMorte = row[11]
        self.pedoniFeriti = row[12]
        self.pedoniMorti = row[13]
        self.ciclistiFeriti = row[14]
        self.ciclistiMorti = row[15]
        self.conducentiMorti = row[16]
        self.conducentiFeriti = row[17]
        self.data = row


    def store(self,cursor,idLuogo):
        import datetime
        date = datetime.datetime.now()
        add_incidente = ("INSERT INTO incidente "
                        "(unique_key,numero_morti,numero_feriti,pedoni_morti,pedoni_feriti,ciclisti_morti,ciclisti_feriti,conducenti_morti,conducenti_feriti,id_luogo,data_incidente,ora_incidente,created_at,updated_at) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        if idLuogo == 0:
            idLuogo = None
        data_incidente = (self.uniquekey,
                          self.personeMorte,
                          self.personeFerite,
                          self.pedoniMorti,
                          self.pedoniFeriti,
                          self.ciclistiMorti,
                          self.ciclistiFeriti,
                          self.conducentiMorti,
                          self.conducentiFeriti,
                          idLuogo,
                          self.date,
                          self.ore,
                          date,
                          date)

        cursor.execute(add_incidente, data_incidente)

        return cursor.lastrowid


