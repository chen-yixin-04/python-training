# Un ciclo for viene utilizzato per l'iterazione su una sequenza (che può essere una lista, una tupla, un dizionario, un set o una stringa).
# Questo è meno simile alla parola chiave for in altri linguaggi di programmazione e funziona più come un metodo iteratore che si trova in altri linguaggi di programmazione orientati agli oggetti.
# Con il ciclo for possiamo eseguire un insieme di istruzioni, una volta per ogni elemento in una lista, tupla, set ecc.

# Stampa ogni frutto in una lista di frutti:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#Il ciclo for non richiede una variabile di indicizzazione da impostare in anticipo.
#Anche le stringhe sono oggetti iterabili, contengono una sequenza di caratteri:
#Scorri le lettere nella parola "banana":
for x in "banana":
  print(x)

#Con l' istruzione break possiamo interrompere il ciclo prima che abbia eseguito il ciclo di tutti gli elementi:
#Esci dal ciclo quando xè "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#Esci dal ciclo quando xè "banana", ma questa volta la pausa viene prima della stampa:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# Con l' istruzione continue possiamo interrompere l'iterazione corrente del ciclo e continuare con la successiva:
#Non stampare banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Per scorrere un insieme di codice un determinato numero di volte, possiamo usare la funzione range() ,
#La funzione range() restituisce una sequenza di numeri, a partire da 0 per impostazione predefinita, e incrementa di 1 (per impostazione predefinita) e termina con un numero specificato
#Usando la funzione range():

for x in range(6):
  print(x)

#La funzione range() è impostata su 0 come valore iniziale, tuttavia è possibile specificare il valore iniziale aggiungendo un parametro: range(2, 6) , che significa valori da 2 a 6 (ma escluso 6):
for x in range(2, 6):
  print(x)

#La funzione range() per impostazione predefinita incrementa la sequenza di 1, tuttavia è possibile specificare il valore di incremento aggiungendo un terzo parametro: range(2, 30, 3 ) :
#Incrementa la sequenza di 3 (il valore predefinito è 1):

for x in range(2, 30, 3):
  print(x)

#La elseparola chiave in un forciclo specifica un blocco di codice da eseguire al termine del ciclo:
#Stampa tutti i numeri da 0 a 5 e stampa un messaggio quando il ciclo è terminato:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Nota: il elseblocco NON verrà eseguito se il ciclo viene interrotto da breakun'istruzione.

#Interrompi il ciclo quando x è 3 e guarda cosa succede con il elseblocco:

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#Un ciclo annidato è un ciclo all'interno di un ciclo.
#Il "ciclo interno" verrà eseguito una volta per ogni iterazione del "ciclo esterno":
#Stampa ogni aggettivo per ogni frutto:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#fori loop non possono essere vuoti, ma se per qualche motivo hai un forloop senza contenuto, inserisci l' passistruzione per evitare di ricevere un errore.
#Esempio
for x in [0, 1, 2]:
  pass