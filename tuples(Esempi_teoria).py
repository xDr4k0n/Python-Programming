#!/usr/bin/python3

def cmp(a, b):
    return (a > b) - (a < b) 


tuples = ('Matrix', 'All_united',2000,2001)
#tupla - oggetti Python immutabili
#Le tuple sono sequenze, come gli elenchi.
#Le differenze tra tuple ed elenchi(list) sono :
#  - tuple non possono essere cambiate.
#  - tuple usano parentesi.
#  - elenchi(liste) possono essere cambiate.
#  - elenchi usano parentesi quadre.
#  - Non si possono copiare dentro le variabili
#  - neanche la misura della tuple

tuple1 = ()
# tupla vuota è scritta come due parentesi che non contengono nulla


tuple2 = (12,)

#Per scrivere una tupla contenente un singolo valore 
# devi includere una virgola, anche se esiste un solo valore


tuplessss = ('OpenMind', 'All_united',2000)
#                0            1        2
#Come gli indici di stringa, gli indici di tupla iniziano da 
# 0 e possono essere suddivisi, concatenati e così via.


#                    Accesso ai valori in Tuple

#tuplessss = ('OpenMind', 'All_united',2000)
print(tuplessss[1])#    2000
print(tuplessss[1:2])# 'All_united'

#                     Aggiornamento tuple(Unione)
# -non è possibile aggiornare o modificare i valori 
# degli elementi tupla.
# -Puoi prendere porzioni di tuple esistenti 
#  per creare nuove tuple 

tuples_g = tuples + tuplessss

print(tuples_g)
#                            Comparazione
tup1 = (1,2,3,4)
tup2 = (1,2,3,4)
#! python non ha il cmp pero posso crearlo io sotto forma
#def cmp(a, b):
    #return (a > b) - (a < b) 
print("cmp(tup1, tup2")
print(cmp(tup1, tup2))

#cmp() returns -1 if x < y
#cmp() returns 0 if  x == y
#cmp() returns 1 if  x > y
#Dopo la prova si puo notare che le tuples si possono comparare....
#Funziona anche con pozitioni
print("cmp(tup1[1], tup2[1]")
print(cmp(tup1[1], tup2[1]))
print("cmp(tup1[1], tup2[2])")
print(cmp(tup1[1], tup2[2]))

#                                 Misura -> len()
print("Misura")
print(len(tuples_g))
#                               Selezione -> min()
#Voglio il oggeto nella positione minore(la piu piccola) 0
print("Positione minima")
#min(tuples_g)
#                               Selezione -> max()
#Voglio il oggeto nella positione maggiore(ultima posizione) posizione massima
print("Positione massima")
#max(tuples_g)

#                         CONVERSIONE liste in tuples !
bad_list = ['b.u.g mafia','-pantelimon']
print("La mia lista",bad_list)
la_mia_tuple = tuple(bad_list)
print("La mia tuple",la_mia_tuple)