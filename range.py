def range (a,x,y):
    if (x>y):
        b=(a>y and a<x)
    elif (y>x):
         b=(a>x and a<y)
    else:
        b=(a==x)
    return b