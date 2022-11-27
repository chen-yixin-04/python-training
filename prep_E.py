#Definisci una funzione chiamata ‘primo’ che riceva come parametro un numero intero
# e ritorni true in caso il numero fosse primo

def primo(n):
    for x in range(2,n):
        check=int(n/x)
        if check * x == n: return False
    return True
n=7
z=primo(n)
print(n,z)
print("..................................................................")

#Chiedi all’utente di inserire un numero. Stampa “primo” nel caso si tratti di un numero primo.
def primo(n):
    for x in range(2,n):
        check=int(n/x)
        if check * x != n: return("primo")
        else: return ("non primo")
z=int(input("inserisci numero: "))
y=primo(z)
print(y)


