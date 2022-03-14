def fatorial(n):
    nfat = 1
    while not n==0:
        nfat = nfat*n
        n = n-1
    return nfat

def  binomionewton(n, k):
    return fatorial(n)/(fatorial(k)*(fatorial(n-k)))
 
