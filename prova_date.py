import os
import pymysql
import sqlite3 as spl
import datetime
import pymysql.cursors
import datetime
import time
import calendar

ALIQUOTA_IVA = float(0.22)
COSTO_UNITARIO = float(0.20)
COSTO_UNITARIO_SOCIALE = float(0.10)
SOGLIA_CONSUMO_SOCIALE = int(50)

tariffa = 0
importo = 0


def calcola_tariffa(quantita):
    if quantita <= SOGLIA_CONSUMO_SOCIALE:
        tariffa_ins = COSTO_UNITARIO_SOCIALE
    else:
        tariffa_ins = COSTO_UNITARIO
    return tariffa_ins


def calcola_importo(regime_fiscale):
    if regime_fiscale == 'esente iva':
        importo_ins = (tariffa) * (quantita)
    elif regime_fiscale == 'soggetto a iva':
        importo_ins = (tariffa * quantita) * (1 + ALIQUOTA_IVA)
    else:
        print('inserimento non valido')
    return importo_ins


# def days_between(d1, d2):
#       d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
#       d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
#       return abs((d2 - d1).days)

# data_pagamento = "2020-10-01"

# oggi = datetime.date.today().strftime("%Y-%m-%d")

# differenza = 0
# differenza = days_between(data_pagamento, oggi)

# def morosità(differenza):
#       if differenza <= 0:
#              morosità = 'in regola'
#       elif differenza > 0:
#              morosità = 'moroso'
#       elif differenza > 0 and solvibilità == 'moroso':
#              morosità = 'gravemente moroso'
#       return morosità


def add_utenti(id_utente, nome, cognome, indirizzo, città, provincia, cap, tipologia_cliente, regime_fiscale,
               solvibilità, regione):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()
    c.execute("INSERT INTO utenti VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
              (id_utente, nome, cognome, indirizzo, città, provincia, cap, tipologia_cliente, regime_fiscale,
               solvibilità, regione))
    conn.commit()


def add_boll_em(id_boll, id_utente, quantita, contratto, tariffa, importo, periodo, data_em, data_scad):
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


def solvibilita():
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia_Troisi',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

    c = conn.cursor()
    c.execute("SELECT u.solvibilita FROM (utenti u JOIN bollette_emesse be ON u.id_utente=be.id_utente) "
              "JOIN bollette_pagate bp ON be.id_bolletta_emessa=bp.id_bolletta_emessa "
              "WHERE be.id_bolletta_emessa IN (SELECT bp.id_bolletta_emessa FROM bollette_pagate bp)")

    items = c.fetchall()

    for item in items:
        print(item)

    # solvibilita()

    id_utente = int(input('inserisci id_utente:'))
    nome = str(input('inserisci nome: '))
    cognome = str(input('inserisci cognome: '))
    indirizzo = str(input('inserisci indirizzo: '))
    città = str(input('inserisci città: '))
    provincia = str(input('inserisci provincia: '))
    cap = str(input('inserisci cap: '))
    tipologia_cliente = str(input('inserisci "privato" o "azienda": '))
    regime_fiscale = str(input('inserisci "esente iva" o "soggetto a iva": '))
    regione = str(input('inserisci regione: '))
    solvibilità = morosità(differenza)

    add_utenti(id_utente, nome, cognome, indirizzo, città, provincia, cap, tipologia_cliente, regime_fiscale,
               solvibilità, regione)


def solv2():
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia_Troisi',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()
    c.execute("SELECT be.id_utente, COUNT(*) as num_bollette_non_pagate " "FROM bollette_emesse as be "
              "WHERE be.id_bolletta_emessa NOT IN (SELECT bp.id_bolletta_emessa "
              "FROM bollette_pagate as bp) GROUP BY be.id_utente")
    items = c.fetchall()
    # for item in items:
    # if :
    #  print('moroso')
    # else:
    #     print('errore')

    # print(item)


solv2()

diz = items

diz = dict()

type(diz)

# lista_solvibili = {solv2()}


# print(lista_solvibili)

# lista_solvibili['num_bollette_non_pagate']
