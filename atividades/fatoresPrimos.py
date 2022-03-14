n = int(input("Digite um número inteiro maior que 1 para fatorarmos: "))

fator = 2


while n >1:
    multiplicidade = 0
    while n % fator == 0:
        multiplicidade += 1
        n = n/fator
    if multiplicidade > 0:
        print ("fator",fator, "multiplicidade =",multiplicidade)
    fator += 1
 
