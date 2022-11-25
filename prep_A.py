#Chiedi all’utente di inserire 5 numeri e stampa i numeri man mano che vengono inseriti

#for x in range(5):
#    n=int(input("inserisci numero"+" "+str(x+1)+" : "))
#    print(n)
#print("..................................................................")

#Chiedi all’utente di inserire 5 numeri e stampa i numeri in ordine inverso
#numeri = []
#for z in range(5):
#    num = int(input("inserisci numero"+" "+str(x+1)+" : "))
#    numeri.append(num)
#print(numeri)
#numeri.reverse()
#print(numeri)
#print("..................................................................")

#Chiedi all’utente di inserire 5 numeri e stampa solo i numeri pari in ordine inverso

lista = []
for y in range(5):
  l = int(input("inserisci numero"+" "+str(y+1)+" : "))
  check = int(l/2)
  if (check*2)== l:
    lista.append(l)
print(lista)
lista.reverse()
print(lista)



 