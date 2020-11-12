import datetime
import time
import calendar


def days_between(d1, d2):
       d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
       d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
       return abs((d2 - d1).days)

data_pagamento = "2020-10-01"

oggi = datetime.date.today().strftime("%Y-%m-%d")


#data_odierna = "2020-11-11"

#data_oggi = datetime.strptime.today()

#print(today)

#oggi = datetime.datetime.now()

differenza = days_between(data_pagamento, oggi)

print(differenza)


def solvibilità(differenza):
       if differenza <= 0:
              solvibilita = 'in regola'
       elif differenza > 0:
              solvibilità = 'moroso'
       
              
