# Uguale a: a == b
# Diverso da: a != b
# Minore di: a < b
# Minore o uguale a: a <= b
# Maggiore di: a > b
# Maggiore o uguale a: a >= b
# Queste condizioni possono essere utilizzate in diversi modi, più comunemente in "istruzioni if" e cicli.
a = 33
b = 200
if b > a:
  print("b è maggiore di a")

# La parola chiave elif è un modo Python per dire "se le condizioni precedenti non erano vere, prova questa condizione".
a = 33
b = 33
if b > a:
  print("b è maggiore di a")
elif a == b:
  print("a e b sono uguali")
# In questo esempio a è uguale a b , quindi la prima condizione non è vera, ma la condizione elif è vera, quindi stampiamo sullo schermo che "a e b sono uguali".

#La parola chiave else cattura tutto ciò che non è catturato dalle condizioni precedenti.
a = 200
b = 33
if b > a:
  print("b è maggiore di a")
elif a == b:
  print("a e b sono uguali")
else:
  print("a è maggiore di b")

#In questo esempio a è maggiore di b , quindi la prima condizione non è vera, anche la condizione elif non è vera, quindi andiamo alla condizione else e stampiamo sullo schermo che "a è maggiore di b".

#Puoi anche avere un elsesenza elif:
a = 200
b = 33
if b > a:
 print("b è maggiore di a")
else:
 print("b non è maggiore di a")

#Se hai solo un'istruzione da eseguire, puoi metterla sulla stessa riga dell'istruzione if.
 if a > b: print("b è maggiore di a")

#Se hai una sola istruzione da eseguire, una per se e una per l'altra, puoi metterla tutta sulla stessa riga:
a = 2
b = 330
print("A") if a > b else print("B")

#La parola chiave and è un operatore logico e viene utilizzata per combinare istruzioni condizionali:
#Verifica se aè maggiore di b, E se c è maggiore di a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#La orparola chiave è un operatore logico e viene utilizzata per combinare istruzioni condizionali:
#Verifica se aè maggiore di b, OPPURE se a è maggiore di c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#Puoi avere ifistruzioni all'interno ifdi istruzioni, questo è chiamato istruzioni nidificate if
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#ifle istruzioni non possono essere vuote, ma se per qualche motivo hai una ifdichiarazione senza contenuto, inseriscila passper evitare di ottenere un errore.
a = 33
b = 200
if b > a:
  pass