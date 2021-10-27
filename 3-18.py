a=input ('Enter the amount in PLN: ')
a=int(a)
b=int(a)
p=0
d=0
j=0
while (a>=5 and a>0):
    a-=5
    p+=1
while (a>=2 and a>0):
    a-=2
    d+=1
while (a>=1 and a>0):
    a-=1
    j+=1
print (f'The amount of PLN {b} in coins: ')
print (f'5 zł - {p}')
print (f'2 zł - {d}')
print (f'1 zł - {j}')