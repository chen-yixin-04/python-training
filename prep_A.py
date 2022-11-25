#Chiedi all’utente di inserire 5 numeri e stampa i numeri man mano che vengono inseriti

for x in range(5):
    n=int(input("inserisci numero"+" "+str(x+1)+" : "))
    print(n)