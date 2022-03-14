n = int(input("Digite um número inteiro: "))
i="não"
while n//10!=0:
    if n%10==n//10%10:
        i="sim"       
    n = n//10
print(i)
