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
    (5, 1, 3678978),
    (6, 2, 3432566435)]

conn.commit()

sql = "INSERT INTO bollette_emesse (id_bolletta_emessa, id_utente, quantita, " \
      "id_contratto, tariffa, importo, periodo_riferimento, data_emissione, data_scadenza) " \
      "VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s)"

val = [
    (1,1,3516, 1, 68, 0,  "Maggio-Luglio", datetime.date (2020,07,10), detatime.date  (2020,07,25),
    (2, 2, 3546, 2, 34, 0, "Gennaio-Marzo", datetime.date (2020,03,02), datetime.date  (2020,03,17)]

ALIQUOTA_IVA = 0.22
COSTO_UNITARIO = 0.20
COSTO_UNITARIO_SOCIALE = 0.10
SOGLIA_CONSUMO_SOCIALE = 50.0

def calcola_totale(quantità):
    importo = 0.0;
    if quantità <= SOGLIA_CONSUMO_SOCIALE:
        importo = quantità * COSTO_UNITARIO_SOCIALE
    else:
        importo = quantità * COSTO_UNITARIO
