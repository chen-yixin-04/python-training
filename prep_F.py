def primo(n):
    for x in range(2,n):
        check=int(n/x)
        if check * x != n: return("primo")
    return("non primo")

z=int(input("inserisci numero: "))
y=primo(z)
print(y)
