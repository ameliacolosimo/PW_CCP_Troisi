import os
import pymysql
import sqlite3 as spl
import pymysql.cursors
import datetime
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       db='ACME_Energia',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()



