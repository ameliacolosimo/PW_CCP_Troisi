import os
import pymysql
import sqlite3 as spl
import datetime
import pymysql.cursors

conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
c = conn.cursor()

lista = [("1", "Mario", "Rossi", "Via Nazionale", "Pizzo", "VV", "89812", "soggetto a IVA", "in regola", "privato", "Calabria"),
   (2, "Marica", "Marchese", "Via Pignatta", "Napoli", "NA", "65478", "soggetto a IVA", "moroso grave", "privato", "Campania")
]

c.executemany("INSERT INTO utenti VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (lista))

conn.commit()
