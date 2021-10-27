a=input ('a: ')
b=input ('b: ')
a=int(a)
b=int(b)
q=a-2
w=b-2
for i in range (0,b):
    print ('*',end='')
for i in range (0,q):
    print ('*',end='')
    for j in range (0,w):
        print ('',end='')
    print ('*',end='')