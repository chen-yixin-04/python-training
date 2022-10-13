# assegno un valore alle variabili, che si creano nel momento stesso
x = 4
y = "John"
print(x)
print(y)

# non devo dichiarare le variabilli con nessun tipo particolare, e posso cambiarli anche dopo che sono state impostate.
x = 4       
x = "Sally" 
print(x)

# con il casting posso specificare il tipo di dati di una variabile
# x sarà '3'
# y sarà 3
# z sarà 3.0
x = str(3)    
y = int(3)    
z = float(3)  

# è possibile ottenere il tipo di dati di una variabile con la type()funzione
x = 5
y = "John"
print(type(x))
print(type(y))

# le variabili stringa possono essere dichiarate utilizzando virgolette singole o doppie
x = "John"
x = 'John'

# i nomi delle variabili fanno distinzione tra maiuscole e minuscole
a = 4
A = "Sally"