#!/usr/bin/python3

spesa = ['pasta integrale corta','pasta integrale lunga','pastina integrale',
'riso integrale per risotti','riso integrale per insalate','cereali in chicchi (orzo decorticato',
'farro decorticato','grano saraceno','legumi secchi','legumi cotti in barattolo di vetro',
'frutta secca (mandorle, noci, pistacchi, anacardi)','tonno e sgombro in barattolo di vetro',
'pelati o polpa di pomodoro','sotto aceti','biscotti integrali e senza zucchero',
'fette biscottate integrali e senza zucchero','gallette integrali','crackers integrali',
'pan bauletto integrale','latte a lunga conservazione (vaccino, di capra o vegetale)','caffe','miele',
'the, tisane, camomilla','cacao in polvere','marmellata senza zucchero','crema spalmabile (es. 100% nocciole)',
'lievito secco','sale marino integrale fino','sale marino integrale grosso',
'capperi','olive','pangrattato integrale','farina integrale','farina di cocco','farina di mandorle',
'pepe nero', 'peperoncino', 'cannella', 'noce moscata', 'curry', 'origano', 'zafferano', 'paprika',
'preparato per brodo vegetale','olio extra vergine oliva','aceto di mele','aceto balsamico','pesto','bicarbonato']

i=0
dimensione = len(spesa)
while True:
    print(i,spesa[i])
    i = i + 1
    if(i == dimensione):
        break