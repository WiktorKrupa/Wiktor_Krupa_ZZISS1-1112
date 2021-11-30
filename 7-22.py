file=open("722.txt",'w')
for i in range (1,11):
    file.write(str(i)+','+str(i*i)
               +','+str(i*i*i)+'\n')
file.close()
    