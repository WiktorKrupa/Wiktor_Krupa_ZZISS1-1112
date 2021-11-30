a= input('Podaj nazwę pliku: ')
f = open(a,'r')
s=0
for line in f:
    s+=1
print (f"file name: {a}")
print (f"Number of lines: {s}")
    