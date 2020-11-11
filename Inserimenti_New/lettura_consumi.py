import os
import pymysql
import sqlite3 as spl
import datetime
import pymysql.cursors


id_lettura = int(input('inserisci id_lettura:' ))
id_contatore = int(input('inserisci id_contatore:' ))
id_utente = int(input('inserisci id_utente:' ))
livello_soglia = str(input('inserisci livello_soglia: '))
lettura1 = float(input('inserisci lettura1: '))
lettura2 = float(input('inserisci lettura2: '))
quantita = int(input('inserisci quantita: '))
data_lettura1 = str(input('inserisci data_lettura1 yyyy-mm-dd: '))
data_lettura2 = str(input('inserisci data_lettura2 yyyy-mm-dd: '))


def add_lettura_consumi_one(id_lettura, id_contatore, id_utente, livello_soglia, lettura1, lettura2, quantita, data_lettura1, data_lettura2) :
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()
    c.execute("INSERT INTO lettura_consumi VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
              (id_lettura, id_contatore, id_utente, livello_soglia, lettura1, lettura2, quantita, data_lettura1, data_lettura2))
    conn.commit()


add_lettura_consumi_one(id_lettura, id_contatore, id_utente, livello_soglia, lettura1, lettura2, quantita, data_lettura1, data_lettura2)
