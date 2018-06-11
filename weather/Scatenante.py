
class Scatenante:
    def __init__(self,descrizione):
        self.descrizione = descrizione


    def store(self,cursor):
        import mysql.connector
        import datetime

        import datetime
        date = datetime.datetime.now()
        tomorrow = datetime.date
        time = datetime.time

        exist_tipo = "SELECT * FROM scatenante where descrizione = '"+self.descrizione+"'"
        cursor.execute(exist_tipo)
        exist = False
        for descrizione in cursor:
            id = descrizione[0]
            exist = True
        if not exist:
            add_scatenante = "INSERT INTO scatenante (descrizione,created_at)VALUES ('"+self.descrizione+"','"+str(date)+"')"
            cursor.execute(add_scatenante)
            id = cursor.lastrowid

        return id
