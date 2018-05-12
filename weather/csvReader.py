import csv
import mysql
import mysql.connector

from Incidente import Incidente
from Tipoveicolo import Tipoveicolo
from Scatenante import Scatenante
from Luogo import Luogo
from Strada import Strada
from pprint import pprint

passwordSQL = 'passMysql'

def linkLuogoStrada(cursor, idLuogo, idStrada):
    if idLuogo != 0 and idStrada != 0:
        try:
            cursor.execute("INSERT INTO link_luogo_strada (idluogo,idstrada) values (" + str(idLuogo) + "," + str(idStrada) + ")")
        except Exception as t:
            print(t)

def link(cursor,idIncidente,idVeicolo,idScatenante):
    if idVeicolo != 0 or idScatenante != 0:
        cursor.execute("INSERT INTO link (id_incidente,id_scatenante,id_tipoveicolo) values (" + str(idIncidente) + "," + str(idScatenante) + ","+str(idVeicolo)+")")

with open('NYPD_Motor_Vehicle_Collisions.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = True
    cnx = mysql.connector.connect(user='root', password=passwordSQL,
                                  host='localhost',
                                  database='stepone')
    cursor = cnx.cursor()
    i = 0
    for row in reader:
        i = i+1
        if header:
            header = False
            continue
        lu = Luogo(row[2],row[3],row[4],row[5])
        idLuogo = lu.store(cursor)
        print(i)
        st = Strada(row[7])
        idStrada = st.store(cursor)
        linkLuogoStrada(cursor,idLuogo,idStrada)
        inc = Incidente(row)
        idInc = inc.store(cursor, idLuogo)

        s = Scatenante(row[18])
        idscat = s.store(cursor)
        t = Tipoveicolo(row[24])
        idTipo = t.store(cursor)
        link(cursor,idInc,idTipo,idscat)

        s = Scatenante(row[19])
        idscat = s.store(cursor)
        t = Tipoveicolo(row[25])
        idTipo = t.store(cursor)
        link(cursor,idInc,idTipo,idscat)

        s = Scatenante(row[20])
        idscat = s.store(cursor)
        t = Tipoveicolo(row[26])
        idTipo = t.store(cursor)
        link(cursor,idInc,idTipo,idscat)

        s = Scatenante(row[21])
        idscat = s.store(cursor)
        t = Tipoveicolo(row[27])
        idTipo = t.store(cursor)
        link(cursor,idInc,idTipo,idscat)

        s = Scatenante(row[22])
        idscat = s.store(cursor)
        t = Tipoveicolo(row[28])
        idTipo = t.store(cursor)
        link(cursor,idInc,idTipo,idscat)


        if i % 10000 == 0:
             print("commit")
             cnx.commit()


    cnx.commit()
    cursor.close()
    cnx.close()


