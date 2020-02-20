#!/usr/bin/python3

messaggio = "Ciao, sono Matrix! \n"

print(messaggio*20)
carattere = 'M'
if carattere in messaggio:
    print("La lettera m esiste nella stringa")


lettere = ['M','a','t','r','i','x']
print(lettere*20)

if carattere in lettere:
    print("La lettera m esiste nella lista")


for x in lettere:
    print("lettera")

parole = ['uno', 'due', 'tre']
print(parole[1])
print(parole[-1])
print(parole[1:])

print (max(parole))
print (min(parole))

