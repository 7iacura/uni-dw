
class Strada:
    def __init__(self,strada):
        self.strada = strada


    def store(self,cursor):
        import datetime

        if self.strada == "":
            return 0



        exist_strada = "SELECT * FROM strada where strada = '"+self.strada.strip().replace("'", "").replace('"', '')+"'"
        cursor.execute(exist_strada)
        exist = False
        for strada in cursor:
            id = strada[0]
            exist = True
        if not exist:
            add_strada = "INSERT INTO strada (strada)VALUES ('"+self.strada.strip().replace("'", "").replace('"', '')+"')"
            cursor.execute(add_strada)
            id = cursor.lastrowid


            # Make sure data is committed to the database

        return id



