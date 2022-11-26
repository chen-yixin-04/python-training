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

#Chiedi all’utente di inserire 5 numeri e stampa solo i numeri pari in ordine inverso e contali

#lista = []
#count=0
#for y in range(5):
#  l = int(input("inserisci numero"+" "+str(y+1)+" : "))
#  check = int(l/2)
 # if (check*2)== l:
 #   lista.append(l)
 #   count=count+1
#print(lista)
#lista.reverse()
#print(lista,count)

#Chiedi all’utente quanti numeri vuole inserire. 
#Leggi tutti i numeri in input. Stampa tutti i numeri inseriti al quadrato

#lista=[]
#quadrato=[]
#y=int(input("quanti numeri vuoi inserire? "))
#for x in range(y):
 # z=int(input("inserisci numero "+str(x+1)+": "))
  #lista.append(z)
 # q=z*z
  #quadrato.append(q)
#print(lista,quadrato)


def primo(n):
  for x in range(2,n):
    n = int(input("inserisci numero"))
    x=primo(n)
    check=int(n/x)
    if check*x!=n: 
      print("primo")




 