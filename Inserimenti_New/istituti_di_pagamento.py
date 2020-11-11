import os
import pymysql
import sqlite3 as spl
import datetime
import pymysql.cursors

id_istituto = int(input('inserisci id_istituto:' ))
tipologia_istituto = str(input('inserisci tipologia_istituto: ' ))
indirizzo = str(input('inserisci indirizzo: '))
citta = str(input('inserisci citta: '))
provincia = str(input('inserisci provincia: '))
CAP = str(input('inserisci CAP: '))
id_utente = int(input('inserisci id_utente:' ))


def add_istituti_di_pagamento_one(id_istituto, tipologia_istituto, indirizzo, citta, provincia, CAP, id_utente) :
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()
    c.execute("INSERT INTO istituti_di_pagamento VALUES (%s, %s, %s, %s, %s, %s, %s)",
              (id_istituto, tipologia_istituto, indirizzo, citta, provincia, CAP, id_utente))
    conn.commit()


add_istituti_di_pagamento_one(id_istituto, tipologia_istituto, indirizzo, citta, provincia, CAP, id_utente)
