n = int(input("Digite um número inteiro: "))

aux = 2

while n%aux !=0:
    aux=aux+1
    
if n==aux:
    print("primo")
else:
    print("não primo")
