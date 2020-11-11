import os
import pymysql
import sqlite3 as spl
import datetime
import pymysql.cursors


id_contatore = int(input('inserisci id_contatore:' ))
id_utente = int(input('inserisci id_utente:' ))
quantita_totale = float(input('inserisci quantita_totale: '))

def add_contatore(id_contatore, id_utente, quantita_totale):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()
    c.execute("INSERT INTO contatori VALUES (%s, %s, %s)",(id_contatore, id_utente, quantita_totale))
    conn.commit()


add_contatore(id_contatore, id_utente, quantita_totale)
