thislist = ["apple", "banana", "cherry"]
print(thislist)
#Riempi due variabili (x e y) con dei valori. Se x è maggiore di y stampa “ciao”. Se x è minore o uguale a y stampa “arrivederci”
x = 5
y = 10
if x>y:
    print("ciao")
else:
    print("arrivederci")

#Riempi tre variabili (x, y ,z) con dei valori. 
#Se x è maggiore di y e maggiore di z stampa ‘X è il numero maggiore’
n1=3
n2=6
n3=2
if n1>n2 and n1>n3:
 print("n1 è il numero maggiore")
else: 
    print("null")

#Rifai l’esercizio C stampando il nome della variabile con il valore maggiore
n1=3
n2=6
n3=2
if n1>n2 and n1>n3:
 print(n1)
elif n2>n1 and n2>n3:
    print(n2)
else:
    print(n3)

#Crea due vettori uno con il nome di città e uno con il nome di persone.
#Stampa usando dei cicli for per ogni città tutti i nomi degli abitanti
citta=["torino", "milano" ] 
abitanti= ["gino", "lino"]
for x in citta:
 for y in abitanti:
    print(x,y)



