
class Tipoveicolo:
    def __init__(self,tipologia):
        self.tipologia = tipologia


    def store(self,cursor):
        import mysql.connector
        import datetime

        if self.tipologia == "":
            return 0

        tomorrow = datetime.date
        time = datetime.time

        exist_tipo = "SELECT * FROM tipoveicolo where tipologia = '"+self.tipologia+"'"
        cursor.execute(exist_tipo)
        exist = False
        for tipologia in cursor:
            id = tipologia[0]
            exist = True
        if not exist:

            add_tipoveicolo = "INSERT INTO tipoveicolo (tipologia)VALUES ('"+self.tipologia+"')"

            cursor.execute(add_tipoveicolo)
            id = cursor.lastrowid

        return id





