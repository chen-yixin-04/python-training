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