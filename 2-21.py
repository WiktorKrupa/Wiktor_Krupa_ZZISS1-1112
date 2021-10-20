import random
a=random.randint(1,6)
a%=6
a+=1
b=random.randint(1,6)
b%=6
b+=1
c=random.randint(1,6)
c%=6
c+=1
s=a+b+c
print (f'liczby to : {a}, {b}, {c}.  Ich suma to {s}')