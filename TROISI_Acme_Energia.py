#********** IMPORT DEI PACKAGE UTILI ***********

import os
import pymysql
import sqlite3 as spl
import datetime
import pymysql.cursors
import datetime
import time
import calendar



#********** STAMPA DEI COMANDI UTILI A COMPILARE UN RECORD PER LA TABELLA SCELTA ***********



def stampa_comandi():
    print('********************')
    print('********************')
    print('1 - Registra nuovo utente')
    print('2 - Registra nuova bolletta emessa')
    print('3 - Registra nuovo istituto di pagamento')
    print('4 - Registra lettura dei consumi')
    print('5 - Registra guasto')
    print('6 - Registra pagamento bolletta')
    print('7 - Registra nuovo contratto')
    print('8 - Registra dati contattore')
    print('0 - quit')
    print('********************')




#*********** PRIMA PARTE DI FUNZIONI UTILI AL CALCOLO DI ALCUNE VARIABILI ***********

    

# Viene definita una funzione per ottenere una differenza in giorni tra due date,
# utile a stabilire la morosità dell'utente

def days_between(d1, d2):
       d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
       d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
       oggi = datetime.date.today().strftime("%Y-%m-%d")
       return abs((d2 - d1).days)

#differenza = 0
#data_pagamento = "2020-10-01"
#differenza = days_between(data_pagamento, oggi)
#print(differenza)


# Variabili utili all'attribuzione di valori in per le variabili tariffa e importo

ALIQUOTA_IVA = float(0.22)
COSTO_UNITARIO = float(0.20)
COSTO_UNITARIO_SOCIALE = float(0.10)
SOGLIA_CONSUMO_SOCIALE = int(50)

tariffa = 0
importo = 0


# Funzione per calcolare la tariffa

def calcola_tariffa(quantita):
    if quantita <= SOGLIA_CONSUMO_SOCIALE:
        tariffa_ins = COSTO_UNITARIO_SOCIALE
    else:
        tariffa_ins = COSTO_UNITARIO
    return tariffa_ins


# Funzione per calcolare l'importo totoale della bolletta

def calcola_importo(regime_fiscale):
    if regime_fiscale =='esente iva':
        importo_ins = (tariffa)*(quantita)
    elif regime_fiscale =='soggetto a iva':
        importo_ins = (tariffa*quantita)*(1+ALIQUOTA_IVA)
    else:
        print('inserimento non valido')
    return importo_ins


# Funzione per stabilire morosità

def morosità(differenza):
       if differenza <= 0:
              morosità = 'in regola'
       elif differenza > 0:
              morosità = 'moroso'
       elif differenza > 0 and solvibilità == 'moroso':
              morosità = 'gravemente moroso'
       return morosità






#*********** FUNZIONI PER L'INSERIMENTO DI RECORD IN OGNI TABELLA CORRISPONDENTE ***********





# PREMESSA GENERALE = in ogni funzione, viene prima stabilito un collegamento con il DB sulla piattaforma php;
                    # viene poi usato un "cursore" il quale va a posizionarsi nella query in SQL;
                    # ciò avviene attraverso il comando execute.
                    # Alla fine della query, si aggiorna il DB attraverso il comando conn.commit()




# Funzione inserimento in tabella 'utenti'

def add_utenti(id_utente, nome, cognome, indirizzo, città, provincia, cap, tipologia_cliente, regime_fiscale, solvibilità, regione):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()
    c.execute("INSERT INTO utenti VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
              (id_utente, nome, cognome, indirizzo, città, provincia, cap, tipologia_cliente, regime_fiscale, solvibilità, regione))
    conn.commit()


# Funzione inserimento in tabella 'bollette_emesse'

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



# Funzione inserimento in tabella 'istituti_di_pagamento'

