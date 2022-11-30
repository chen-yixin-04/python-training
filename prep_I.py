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