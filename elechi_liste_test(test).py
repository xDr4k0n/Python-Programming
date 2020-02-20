#!/usr/bin/python3

la_mia_lista = [500,700,800,900,'mille',1100,1200]

print(la_mia_lista[0:6])

la_mia_lista[0] = 600
print("----Modificare")
print(la_mia_lista[0:6])
#-----------------------------------------------------------
print("Eliminare 1 elemento. che sta in posizione o")

del la_mia_lista[0]

print(la_mia_lista[0:5])
#-----------------------------------------------------------
print("Quanto e larga la mia lista?  len(la_mia_lista")
print(len(la_mia_lista))

la_mia_lista1 = [321,123,345,1231,5674,8996,554]
print(la_mia_lista1[0:6])
#-----------------------------------------------------------
lista_totale = la_mia_lista1 + la_mia_lista

print(len(lista_totale))
print(lista_totale[0:13])

test_lista3 = lista_totale[0:13] + ['nuova',4553,3322]

print(len(test_lista3))

last_test = [3121,784,32423,56756,34]+[23426,7855,673,123,1465]

print(len(last_test))
