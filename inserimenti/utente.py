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

def add_utenti(lista):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()
    c.executemany("INSERT INTO utenti VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (lista))
    conn.commit()

utenti_t = [
    ('1', 'Mario', 'Rossi', 'Via Nazionale', 'Pizzo', 'VV', '89812', 'soggetto a IVA', 'in regola', 'privato', 'Calabria'),
    ('2', 'Marica', 'Marchese', 'Via Pignatta', 'Napoli', 'NA', '65478', 'soggetto a IVA', 'in regola', 'privato', 'Campania'),
    ('3', 'Luca', 'Gammo', 'Via Appia Nuova', 'Roma', 'RM', '00181', 'esente IVA', 'moroso', 'azienda', 'Lazio'),
    ('4', 'Rocco', 'Stillitani', 'Via XXV Aprile', 'Roma', 'RM', '00456', 'soggetto a IVA', 'in regola', 'privato', 'Lazio'),
    ('5', 'Rossana', 'Gallo', 'Viale Arcala', 'Milano', 'MI', '56789', 'esente IVA', 'in regola', 'azienda', 'Lombardia'),
    ('6', 'Federica', 'Galfo', 'Via Siracusa', 'Bologna', 'BO', '56789', 'soggetto a IVA', 'moroso grave', 'privato', 'Emilia-Romagna'),
    ('7', 'Carmela', 'Cortese', 'Via Sant Antonio', 'Maierato', 'VV', '45679', 'esente IVA', 'in regola', 'azienda', 'Calabria'),
    ('8', 'Filippo', 'Callipo', 'Via Milino', 'Venezia', 'VE', '53492', 'esente IVA', 'in regola', 'azienda', 'Veneto'),
    ('9', 'Miriam', 'Cugliari', 'Via Ripa', 'Torino', 'TO', '45678', 'soggetto a IVA', 'in regola', 'privato', 'Veneto'),
    ('10', 'Francesca', 'De Pasquale', 'Via Torli', 'Firenze', 'FI', '56788', 'esente IVA', 'in regola', 'azienda', 'Toscana'),
    ('11', 'Giuseppe', 'Calfapietra',  'Viale Silco', 'Milano', 'MI', '56789', 'esente IVA', 'moroso', 'azienda', 'Lombardia'),
    ('12', 'Lucia', 'Conti', 'Via Frico', 'Milano', 'MI', '67899', 'soggetto a IVA', 'in regola', 'privato', 'Lombardia'),
    ('13', 'Marco', 'Porcella', 'Viale Fiorito', 'Roma', 'RM', '45678', 'soggetto a IVA', 'moroso grave', 'privato', 'Lazio'),
    ('14', 'Andrea', 'Lepanto', 'Via Po', 'Torino', 'TO', '67487', 'esente IVA', 'moroso grave', 'azienda', 'Piemonte'),
    ('15', 'Sara', 'Giuliani', 'Via Fruci', 'Bologna', 'B0', '56787', 'soggetto a IVA', 'in regola', 'privato', 'Emilia-Romagna'),
    ]


add_utenti(utenti_t)
