import ProgrammaTroisi
import os
from typing import List, Tuple
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

bollette = [('7', '1', '3516', '1', '68', '1', 'Maggio-Luglio', '2020-07-10', '2020-07-25'),
                ('8', '2', '3546', '2', '34', '1', 'Gennaio-Marzo', '2020-03-02', '2020-03-17'), ]

ProgrammaTroisi.add_many(bollette)


