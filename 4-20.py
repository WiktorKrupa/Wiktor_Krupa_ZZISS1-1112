def power(x,n):
    if (n>0):
        return x* power(x,n-1)
    else: return x
        