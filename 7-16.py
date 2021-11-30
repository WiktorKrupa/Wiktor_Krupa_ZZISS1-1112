f = open("rickroll.txt",'r')
limit=0
i=0
tab=[]
for line in f:
    limit+=1
    tab.append(line)
    i+=1
counter=5
for j in range (0,5):
    print (tab[j])
while (counter<limit):
    a=input('')
    if (a==''):
        for j in range (counter,counter+5):
            print (tab[j])
        counter+=5
file.close()
        
    