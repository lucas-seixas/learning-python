def primo(n):
    aux = 2
    while n%aux !=0:
        aux=aux+1
    return aux

n = int(input("Digite um número inteiro: "))
    
if n==primo(n):
    print("primo")
else:
    print("não primo")
