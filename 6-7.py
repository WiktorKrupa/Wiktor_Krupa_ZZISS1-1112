tablica = [1,2,3]
p=0
np=0
for i in range (0,len(tablica)):
    if tablica[i]%2==0: p+=1
    else: np+=1
print (f"parzyste={p}")
print (f"nieparzyste={np}")