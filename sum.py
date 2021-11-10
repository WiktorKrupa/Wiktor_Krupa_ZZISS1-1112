def fib(n):
    s=''
    a=0
    b=1
    c=0
    for i in range(0,n):
        s+=str(a)
        c=b
        b=a
        a=b+c
        s+=' '
    return s
print (fib(5),)