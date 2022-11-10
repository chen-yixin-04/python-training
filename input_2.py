#Una funzione è un blocco di codice che viene eseguito solo quando viene chiamata.
#È possibile passare dati, noti come parametri, in una funzione.
#Una funzione può restituire dati come risultato.

#In Python una funzione è definita usando la parola chiave def :
#Per chiamare una funzione, utilizzare il nome della funzione seguito da parentesi:
def my_function():
  print("Hello from a function")

my_function()

#Le informazioni possono essere passate in funzioni come argomenti.
#Puoi aggiungere tutti gli argomenti che vuoi, separandoli semplicemente con una virgola.
def my_function(funzione):
  print(funzione + " Galvani")

my_function("scientifico")
my_function("linguistico")
my_function("informatico")

#Per impostazione predefinita, una funzione deve essere chiamata con il numero corretto di argomenti. 
#Ciò significa che se la tua funzione prevede 2 argomenti, devi chiamare la funzione con 2 argomenti, non di più e non di meno.

#Questa funzione prevede 2 argomenti e ottiene 2 argomenti:

def my_function(nome, cognome):
  print(nome + " " + cognome)

my_function("Yixin", "Chen")

#Se provi a chiamare la funzione con 1 o 3 argomenti, otterrai un errore:
#Questa funzione prevede 2 argomenti, ma ne ottiene solo 1:

#def my_function(nome, cognome):
  #print(nome + " " + cognome)

#my_function("Chen")

#Se non sai quanti argomenti verranno passati nella tua funzione, aggiungi a *prima del nome del parametro nella definizione della funzione.
#In questo modo la funzione riceverà una tupla di argomenti e potrà accedere agli elementi di conseguenza:
def my_function(*materia):
  print("Il voto più alto è di " + materia[2])

my_function("matematica", "scienze", "fisica")

#Puoi anche inviare argomenti con la sintassi chiave = valore .
#In questo modo l'ordine degli argomenti non ha importanza.
def my_function(materia1, materia2, materia3):
  print("Il voto più alto è di " + materia2)

my_function(materia1 = "matematica", materia2 = "scienze", materia3 = "fisica")

#Se il numero di argomenti della parola chiave è sconosciuto, aggiungi un double **prima del nome del parametro:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")