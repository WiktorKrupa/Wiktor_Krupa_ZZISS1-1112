file = open('liczby.txt','w')
for i in range (1,51):
    file.write(str(i)+'\n')
file.close()