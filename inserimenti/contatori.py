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

def add_contatori(lista):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()
    c.executemany("INSERT INTO contatori VALUES (%s, %s, %s)", (lista))
    conn.commit()


contatori_t = [
    (1,1,367897834),
    (2,2,3432566435),
    (3,2,455661356),
    (4,1,667465778),
    (5,6,1000239656),
    (6,3,448245632),
    (7,4,9812007539),
    (8,5,1134227539),
    (9,7,3302846541),
    (10,8,210093214),
    (11,9,4533997412),
    (12,10,812740954),
    (13,3,112878541),
    (14,2,672195951),
    (15,10,20065498),
    (16,11,485295545),
    (17,12,894516541),
    (18,13,646565416),
    (19,15,654665656),
    (20,14,516146562)
   ]

add_contatori(contatori_t)
