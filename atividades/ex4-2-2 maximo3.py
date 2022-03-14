def maximo(a,b,c):
    if a>=b and a>=c:
        return a
    if c>=a and c>=b:
        return c
    if b>=a and b>=c:
        return b
