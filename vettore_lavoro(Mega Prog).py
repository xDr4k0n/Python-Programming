import numpy as np
from random import randrange


def info_start_menu_programma():
    print("-----------------------------------------------")
    print("------------------Main menu--------------------")
    print("---1)            Riempimento                ---")
    print("---2)            Ordinamento                ---")
    print("---                  -Min maggiore          ---")
    print("---                    (Bubble sort)        ---")
    print("---                  -Maggiore minore       ---")
    print("---                    (Bubble sort)        ---")
    print("---3)           Visualizza Vettore          ---")
    print("---4)            Cerca Numero               ---")
    print("---                 -Risultato: Positione(1)---")
    print("---                 -Risultato: Positioni   ---")
    print("---                 -Pari (totale)          ---")
    print("---                 -Dispari (totale)       ---")
    print("---                 -Minimo                 ---")
    print("---                 -Massimo                ---")
    print("-----------------------------------------------")
    print("---0)                 EXIT                  ---")
    print("-----------------------------------------------")
    print("Inserisci decisione :")
    decisione = int(input(""))
    return decisione

def info_start_vector_dimensione():
    print("-----------------------------------------------------------")
    print("--------------------------Start----------------------------")
    print("---   Programma si basa sul 'vettore', per con tinuare, ---")
    print("---inserisci greandezza del vettore prima di entrare nel---")
    print("---main menu del prog.                                  ---")
    print("-----------------------------------------------------------")
    print("---      Quanto vuoi che sia grande il tuo vettore?     ---")
    print("-----------------------------------------------------------")
    print("Inserisci grandezza vettore(array) :")
    dimensione = int(input(""))
    return dimensione

def info_riempimento_1_optioni():
    print("-----------------------------------------------")
    print("--------------Riempimento vettore--------------")
    print("---                Optioni                  ---")
    print("---       1 = Riempimento automatico        ---")
    print("---        2 = Riempimento manuale          ---")
    print("---            3 = Indietro                 ---")
    print("-----------------------------------------------")
    decisione = int(input(""))
    return decisione

def info_ordinamento_2_optioni():
    print("-----------------------------------------------")
    print("-----------------Ordinamento-------------------")
    print("---                Optioni                  ---")
    print("---1. Ordinamento vettore (minimo - massimo)---")
    print("---2. Ordinamento vettore (massimo - minimo)---")
    print("---            3 = Indietro                 ---")
    print("-----------------------------------------------")
    decisione = int(input(""))
    return decisione

def info_cerca_4_optioni():
    print("-----------------------------------------------")
    print("-----------------   Cerca   -------------------")
    print("---                Optioni                  ---")
    print("---1) Positione 'Un numero se esistente'    ---")
    print("---2) Positioni 'Se esistente,e volte pres.'---")
    print("---3)           Cerca Pari                  ---")
    print("---4)           Cerca Dispari               ---")
    print("---5)              Minimo                   ---")
    print("---6)              Massimo                  ---")
    print("-----------------------------------------------")
    print("---9)Back                                   ---")
    print("-----------------------------------------------")
    decisione = int(input(""))
    return decisione

def carica_manuale(vet):
    i=0
    j=0
    for i in vet:
        vet[j] = int(input("Inserisci numero : "))
        j = j + 1
    #caricamento manuale vettore

def carica_automatica(vet):
    i=0
    j=0
    for i in vet:
        vet[j] = randrange(40)
        j = j + 1
    #caricamento vettore

def visualizza(vet):
    i=0
    j=0
    for i in vet:
        print(j+1,"-->", vet[j])
        j = j + 1
    #visualizza vettore


def ordina_min_max(vet,dim):
    i=0
    j=0
    m=0
    n=1
    for i in vet:
        j=0
        n=1
        print("1")
        for m in vet:
            print("2")
            if n != 8:
                if vet[j] > vet[n]:
                    print("3")
                    aiuto = vet[j]
                    aiuto2 = vet[n]
                    vet[n] = aiuto
                    vet[j] = aiuto2
                    visualizza(vet)
                j=j+1
                n=n+1






    
#    i = 0
#    j = 1
#    secchio_1 = 0
#    secchio_2 = 0
#    uso2 = dim -1
#    while i < uso2:
#        print("1")
#        while i < j:
#            print("2")
#            if vet[i] > vet[j]:
#                print("3")
#                secchio_1 = vet[j]
#                secchio_2 = vet[i]
#                vet[j] = secchio_2
#                vet[i] = secchio_1
#            j=j+1
#        i=i+1










# --------------------Fake Main-------------------------
#                   "Dichiarazioni"

dimensione = info_start_vector_dimensione()
numeri = np.zeros([dimensione, 1], dtype=int)
decisione_main = 1
#decisione_main
#decisione_ordinamento
#decisione_riempimento
#decisione_cerca

#-----------------------Scheletto-----------------------------


while decisione_main !=0:
    decisione_main = info_start_menu_programma()
    if decisione_main == 1:
        #riempimento------------------------------------------------------------------------------------
        decisione_riempimento = info_riempimento_1_optioni()
        while (decisione_riempimento == 1 or decisione_riempimento == 2):
            if decisione_riempimento == 1 :
                #riempimento automatico
                carica_automatica(numeri)
                visualizza(numeri)
            elif decisione_riempimento == 2 :
                #riempimento manuale
                carica_manuale(numeri)
                visualizza(numeri)
            decisione_riempimento = info_riempimento_1_optioni()
        #riempimento------------------------------------------------------------------------------------
#11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    elif decisione_main == 2:
        #ordinamento------------------------------------------------------------------------------------
        decisione_ordinamento = info_ordinamento_2_optioni()
        while (decisione_ordinamento == 1 or decisione_ordinamento == 2):
            if decisione_ordinamento == 1 :
                ordina_min_max(numeri,dimensione)
                visualizza(numeri)
                #(minimo - massimo)
                print("-----------------------------------------------------------\n")
            elif decisione_ordinamento == 2 :
                visualizza(numeri)
                #(massimo - minimo)
                print("-----------------------------------------------------------\n")
            decisione_ordinamento = info_ordinamento_2_optioni()



        #ordinamento------------------------------------------------------------------------------------
#222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
    elif decisione_main == 3:
        #visualizza-------------------------------------------------------------------------------------
        visualizza(numeri)

        #visualizza-------------------------------------------------------------------------------------
#333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    elif decisione_main == 4:
        #cerca------------------------------------------------------------------------------------------
        decisione_cerca = info_cerca_4_optioni()
        while (decisione_cerca != 9):
            if decisione_cerca == 1 :
                #Positione 'Un numero se esistente'  1
                print("-----------------------------------------------------------\n")
            elif decisione_cerca == 2 :
                #Positioni 'Se esistente,e volte pres.' 2
                print("-----------------------------------------------------------\n")


            elif decisione_cerca == 3 :
                # Cerca Pari  
                print("-----------------------------------------------------------\n")
            elif decisione_cerca == 4 :
                #Cerca Dispari 
                print("-----------------------------------------------------------\n")

            elif decisione_cerca == 5 :
                # Minimo 
                print("-----------------------------------------------------------\n")

            elif decisione_cerca == 6 :
                #  Massimo  
                print("-----------------------------------------------------------\n")
            decisione_cerca = info_cerca_4_optioni()
        #cerca------------------------------------------------------------------------------------------
#444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
