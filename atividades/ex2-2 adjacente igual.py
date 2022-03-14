n = int(input("Digite um número inteiro: "))
i=0
while n//10!=0:
    if n%10==n//10%10:
        i=1
        
    n = n//10
    
if i==1:
    print("sim")
else:
    print("não")
