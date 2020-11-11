import os
import pymysql
import sqlite3 as spl
import datetime
import pymysql.cursors


id_guasto = int(input('inserisci id_guasto:' ))
id_contatore = int(input('inserisci id_contatore:' ))
data_inizio = str(input('inserisci data_inizio yyyy-mm-dd: '))
data_fine = str(input('inserisci data_fine yyyy-mm-dd: ' ))
ora_inizio = str(input('inserisci ora_inizio hh:mm:ss: ' ))
ora_fine = str(input('inserisci ora_fine hh:mm:ss: ' ))
descrizione = str(input('inserisci descrizione: ' ))




def add_guasti_one(id_guasto, id_contatore, data_inizio, data_fine, ora_inizio, ora_fine, descrizione) :
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()
    c.execute("INSERT INTO guasti VALUES (%s, %s, %s, %s, %s, %s, %s)",
              (id_guasto, id_contatore, data_inizio, data_fine, ora_inizio, ora_fine, descrizione))
    conn.commit()
