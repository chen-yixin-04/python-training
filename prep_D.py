#Chiedi all’utente quanti numeri vuole inserire. Leggi tutti i numeri in input.
#Stampa tutti i numeri inseriti al quadrato

lista=[]
quadrato=[]
y=int(input("quanti numeri vuoi inserire? "))
for x in range(y):
  z=int(input("inserisci numero "+str(x+1)+": "))
  lista.append(z)
  q=z*z
  quadrato.append(q)
print(lista,quadrato)
print("..................................................................")

funzione = int(input("quanti numeri vuoi inserire: "))
list = []
for x in range(funzione):
    y = int(input("numero da inserire: "))
    print(pow(y,2))