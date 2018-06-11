
import mysql.connector


from pprint import pprint

passwordSQL = 'katenkyokotsu77?'

cnx = mysql.connector.connect(user='root', password=passwordSQL,
                              host='localhost',
                              database='ods')

cursorInc = cnx.cursor(buffered=True)
cursor = cnx.cursor(buffered=True)

incidenti = "SELECT * FROM incidente i left join luogo l on i.id_luogo = l.id " \
            "left join ods.weather w on w.id = i.id_meteo " \
            "where i.created_at > (select if (MAX(created_at) is null,'1970-01-01 00:00:00',MAX(created_at)) from datawarehouse.incidente)"
print(incidenti)
cursorInc.execute(incidenti)

cnx2 = mysql.connector.connect(user='root', password=passwordSQL,
                               host='localhost',
                               database='datawarehouse')

cursor2 = cnx2.cursor()
for incidente in cursorInc:
    idOds = incidente[0]
    print(idOds)
    add_incidente = ("INSERT INTO incidente "
                     "(unique_key,numero_morti,numero_feriti,pedoni_morti,pedoni_feriti,ciclisti_morti,ciclisti_feriti,conducenti_morti,conducenti_feriti,id_luogo,id_data,id_ora,created_at,id_meteo) "
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)")
    idluogo = "select id from luogo where latitudine = " + str(incidente[18]) +" and longitudine = " +str(incidente[19])
    cursor2.execute(idluogo)
    for id in cursor2:
        idluogo = id[0]
    idmeteo = "select id from weather where data = '" + str(incidente[22]) + "' and ora = '" + str(incidente[23])+"'"
    cursor2.execute(idmeteo)
    for id in cursor2:
        idmeteo = id[0]



    data_incidente = (incidente[1],
                      incidente[2],
                      incidente[3],
                      incidente[4],
                      incidente[5],
                      incidente[6],
                      incidente[7],
                      incidente[8],
                      incidente[9],
                      idluogo,
                      1,
                      1,
                      incidente[13],
                      idmeteo)
    cursor2.execute(add_incidente, data_incidente)

    idDw = cursor2.lastrowid
    cnx2.commit()
    link = "select tipologia,descrizione from link l " \
           "join scatenante s on s.id = l.id_scatenante " \
        "join tipoveicolo v on v.id = l.id_tipoveicolo " \
           "where id_incidente = "+str(idOds)
    cursor.execute(link)
    for l in cursor:
        dettId = "select id from dettagli where tipoveicolo = '"+str(l[0])+"' " \
                 "and scatenante = '"+str(l[1])+"'"
        cursor2.execute(dettId)
        for i in cursor2:
            linkInsert = "insert into link_dettagli(id_incidente,id_dettagli) values (%s,%s)"
            data = (idDw,i[0])
            cursor2.execute(linkInsert, data)
