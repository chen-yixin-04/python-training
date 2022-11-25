#Chiedi all’utente di inserire 5 numeri e stampa i numeri in ordine inverso


numeri = []
for x in range(5):
    n = int(input("inserisci numero" + str(x+1) + ": "))
    numeri.append(n)
print(numeri)
numeri.reverse()
print(numeri)