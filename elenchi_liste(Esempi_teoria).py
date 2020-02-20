#!/usr/bin/python3

#                           Creazione
# liste - elenco di valori 
lista = [55,'punto',"c",'55', 55]
#         0    1     2    3   4 
# indici di stringa, gli indici di elenco iniziano da 0 e 
# gli elenchi possono essere suddivisi, concatenati e così via
# -non devono essere necessariemente dello stesso tipo


#                       Utilizzo
print("lista[3] : " , lista[3])
print("lista[2:4] : " , lista[2:4]) #2 .3 .4  output


#                      Modificare
#sovrascrivere un elemento della lista "Append"
test_lista = [10,11,22,33]
#              0  1  2  3  
test_lista[0] = 1
# test_lista = [1,11,22,33]

#                          Eliminare
# elenco base
test_lista = [1,11,22,33]
# Eliminare
del test_lista[0]
# Elimino cio che esiste nella positione 0
#della mia lista
test_lista = [11,22,33]


# Altre operazioni che si possono fare sull elenco (Lista)


#                     1. Lunghezza

#                    len(test_lista)
#                 print(len(test_lista))
#               variable = len(test_lista)   


#                    2. Concatenazione
# con variabili senza []
lista_totale = la_mia_lista1 + la_mia_lista

# variabile e lista fisica
test_lista3 = lista_totale[0:13] + ['nuova',4553,3322]

# o liste fisiche
last_test = [3121,784,32423,56756,34] + [23426,7855,673,123,1465]


#               3.Moltiplicazione(Ripetizione)

messaggio = "Ciao, sono Matrix! \n"

print(messaggio*20)

lettere = ['M','a','t','r','i','x']

print(lettere*20)
#               4.Lavorare con i membri

carattere = 'M'
if carattere in messaggio:
    print("La lettera m esiste nella stringa")

if carattere in lettere:
    print("La lettera m esiste nella lista")

for x in lettere:
    print("lettera")

# Indicizzazione ,affettatura e matrici



parole = ['uno', 'due', 'tre']
print(parole[1:]) #['due', 'tre']
print(parole[1])
#output ['due']
print(parole[-1])  #da destra
#output ['tree']

print (max(parole))   #..... ultima parola della lista
print (min(parole))   #uno.... prima parola della lista


#1	list.append (obj)
#Aggiunge l'oggetto all'elenco

#2	list.count (obj)
#Restituisce il conteggio di quante volte si verifica obj nell'elenco

#3	lista.extend (ss)
#Aggiunge il contenuto di seq all'elenco

#4	indice di una lista (obj)
#Restituisce l'indice più basso nell'elenco che appare obj

#5	list.insert (index, obj)
#Inserisce l'oggetto obj nell'elenco nell'elenco dell'indice di offset

#6	list.pop (obj = elenco [-1])
#Rimuove e restituisce l'ultimo oggetto o oggetto dall'elenco

#7	list.remove (obj)
#Rimuove l'oggetto obj dall'elenco

#8	list.reverse ()
#Inverte gli oggetti dell'elenco in atto

#9	list.sort ([func])
#Ordina gli oggetti dell'elenco, se confrontati usa la funzione di confronto