def primo(n):
    aux = 2
    while n%aux !=0:
        aux+=1
    
    if n==aux:
        return "primo"
    else:
        return "não primo"

def n_primos(n):
    if n < 2:
        print("Entrada incorreta.")
    else:
        quantidade_de_primos = 0
        while n > 1:
            if primo(n) == "primo":
                quantidade_de_primos += 1
            n-=1
            
    return quantidade_de_primos
