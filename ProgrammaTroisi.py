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
def show_all():
    c = conn.cursor()
    c.execute("SELECT quantita FROM bollette_emesse")
    items = c.fetchall()
    for item in items:
        print(item)

def add_many(lista):
    c.executemany("INSERT INTO bollette_emesse VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", lista)
    conn.commit()

def add_many1(lista):
    c.executemany("INSERT INTO utenti VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", lista)
    conn.commit()

#ALIQUOTA_IVA = 0.22
#COSTO_UNITARIO = 0.20
#COSTO_UNITARIO_SOCIALE = 0.10
#SOGLIA_CONSUMO_SOCIALE = 50.0

#def calcola_totale(quantità):
 #   importo = 0.0;
  #  if quantità <= SOGLIA_CONSUMO_SOCIALE:
   #     importo = quantità * COSTO_UNITARIO_SOCIALE
    #else:
     #   importo = quantità * COSTO_UNITARIO
