def primo():
 n=int(input("Inserisci un numero naturale n maggiore di 1: "))
 primo=True # ipotizziamo che N sia primo
 for i in range(2,n): # test di divisibilità
  if n%i==0:return False
 if primo: return False
 else: return False
primo()
