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

def funzione(n):
 for x in range(1):
    print("*"*n)
funzione(3)
funzione(7)
funzione(9)
funzione(5)
