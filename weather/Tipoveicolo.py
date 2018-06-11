
class Tipoveicolo:
    def __init__(self,tipologia):
        self.tipologia = tipologia


    def store(self,cursor):
        import mysql.connector
        import datetime

        import datetime
        date = datetime.datetime.now()

        tomorrow = datetime.date
        time = datetime.time

        exist_tipo = "SELECT * FROM tipoveicolo where tipologia = '"+self.tipologia+"'"
        cursor.execute(exist_tipo)
        exist = False
        for tipologia in cursor:
            id = tipologia[0]
            exist = True
        if not exist:

            add_tipoveicolo = "INSERT INTO tipoveicolo (tipologia,created_at)VALUES ('"+self.tipologia+"','"+str(date)+"')"

            cursor.execute(add_tipoveicolo)
            id = cursor.lastrowid

        return id





