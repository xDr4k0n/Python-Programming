#!/usr/bin/python3


def output_giorno(giorno, grandezza, ore):
    i = 0
    while i != grandezza:
        print(ora[i],giorno[i])
        i = i + 1


def info_programma():
    print("Programma che fa vedere il orario della classe!")   
    print("Usando le : Funzioni(+passa-parametri) , liste")
    print("            If , elseif(elif) , while")   
    print("Per Usare il programma devi inserire il giorno in base al")
    print("numero del giorno.")  
    print("Esempio : Per Lunedi inserisci 1.")  
    print("\n\n")  

def info_scelta():
    print("              Orario")
    print("     Giorno             Numero")
    print("Per Lunedi    , inserisci 1")
    print("Per Martedi   , inserisci 2")
    print("Per Mercoledi , inserisci 3")
    print("Per Giovedi   , inserisci 4")
    print("Per Venerdi   , inserisci 5")
    print("\n\n") 

def scelta():
    print("Inserisci la tua scelta : \n")
    scelta_numero = int(input())
    return scelta_numero



settimana = ['Lunedi', 'Martedi', 'Mercoledi', 'Giovedi','Venerdi']
lunedi = ['Telecomunicazioni', 'Telecomunicazioni', 'Matematica', 'Sistemi']
martedi = ['Informatica','Technologie e reti','Sistemi e Reti','Storia']
mercoledi = ['Matematica','Matematica','Informatica','Informatica','Storia']
giovedi = ['Italiano','Informatica','Informatica','Inglese','Sistemi']
venerdi = ['Italiano','Italiano','Technologie e reti','Technologie e reti','Inglese']
ora = ['1 (18:00)','2 (19:00)','3 (20:00)','4 (20:50)','5 (21:40)','6 (22:30)','7 (x:x)']

grandezza_lunedi = len(lunedi)
grandezza_martedi = len(martedi)
grandezza_mercoledi = len(mercoledi)
grandezza_giovedi = len(giovedi)
grandezza_venerdi = len(venerdi)

#output_giorno(lunedi , grandezza_lunedi, ora)

info_programma()
info_scelta()
risposta = scelta()
#test
#print("risposta :", risposta)

if risposta == 1:
    print("Lunedi :")
    output_giorno(lunedi , grandezza_lunedi, ora)
elif risposta == 2:
    print("Martedi :")
    output_giorno(martedi , grandezza_martedi, ora)
elif risposta == 3:
    print("Mercoledi :")
    output_giorno(mercoledi , grandezza_mercoledi, ora)
elif risposta == 4:
    print("Giovedi :")
    output_giorno(giovedi , grandezza_giovedi, ora)
elif risposta == 5:
    print("Venerdi :")
    output_giorno(venerdi , grandezza_venerdi, ora)
else:
    print("Hai inserito una risposta eronata!")


