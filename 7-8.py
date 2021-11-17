file= open('countries.txt','r')
i=1
for line in file:
    print (f'{i}: ',end='')
    i+=1
    print (line, end='')
   

file.close()