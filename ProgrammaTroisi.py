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
c = conn.cursor()
bollette = [ ('1', '1', '3516', '1', '68', '1',  "Maggio-Luglio", '2020-07-10', '2020-07-25'),
    ('2', '2', '3546', '2', '34', '1', "Gennaio-Marzo", '2020-03-02', '2020-03-17'), ]

c.executemany("INSERT INTO bollette_emesse VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", bollette)

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
