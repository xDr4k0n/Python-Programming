#!/usr/bin/python3

somma = 0
somma_pari = 0
somma_dispari = 0
valore = 0
numero_valori = 0
contatore = 0
conta_0 = 0
calc_pari = 0
pari = 0
dispari = 0

print("Inserisci il numero massimo di valori !\n") #Max Valori
numero_valori =int(input()) #Input 

while numero_valori > contatore:
    print("Inserisci valore! \n")
    valore =int(input()) #Input 
    if valore == 0:
    	#Vero
    	conta_0 = conta_0 + 1
    else:
    	calc_pari = valore % 2
    	if calc_pari == 0:
            #Vero
    		pari = pari + 1
    		somma_pari = somma_pari + valore
    	else:
            dispari = dispari + 1
            somma_dispari = somma_dispari + valore
    	
    somma = somma + valore
    contatore = contatore + 1
    
print("Il totale numeri e : ", numero_valori)
print("La somma totale e : ", somma)
#************************************************************
print("Totale numeri pari e : ", pari)
print("La somma dei numeri pari e : ", somma_pari)
#************************************************************
print("Totale numeri pari e : ", dispari)
print("La somma dei numeri pari e : ", somma_dispari)
#************************************************************
print("Numero totale di 0 e : ", conta_0)