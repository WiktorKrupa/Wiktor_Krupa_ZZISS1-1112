def star(n):
    for i in range (0, n):
        print ('*', end='')
       
a= [12,6,4,9,10]
for i in range (0, len(a)):
    if a[i]<10: print (' ',end='')
    print (f"{a[i]}:",end=' ')
    star(a[i])
    print ('')