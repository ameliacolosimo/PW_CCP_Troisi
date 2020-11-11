import os
import pymysql
import sqlite3 as spl
import datetime
import pymysql.cursors

conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='acme_energia',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

c = conn.cursor()

def add_istituti_di_pagamento(lista):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()
    c.executemany("INSERT INTO istituti_di_pagamento VALUES (%s, %s, %s, %s, %s, %s, %s)", (lista))
    conn.commit()


istituti_t = [
   ('1', 'BANCA', 'Via Colpu', 'Pizzo', 'VV', '89812', '1'),
   ('2', 'POSTA', 'Via Pignatta', 'Napoli', 'NA', '65478', '2'),
   ('3', 'POSTA', 'Via Appia Nuova', 'Roma', 'RM', '00181', '3'),
   ('4', 'BANCA', 'Via Torlonia', 'Roma', 'RM', '00456', '4'),
   ('5', 'BANCA', 'Via Giunco', 'Milano', 'MI', '56789', '5'),
   ('6', 'POSTA', 'Via Siracusa', 'Bologna', 'BO', '56789', '6'),
   ('7', 'POSTA',  'Via Sant Antonio', 'Maierato', 'VV', '45679', '7'),
   ('8', 'BANCA', 'Via Unità D Italia', 'Venezia', 'VE', '53492', '8'),
   ('9', 'POSTA', 'Via Sant Antonio', 'Maierato', 'VV', '45679', '9'),
   ('10', 'BANCA', 'Via Simone', 'Firenze', 'FI', '56788', '10'),
   ('11', 'POSTA', 'Viale Silco', 'Milano', 'MI', '56789', '11'),
   ('12', 'POSTA', 'Via Frico', 'Milano', 'MI', '67899', '12'),
   ('13', 'BANCA', 'Via Giuncolo', 'Roma', 'RM', '45678', '13'),
   ('14', 'BANCA', 'Via Ara', 'Torino', 'TO', '67487', '14'),
   ('15', 'POSTA',  'Via Fruci', 'Bologna', 'B0', '56787', '15'),
   ]

add_istituti_di_pagamento(istituti_t)

