def primo(n):
    aux = 2
    while n%aux !=0:
        aux+=1
    
    if n==aux:
        return "primo"
    else:
        return "não primo"

def maior_primo(n):
    while primo(n) == "não primo":
        n-=1
    return n
