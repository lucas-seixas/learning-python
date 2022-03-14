def é_hipotenusa(n):

    i = 1
    j = 1
    temHipotenusa = False
    
    while i < n:
        j = 1
        while j < n:
            if n**2 == i**2 + j**2:
                temHipotenusa = True
            j+=1
        i+=1

    return temHipotenusa


def soma_hipotenusas(n):

    aux = 1
    soma = 0
    while aux <= n:
        if é_hipotenusa(aux) == True:
            soma = soma + aux
        aux+=1
        
    return soma
