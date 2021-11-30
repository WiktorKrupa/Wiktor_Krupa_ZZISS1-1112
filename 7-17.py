f  = open('rickroll.txt','r')
fd = open('copy.txt','w')
for line in f:
    fd.write(line)
f.close()
fd.close()