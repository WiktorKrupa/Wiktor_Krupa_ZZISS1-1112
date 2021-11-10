def power(x,n):
    if (n==0): return 1
    elif (n>1):
        return x* power(x,n-1)
    else: return x
        