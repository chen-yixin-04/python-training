#Controlla se il numero 5 è un numero intero:
x = isinstance(5, int)
#La isinstance()funzione restituisce Truese l'oggetto specificato è del tipo specificato, altrimenti False.
#Se il parametro di tipo è una tupla, questa funzione restituirà Truese l'oggetto è uno dei tipi nella tupla.
#isinstance(object, type)
#object	= Required, An object.
#type =A type or a class, or a tuple of types and/or classes

#Verifica se "Hello" è uno dei tipi descritti nel parametro type:
x = isinstance("Hello", (float, int, str, list, dict, tuple))

#Controlla se y è un'istanza di myObj:
class myObj:
  name = "John"
y = myObj()
x = isinstance(y, myObj)
