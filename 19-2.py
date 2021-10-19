
a= input ('pierwszy bok: ')
b= input ('drugi bok: ')
c= input ('trzeci bok: ')
o=(int(a)+int(b)+int(c))/2
p=(o*(o-int(a))*(o-int(b))*(o-int(c)))**(1/2)
print (p)