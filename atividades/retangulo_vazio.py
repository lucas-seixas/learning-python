largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

aux_altura = 1

while aux_altura <= altura:
    aux_largura = 1
    
    if aux_altura == 1 or aux_altura == altura:
        while aux_largura <= largura:
            print("#", end="")
            aux_largura += 1
    else:
        while aux_largura <= largura:
                if aux_largura == 1 or aux_largura == largura:
                    print("#", end="")
                else:
                    print(" ", end="")
                aux_largura += 1 

    print()
    aux_altura += 1