def add_istituti_di_pagamento(id_istituto, tipologia_istituto, indirizzo, citta, provincia, CAP, id_utente) :
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()
    c.execute("INSERT INTO istituti_di_pagamento VALUES (%s, %s, %s, %s, %s, %s, %s)",
              (id_istituto, tipologia_istituto, indirizzo, citta, provincia, CAP, id_utente))
    conn.commit()



# Funzione inserimento in tabella 'lettura_consumi'

def add_lettura_consumi(id_lettura, id_contatore, id_utente, livello_soglia, lettura1, lettura2, quantita, data_lettura1, data_lettura2) :
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()
    c.execute("INSERT INTO lettura_consumi VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
              (id_lettura, id_contatore, id_utente, livello_soglia, lettura1, lettura2, quantita, data_lettura1, data_lettura2))
    conn.commit()



#funzione inserimento in tabella 'guasti'

def add_guasti(id_guasto, id_contatore, data_inizio, data_fine, ora_inizio, ora_fine, descrizione):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()
    c.execute("INSERT INTO guasti VALUES (%s, %s, %s, %s, %s, %s, %s)",
              (id_guasto, id_contatore, data_inizio, data_fine, ora_inizio, ora_fine, descrizione))
    conn.commit()



#funzione inserimento in tabella 'bollette_pagate'

def add_boll_pag(id_boll_pag, id_boll_em, data_pag, id_istituto, id_utente):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()
    c.execute("INSERT INTO bollette_pagate VALUES (%s, %s, %s, %s, %s)", (id_boll_pag, id_boll_em, data_pag, id_istituto, id_utente))
    conn.commit()



#funzione inserimento in tabella 'contratti'

def add_contratti(id_contratto, cod_contratto, descrizione, id_utente, status_contratti) :
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()
    c.execute("INSERT INTO contratti VALUES (%s, %s, %s, %s, %s)",
              (id_contratto, cod_contratto, descrizione, id_utente, status_contratti))
    conn.commit()



#funzione inserimento in tabella 'contatore'

def add_contatore(id_contatore, id_utente, quantita_totale):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='ACME_Energia',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()
    c.execute("INSERT INTO contatori VALUES (%s, %s, %s)",(id_contatore, id_utente, quantita_totale))
    conn.commit()







#********** PARTE DI __MAIN__ PER L'ESECUZIONE DELLE FUNZIONI ***********

    


# Il main è la parte effettiva di esecuzione del programma;
# Esso permette l'inserimento, tramite input dalla Shell, dei record che andranno a popolare le tabelle
# WHILE = attraverso while True, viene definito un ciclo di funzioni che viene ripetuto n volte
# BREAK = tale ciclo verrà interrotto attraverso il comando break se inserito l'input 0 nella variabile comando

# IF = Ogni if-clause si compone di:
                        #un richiamo alla 'def stampa_comandi()' attraverso la variabile 'comando';
                        #una serie di variabili da compilare tramite input;
                        #eventuali richiami ad altre funzioni per la valorizzazione delle variabili;
                        #richiamo alla funzione che permette il riempimento delle suddette variabili nel DB relazionale;



