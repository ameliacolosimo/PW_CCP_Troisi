import os
import pymysql
import sqlite3 as spl
import datetime
import pymysql.cursors


id_contratto = int(input('inserisci id_contratto:' ))
cod_contratto = str(input('inserisci cod_contratto:' ))
descrizione = str(input('inserisci descrizione: '))
id_utente = int(input('inserisci id_utente:' ))
status_contratti = str(input('inserisci status_contratti: '))




def add_contratti_one(id_contratto, cod_contratto, descrizione, id_utente, status_contratti) :
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()
    c.execute("INSERT INTO contratti VALUES (%s, %s, %s, %s, %s)",
              (id_contratto, cod_contratto, descrizione, id_utente, status_contratti))
    conn.commit()


add_contratti_one(id_contratto, cod_contratto, descrizione, id_utente, status_contratti)
