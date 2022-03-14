def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    p=0
    while p!="1" and p!="2":
        print("1 - para jogar uma partida isolada")
        p = input("2 - para jogar um campeonato ")
        print()
        if p!="1" and p!="2":
            print("Oops! Entrada inválida! Tente de novo.")
            print()
    if p=="1":
        print("Voce escolheu uma partida isolada!")
        partida()
    elif p=="2":
        print("Voce escolheu um campeonato!")
        campeonato()


def usuario_escolhe_jogada(n,m):
    aux = 0
    while aux > m or aux < 1:
        print()
        aux = int(input("Quantas peças você vai tirar? "))
        if aux > m or aux < 1:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
    if aux==1:
        print("Você tirou uma peça.")
    else:
        print("Você tirou",aux,"peças.")
    return aux


def computador_escolhe_jogada(n,m):
    aux = m
    teste = n
    x = 0
    while teste%(m+1) != 0 and x == 0 and aux != n:
        teste = n
        aux -= 1
        teste -= aux
        if aux == 0:
            aux = m
            x = 1  
    if aux==1:
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou",aux,"peças.")    
    return aux


def partida():
    print()
    n=0
    m=0
    while n<1:
        n = int(input('Quantas peças? '))
        if n < 1:
            print("Entrada incorreta. A quantidade de peças não pode ser menor do que uma.")
            print()
    while m<1:
        m = int(input('Limite de peças por jogada? '))
        if m < 1:
            print("Entrada incorreta. O limite de peças por jogada não pode ser menor do que um.")
            print()
    aux = 0
    if n%(m+1) == 0:
        print()
        print("Voce começa!")
        while n!=0:
            print()
            aux = usuario_escolhe_jogada(n,m)
            n -= aux
            if n==1:
                print("Agora resta apenas uma peça no tabuleiro.")
            elif n==0:
                print("Fim do jogo! O usuário ganhou!")
                vencedor = "usuario"
            else:
                print("Agora restam",n,"peças no tabuleiro.")          
            if n!=0:
                print()
                aux = computador_escolhe_jogada(n,m)
                n -= aux
                if n==1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                elif n==0:
                    print("Fim do jogo! O computador ganhou!")
                    vencedor = "computador"
                else:
                    print("Agora restam",n,"peças no tabuleiro.") 
    else:
        print()
        print("Computador começa!")
        while n!=0:
            print()
            aux = computador_escolhe_jogada(n,m)
            n -= aux
            if n==1:
                print("Agora resta apenas uma peça no tabuleiro.")
            elif n==0:
                print("Fim do jogo! O computador ganhou!")
                vencedor = "computador"
            else:
                print("Agora restam",n,"peças no tabuleiro.")
            if n!=0:
                print()
                aux = usuario_escolhe_jogada(n,m)
                n -= aux
                if n==1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                elif n==0:
                    print("Fim do jogo! O usuário ganhou!")
                    vencedor = "usuario"
                else:
                    print("Agora restam",n,"peças no tabuleiro.")
    return vencedor


def campeonato():
    computador = 0
    usuario = 0
    n=1
    while n <4:
        print()
        print("**** Rodada",n,"****")
        vencedor = partida()
        if vencedor == "computador":
            computador += 1
        else:
            usuario += 1
        n += 1
    print()
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você",usuario,"X",computador,"Computador")


main()

