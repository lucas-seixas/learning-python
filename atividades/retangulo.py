largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

aux_um = 0
while aux_um < altura:
    aux_dois = 0
    while aux_dois < largura:
        print("#", end="")
        aux_dois += 1
    print()
    aux_um += 1
