def fatorial(n):
    nfat = 1
    while not n==0:
        nfat = nfat*n
        n = n-1
    return nfat

print("Digite uma sequência de números para ser impresso o fatorial deles.")

qtidade = int(input("Quantos números vai querer? "))
aux = 1
while aux <= qtidade:
    print("Esse é o ",aux," de ",qtidade,": ")
    numero = int(input("Digite o número que quer saber o fatorial: "))
    fat = fatorial(numero)
    
    print("O fatorial de",numero,"é",fat)
    aux += 1
