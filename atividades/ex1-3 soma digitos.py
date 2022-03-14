n = int(input("Digite um número inteiro: "))

resultado = 0

while n!=0:
    resultado = resultado + n%10
    n = n//10

print(resultado)
