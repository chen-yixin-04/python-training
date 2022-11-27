#Chiedi all’utente di inserire 5 numeri e stampa solo i numeri pari in ordine inverso e contali

lista = []
count=0
for y in range(5):
  l = int(input("inserisci numero"+" "+str(y+1)+" : "))
  check = int(l/2)
  if (check*2)== l:
    lista.append(l)
    count=count+1
print(lista)
lista.reverse()
print(lista,count)