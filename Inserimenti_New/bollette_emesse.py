ALIQUOTA_IVA = float(0.22)
COSTO_UNITARIO = float(0.20)
COSTO_UNITARIO_SOCIALE = float(0.10)
SOGLIA_CONSUMO_SOCIALE = int(50)


id_boll = int(input('inserisci id_bolletta:' ))
id_utente = int(input('inserisci id_utente:' ))
quantita = float(input('inserisci quantità consumo: '))
contratto = int(input('inserisci id_contratto: '))
periodo = str(input('inserisci periodo: '))
data_em = str(input('inserisci data emissione: '))
data_scad = str(input('inserisci data scadenza: '))
tariffa_ins = 0
importo_ins = 0

def calcola_tariffa(quantita):

    if quantita <= SOGLIA_CONSUMO_SOCIALE:
        tariffa_ins = COSTO_UNITARIO_SOCIALE
    else:
        tariffa_ins = COSTO_UNITARIO
    return tariffa_ins



tariffa=calcola_tariffa(quantita)

print('La tariffa applicata è: ')
print(tariffa)

regime_fiscale = str(input('inserire "esente iva" o "soggetto a iva": ' ))

def calcola_importo(regime_fiscale):
    if regime_fiscale =='esente iva':
        importo_ins = tariffa*quantita*(1+(ALIQUOTA_IVA))
    elif regime_fiscale =='soggetto a iva':
        importo_ins = tariffa*quantita
    else:
        print('inserimento non valido')
    return importo_ins

importo=calcola_importo(regime_fiscale)
print('Importo totale: ')
print(importo)


import os
import pymysql
import sqlite3 as spl
import datetime
import pymysql.cursors



def add_boll_one(id_boll, id_utente, quantita, contratto, tariffa, importo, periodo, data_em, data_scad):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()
    c.execute("INSERT INTO bollette_emesse VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
              (id_boll, id_utente, quantita, contratto, tariffa, importo, periodo, data_em, data_scad))
    conn.commit()


add_boll_one(id_boll, id_utente, quantita, contratto, tariffa, importo, periodo, data_em, data_scad)
