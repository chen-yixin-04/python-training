# Gli elenchi vengono utilizzati per memorizzare più elementi in una singola variabile.
# Gli elenchi sono uno dei 4 tipi di dati integrati in Python utilizzati per archiviare raccolte di dati, gli altri 3 sono Tuple , Set e Dictionary , tutti con qualità e utilizzo diversi.
# Gli elenchi vengono creati utilizzando parentesi quadre
# L'elenco è modificabile, il che significa che possiamo modificare, aggiungere e rimuovere elementi in un elenco dopo che è stato creato
# Le voci dell'elenco sono ordinate, modificabili e consentono valori duplicati.
# Gli elementi dell'elenco sono indicizzati, il primo elemento ha index [0], il secondo elemento ha index [1]ecc.
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Quando diciamo che le liste sono ordinate, significa che gli articoli hanno un ordine definito e quell'ordine non cambierà.
# Se aggiungi nuovi elementi a un elenco, i nuovi elementi verranno inseriti alla fine dell'elenco.

# Gli elenchi consentono valori duplicati:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#Per determinare quanti elementi ha un elenco, utilizzare la len()funzione:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# Gli elementi dell'elenco possono essere di qualsiasi tipo di dati:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1,list2,list3)

# Un elenco può contenere diversi tipi di dati
list1 = ["abc", 34, True, 40, "male"]

# Dal punto di vista di Python, le liste sono definite come oggetti con il tipo di dati 'list'
#Qual è il tipo di dati di un elenco? <class 'list'>
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# È anche possibile utilizzare il costruttore list() durante la creazione di una nuova lista. È il modo alternativo per scrivere thislist = ["apple", "banana", "cherry"]
# esempio: utilizzando il list()costruttore per creare un elenco:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Esistono quattro tipi di dati di raccolta nel linguaggio di programmazione Python:
# List è una collezione ordinata e modificabile. Consente membri duplicati.
# Tuple è una collezione ordinata e immutabile. Consente membri duplicati.
# Set è una raccolta non ordinata, non modificabile e non indicizzata. Nessun membro duplicato. Gli elementi impostati non sono modificabili, ma puoi rimuovere e/o aggiungere elementi quando vuoi.
#  dizionario è una raccolta ordinata e modificabile. Nessun membro duplicato.