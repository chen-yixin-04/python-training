#Chiedi all’utente di inserire 5 numeri e stampa i numeri man mano che vengono inseriti

for x in range(5):
    n=int(input("inserisci numero"+" "+str(x+1)+" : "))
    print(n)
print("..................................................................")

#Chiedi all’utente di inserire 5 numeri e stampa i numeri in ordine inverso
numeri = []
for z in range(5):
    num = int(input("inserisci numero"+" "+str(z+1)+" : "))
    numeri.append(num)
print(numeri)
numeri.reverse()
print(numeri)
print("..................................................................")

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
print("..................................................................")

#Chiedi all’utente quanti numeri vuole inserire. 
#Leggi tutti i numeri in input. Stampa tutti i numeri inseriti al quadrato

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
print("..................................................................")

#Definisci una funzione chiamata ‘primo’ che riceva come parametro un numero intero
# e ritorni true in caso il numero fosse primo

def primo(n):
    for x in range(2,n):
        check=int(n/x)
        if check * x == n: return False
    return True
z=primo(7)
print(z)
print("..................................................................")

#Scrivi una funzione che, data una lista di numeri in input, fornisce in output un istogramma basato su questi numeri, usando asterischi per disegnarlo.
#Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:
#***
#*******
#*********
#*****

x = input("quanti numeri vuoi inserire? ")
x = int(x)
lista=[]
for y in range(x):
    z = int(input("inserisci numero: "))
    lista.append(z)
for n in lista:
    print("*"*n)
print(".....................................................")

def funzione(lista):
 for x in lista:
    print("*"*x)
lista=[3, 7, 9, 5]
funzione(lista)
print(".....................................................")
#Definisci una funzione che riceva in input un numero indefinito di parametri. 
#Stampi solo il terzo e il quarto (se esistono)

def funzione(lista):
    if l>3:
      print(lista[2],lista[3])
    else: 
        print("non esiste")
lista=[]
l=int(input("quanti numeri vuoi inserire? "))    
for x in range (l):
 n=int(input("inserisci numeri: "))
 lista.append(n)
funzione(lista)
print(".....................................................")

#Scrivi una funzione che dato in input un numero h e un carattere c stampi un albero di natale fatto di caratteri di altezza h
#es:            *
#              ***
 #            *****
#Per h = 3, e c= *

def albero(h,c):
    asterischi=1
    spazi=h-1

    for x in range(0,h):
        print(spazi*" ", asterischi*char)
        asterischi=asterischi +2
        spazi=spazi -1

altezza=int(input("dammi un altezza: "))
char=input("dammi un carattere: ")
albero(altezza,char)