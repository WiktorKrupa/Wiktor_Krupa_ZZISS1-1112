a=[4,36,12,28,9,44,5]
b=[5,1,36]
for i in range (0,len(a)):
    t=0
    for j in range (0,len(b)):
        if (a[i]==b[j]): t+=1
    if (t==0): print (a[i])