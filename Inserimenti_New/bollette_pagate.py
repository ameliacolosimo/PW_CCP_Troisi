id_boll_pag = int(input('inserisci id_pagamento:' ))
id_boll_em = int(input('inserisci id_bolletta emessa:' ))
data_pag = str(input('inserisci data pagamento yyyy-mm-dd: '))
id_istituto = int(input('inserisci id_istituto: '))
id_utente = int(input('inserisci id_utente:' ))




import os
import pymysql
import sqlite3 as spl
import datetime
import pymysql.cursors



def add_boll_pag(id_boll_pag, id_boll_em, data_pag, id_istituto, id_utente):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()
    c.execute("INSERT INTO bollette_pagate VALUES (%s, %s, %s, %s, %s)", (id_boll_pag, id_boll_em, data_pag, id_istituto, id_utente))
    conn.commit()


add_boll_pag(id_boll_pag, id_boll_em, data_pag, id_istituto, id_utente)

print('End')
