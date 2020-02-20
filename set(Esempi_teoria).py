#!/usr/bin/python3

mio_set = {'giorno','mese','anno'}




#                             Set di python


#  - una raccolta non ordinata e non indicizzata
#  - parentesi graffe

print(mio_set)
# {'giorno','mese','anno'}




#                         Accedi agli articoli
#Controlla se "anno" è presente nel set:

print('anno' in mio_set)
#risposta e = True




#                           Modifica articoli
#  -non è possibile modificarne gli elementi
#  -ma è possibile aggiungere nuovi elementi




#                           Aggiungi elementi
#                                -add()
#                add() aggiunge nella posizione random
#                          -SOLO UN ELEMENTO
mio_set.add("ora")
print(mio_set)




#                              update()
# più elementi a un set, usando il update() metodo:
mio_set.update(["milenio",'citta','paese'])
print(mio_set)
#   Random!Aggiungi in posizione 





#                   Ottieni la lunghezza di un set
#                                  len()
print(len(mio_set))

#                           Rimuovi oggetto
#Nota: se l'elemento da rimuovere non esiste, remove()genererà un errore.
print("_____________________________________________________________________")
print(mio_set)
mio_set.remove("ora")
print(mio_set)

#Nota: se l'elemento da rimuovere non esiste, remove()genererà un errore.
#                                         discard()
#Nota: se l'elemento da rimuovere non esiste, NONdiscard() genererà un errore.


#                                pop()
print("_____________________________________________________________________")
print(mio_set)
#              pop()metodo, per rimuovere un elemento
#                   rimuoverà l' ultimo elemento (primo)
# Ricorda che i set non sono ordinati, 
# quindi non saprai quale elemento viene rimosso posizione 0
elemento = mio_set.pop()
print("Primo elemento rimosso")
print(elemento)

#                                clear()
#                           rimuovo tutto
print("_____________________________________________________________________")
print(mio_set)
#mio_set.clear()
#print(mio_set)

#                                clear()
#                           rimuovo tutto
#del mio_set
#print(mio_set) ERROR non esiste piu, lho eliminato

print("_____________________________________________________________________")
#                            Unire due set
#union()metodo che restituisce un 
# nuovo set contenente tutti gli elementi di entrambi i set

#update()metodo che inserisce tutti gli elementi di un set in un altro

set1 = {'1','2','3'}
set2 = {'4',5,'6'}
set3 = set1.union(set2)
print(set3)

set11 = {'1','2','3'}
set22 = {'4','5',6}
set33 = set11.update(set22)
print(set33)

#Esistono altri metodi che uniscono due insiemi e mantengono
#  SOLO i duplicati, o MAI i duplicati, controlla l'elenco 
# completo dei metodi dell'insieme in fondo a questa pagina.

#                            Costruttore set!
#Utilizzo del costruttore set () per creare un set
nuovo = set(('Lambo','Porshe','Lexus'))
print(nuovo)

#                            Imposta metodi
#copy
coppy = nuovo.copy()
print(coppy)

#differenza tra una e laltra
dif = coppy.difference(set3)
print(dif)
#                       difference_update()
#         difference_update() rimove coppie tra due set
prova1_1 = {'5','4','3','2'}
prova1_2 = {'6','8','1','2'}
prova = prova1_1.difference_update(prova1_2)
print("_____________________________________________________________________")
print(prova)

#                        intersection() 
#         Il intersection()    metodo restituisce 
# un set che contiene la somiglianza tra due o più set.
#           set.intersection(set1, set2 ... etc)
prova1_3 = {'5','4','3','2'}
prova1_4 = {'6','8','1','2'}
prova11 = prova1_3.difference_update(prova1_4)
print("_____________________________________________________________________")
print(prova11)

#                       intersection_update()
#intersection_update()metodo rimuove gli 
# elementi che non sono presenti in entrambi i set


#                         isdisjoint()
#isdisjoint() metodo restituisce True se nessuno degli 
# elementi è presente in entrambi i set, altrimenti restituisce False.
#                 set.isdisjoint(set)


#                          issubset()
#Il issubset() metodo restituisce True se tutti gli elementi nel set sono presenti 
# nel set specificato, altrimenti ritrasferisce False.
#                   set.issubset(set)


#                        issuperset()
#Il issuperset()metodo restituisce True se tutti gli elementi nel set specificato
#  sono presenti nel set originale, altrimenti restituisce False.
#                     set.issuperset(set)


#                       symmetric_difference()
#Il symmetric_difference() metodo restituisce un set che contiene tutti gli elementi
#  di entrambi i set, ma non gli elementi presenti in entrambi i set.
#                     set.symmetric_difference(set)


#                       symmetric_difference_update()
#Il symmetric_difference_update() metodo aggiorna il set originale rimuovendo gli elementi 
# presenti in entrambi i set e inserendo gli altri elementi.

