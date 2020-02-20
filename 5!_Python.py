#!/usr/bin/python3



print("Inserisci valore! \n")
valore_originale = int(input())

valore = valore_originale
contatore = 1
moltiplicatore = 1
valore_originale = 0

while valore > contatore :

	print("Test valore : ", valore)
	moltiplicatore = moltiplicatore * valore
	valore = valore - 1

print("\n\n\n")
print("Il risultato e : ", moltiplicatore)