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

def add_contratti(lista):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()
    c.executemany("INSERT INTO contratti VALUES (%s, %s, %s, %s,%s)", (lista))
    conn.commit()


contratti_t = [
   ('1', 'A12', 'GAS', '1', 'attivo'),
   ('2', 'B23', 'ACQUA', '2', 'attivo'),
   ('3', 'A34', 'LUCE', '3', 'attivo'),
   ('4', 'C34', 'ACQUA', '4', 'attivo'),
   ('5', 'A23', 'LUCE', '5', 'attivo'),
   ('6', 'D34', 'GAS', '6', 'sospeso'),
   ('7', 'A45', 'GAS', '7', 'attivo'),
   ('8', 'E45', 'LUCE', '8', 'attivo'),
   ('9', 'A67', 'ACQUA', '9', 'attivo'),
   ('10', 'E98', 'GAS', '10', 'attivo'),
   ('11', 'E34', 'LUCE', '11', 'attivo'),
   ('12', 'E87', 'ACQUA', '12', 'attivo'),
   ('13', 'A56', 'GAS', '13', 'sospeso'),
   ('14', 'G56', 'LUCE', '14', 'sospeso'),
   ('15', 'E98', 'GAS', '15', 'attivo'),
   ]

add_contratti(contratti_t)
