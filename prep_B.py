#Chiedi all’utente di inserire 5 numeri e stampa i numeri in ordine inverso


numeri = []
for z in range(5):
    numero = int(input("inserisci numero" + str(z+1) + ": "))
    numeri.append(numero)

print(numeri)
print(numeri.reverse())