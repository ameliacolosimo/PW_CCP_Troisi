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

def add_many(lista):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()
    c.executemany("INSERT INTO guasti VALUES (%s, %s, %s, %s, %s, %s, %s)", (lista))
    conn.commit()

guasti_t = [('1', '1', '2020-7-10', '2020,7,10', '9:00:00', '10:00:00', 'guasti al contatore'),
           ('2', '2', '2020-10-7', '2020-10-7', '12:00:00', '00:00:00', 'pericolo relativo al contatore o alla rete esterna'),
           ('3', '3', '2020-11-9', '2020-11-9', '6:00:00', '23:00:00', 'interruzioni di corrente elettrica'), 
           ('4', '4', '2020-12-15', '2020-12-15', '12:00:00', '3:00:00', 'anomalie sulla rete esterna'),
           ('5', '5', '2020-1-31', '2020-2-1', '23:50:00', '00:5:00', 'guasti al contatore'),
           ('6', '6', '2020-11-11', '2020-11-11', '16:00:00', '16:50:00', 'interruzioni di corrente elettrica'),
           ('7', '7', '2020-1-4', '2020-1-4', '15:00:00', '19:00:00', 'anomalie sulla rete esterna'),
           ('8', '8', '2020-3-12', '2020-3-12', '22:00:00', '23:50:00', 'pericolo relativo al contatore o alla rete esterna'),
           ('9', '9', '2020-4-8', '2020-4-8', '20:50:00', '23:50:00', 'pericolo relativo al contatore o alla rete esterna'),
           ('10', '10', '2020-5-4','2020-5-4', '15:35:00', '19:22:00', 'anomalie sulla rete esterna'),
           ('11', '11', '2020-9-11','2020-9-11', '8:00:00', '16:50:00', 'interruzioni di corrente elettrica'),
           ('12', '12', '2020-7-10', '2020-8-10', '9:00:00', '10:00:00', 'guasti al contatore'),
           ('13', '13', '2020-6-13', '2020-6-13', '10:40:00', '11:50:00', 'interruzioni di corrente elettrica'),
           ('14', '14', '2020-2-2', '2020-2-2', '17:35:00', '23:46:00', 'anomalie sulla rete esterna'),
           ('15', '15', '2020-8-31', '2020-9-1', '23:50:00', '00:5:00', 'guasti al contatore'),]

add_many(guasti_t)