while True:
    stampa_comandi()
    print('Digita comando')
    comando=int(input('>>> '))



    if comando==1:
        id_utente = int(input('inserisci id_utente:' ))
        nome = str(input('inserisci nome: '))
        cognome = str(input('inserisci cognome: '))
        indirizzo = str(input('inserisci indirizzo: '))
        città = str(input('inserisci città: '))
        provincia = str(input('inserisci provincia: '))
        cap = str(input('inserisci cap: '))
        tipologia_cliente = str(input('inserisci "privato" o "azienda": '))
        regime_fiscale = str(input('inserisci "esente iva" o "soggetto a iva": ' ))
        regione = str(input('inserisci regione: '))
        solvibilità = 'in regola' #il nuovo utente risulta sempre in regola all'inizio del contratto
        
        add_utenti(id_utente, nome, cognome, indirizzo, città, provincia, cap, tipologia_cliente, regime_fiscale, solvibilità, regione)
        

    elif comando==2:
        id_boll = int(input('inserisci id_bolletta:' ))
        id_utente = int(input('inserisci id_utente:' ))
        quantita = float(input('inserisci quantità consumo: '))
        contratto = int(input('inserisci id_contratto: '))
        periodo = str(input('inserisci periodo: '))
        data_em = str(input('inserisci data emissione: '))
        data_scad = str(input('inserisci data scadenza: '))
        regime_fiscale = str(input('inserisci "esente iva" o "soggetto a iva": ' ))
        tariffa = calcola_tariffa(quantita)
        importo = calcola_importo(regime_fiscale)

        add_boll_em(id_boll, id_utente, quantita, contratto, tariffa, importo, periodo, data_em, data_scad)
        

    elif comando==3:
        id_istituto = int(input('inserisci id_istituto:' ))
        tipologia_istituto = str(input('inserisci tipologia_istituto: ' ))
        indirizzo = str(input('inserisci indirizzo: '))
        citta = str(input('inserisci citta: '))
        provincia = str(input('inserisci provincia: '))
        CAP = str(input('inserisci CAP: '))
        id_utente = int(input('inserisci id_utente:' ))

        add_istituti_di_pagamento(id_istituto, tipologia_istituto, indirizzo, citta, provincia, CAP, id_utente)


    elif comando==4:
        id_lettura = int(input('inserisci id_lettura:' ))
        id_contatore = int(input('inserisci id_contatore:' ))
        id_utente = int(input('inserisci id_utente:' ))
        livello_soglia = str(input('inserisci livello_soglia: '))
        lettura1 = float(input('inserisci lettura1: '))
        lettura2 = float(input('inserisci lettura2: '))
        quantita = int(input('inserisci quantita: '))
        data_lettura1 = str(input('inserisci data_lettura1 yyyy-mm-dd: '))
        data_lettura2 = str(input('inserisci data_lettura2 yyyy-mm-dd: '))

        add_lettura_consumi(id_lettura, id_contatore, id_utente, livello_soglia, lettura1, lettura2, quantita, data_lettura1, data_lettura2)


    elif comando==5:
        id_guasto = int(input('inserisci id_guasto:' ))
        id_contatore = int(input('inserisci id_contatore:' ))
        data_inizio = str(input('inserisci data_inizio yyyy-mm-dd: '))
        data_fine = str(input('inserisci data_fine yyyy-mm-dd: ' ))
        ora_inizio = str(input('inserisci ora_inizio hh:mm:ss: ' ))
        ora_fine = str(input('inserisci ora_fine hh:mm:ss: ' ))
        descrizione = str(input('inserisci descrizione: ' ))

        add_guasti(id_guasto, id_contatore, data_inizio, data_fine, ora_inizio, ora_fine, descrizione)

    elif comando==6:
        id_boll_pag = int(input('inserisci id_pagamento:' ))
        id_boll_em = int(input('inserisci id_bolletta emessa:' ))
        data_pag = str(input('inserisci data pagamento yyyy-mm-dd: '))
        id_istituto = int(input('inserisci id_istituto: '))
        id_utente = int(input('inserisci id_utente:' ))

        add_boll_pag(id_boll_pag, id_boll_em, data_pag, id_istituto, id_utente)


    elif comando==7:
        id_contratto = int(input('inserisci id_contratto:' ))
        cod_contratto = str(input('inserisci cod_contratto:' ))
        descrizione = str(input('inserisci descrizione: '))
        id_utente = int(input('inserisci id_utente:' ))
        status_contratti = str(input('inserisci status_contratti: '))

        add_contratti(id_contratto, cod_contratto, descrizione, id_utente, status_contratti)


    elif comando==8:
        id_contatore = int(input('inserisci id_contatore:' ))
        id_utente = int(input('inserisci id_utente:' ))
        quantita_totale = float(input('inserisci quantita_totale: '))

        add_contatore(id_contatore, id_utente, quantita_totale)


    elif comando==0:
        break
    else:
        print('Errore')
