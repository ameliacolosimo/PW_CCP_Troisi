import os
import pymysql
import sqlite3 as spl
import datetime
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       db='ACME_Energia',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
mycursor = conn.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

mycursor = conn.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

mycursor = conn.cursor()
sql = "INSERT INTO contatori( id_contatore, id_utente, quantità_totale) VALUES (%s, %s, %s)"

val = [
    (1, 1, 3678978),
    (2, 2, 3432566435)
]
mycursor.executemany(sql,val)
conn.commit()

