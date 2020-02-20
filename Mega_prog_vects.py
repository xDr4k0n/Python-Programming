import numpy as np
from random import randrange

#------------------------------------------------------------------------------------------------------------------------

def menu():
    print("\n\n\n\n")
    print("          Menu")
    print("1. Somma di un array")
    print("2. Media di un array")
    print("3. Sommare 2 array(Posizione con posizione)")
    print("4. Media 2 array(Posizione con posizione)")
    print("0. Per uscire")


def info_carica():
    print("       Option")
    print("1. Caricamento automatico,")
    print("2. Caricamento manuale.")



def input_scelta():
    option = int(input("Inserisci scelta : "))
    return option


def carica_manuale(vet):
    i = 0
    j = 0
    for i in vet:
        vet[j] = int(input("Inserisci numero : "))
        j = j + 1
    #caricamento manuale vettore

def carica_automatica(vet):
    i = 0
    j = 0
    for i in vet:
        vet[j] = randrange(100)
        j = j + 1
    #caricamento vettore
def visualizza(vet):
    i = 0
    j = 0
    for i in vet:
        print(j+1,"-->", vet[j])
        j = j + 1
    #visualizza vettore



def sommatore(vet):
    i = 0
    j = 0
    somma = 0
    for i in vet:
        somma = somma + vet[j]  
        j = j + 1
    return somma
    #caricamento vettore

def sommatore_2_array_positione_con_positione(array_1,array_2,finale_array):
    i = 0
    j = 0
    for i in array_1:
        finale_array[j] = array_1[j] + array_2[j]  
        j = j + 1

def mediatore_2_array_positione_con_positione(array_1,array_2,finale_array):
    i = 0
    j = 0
    for i in array_1:
        finale_array[j] = (array_1[j] + array_2[j]) / 2  
        j = j + 1
#------------------------------------------------------------------------------------------------------------------------



# --------------------Fake Main-------------------------
#                   "Dichiarazioni"
numeri = np.zeros([10, 1], dtype=int)
numeri2 = np.zeros([10, 1], dtype=int)
usura_somma = np.zeros([10, 1], dtype=int)
usura_media_risultato = np.zeros([10, 1], dtype=float)
ritorno_somma = 0
carica = 10
risposta = 9
aiuto_media = 0


#-----------------------Scheletto-----------------------------
while risposta != 0:
    menu()
    carica = 10
    risposta = input_scelta()
    #Risposta 1 Somma array
    #------------------------------------------------------------------------------------------------------------------------
    #SOMMA
    if risposta == 1:
        while (carica != 1 and carica !=2) :
            info_carica()
            carica = input_scelta()
            if carica == 1:
                #carica automatica
                carica_automatica(numeri)
                visualizza(numeri)
                ritorno_somma = sommatore(numeri)
                print("La tua somma totale e :",ritorno_somma)
            elif carica == 2:
                #carica manuale
                carica_manuale(numeri)
                ritorno_somma = sommatore(numeri)
                print("La tua somma totale e :",ritorno_somma)
    #SOMMA 
    #------------------------------------------------------------------------------------------------------------------------   
    #MEDIA
    elif risposta == 2:
        while (carica != 1 and carica !=2) :
            info_carica()
            carica = input_scelta()
            if carica == 1:
                carica_automatica(numeri)
                visualizza(numeri)
                ritorno_somma = sommatore(numeri)
                aiuto_media = (ritorno_somma / 10)
                print("La tua Media totale e :", aiuto_media)
                #carica automatica
            elif carica == 2:
                carica_manuale(numeri)
                ritorno_somma = sommatore(numeri)
                aiuto_media = (ritorno_somma / 10)
                print("La tua Media totale e :", aiuto_media)
                #carica manuale
    #MEDIA
    #------------------------------------------------------------------------------------------------------------------------
    #SOMMA 2 vettori
    elif risposta == 3:
        while (carica != 1 and carica !=2) :
            info_carica()
            carica = input_scelta()
            if carica == 1:
                print("--------------Primo Array----------------")
                carica_automatica(numeri)
                visualizza(numeri)
                print("--------------Secondo Array--------------")
                carica_automatica(numeri2)
                visualizza(numeri2)
                sommatore_2_array_positione_con_positione(numeri,numeri2,usura_somma)
                print("-----------------Somma Finale------------")
                visualizza(usura_somma)
                #carica automatica
            elif carica == 2:
                print("--------------Primo Array----------------")
                carica_manuale(numeri)
                print("--------------Secondo Array--------------")
                carica_manuale(numeri2)
                sommatore_2_array_positione_con_positione(numeri,numeri2,usura_somma)
                print("-----------------Somma Finale------------")
                visualizza(usura_somma)
                #carica manuale
    #SOMMA 2 vettori
    #------------------------------------------------------------------------------------------------------------------------
    #Media 2 vettori
    elif risposta == 4:
        while (carica != 1 and carica !=2) :
            info_carica()
            carica = input_scelta()
            if carica == 1:
                print("--------------Primo Array----------------")
                carica_automatica(numeri)
                visualizza(numeri)
                print("--------------Secondo Array--------------")
                carica_automatica(numeri2)
                visualizza(numeri2)
                mediatore_2_array_positione_con_positione(numeri,numeri2,usura_media_risultato)
                print("-----------------Media Finale------------")
                visualizza(usura_media_risultato)
                #carica automatica
            elif carica == 2:
                print("--------------Primo Array----------------")
                carica_manuale(numeri)
                print("--------------Secondo Array--------------")
                carica_manuale(numeri2)
                mediatore_2_array_positione_con_positione(numeri,numeri2,usura_media_risultato)
                print("-----------------Media Finale------------")
                visualizza(usura_media_risultato)
                #carica manuale
    #Media 2 vettori
#------------------------------------------------------------------------------------------------------------------------