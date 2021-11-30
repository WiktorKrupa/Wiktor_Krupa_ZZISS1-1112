import re
file = open("rickroll.txt.",'r')
tekst = file.read()
v = re.findall(r"[a-zA-Z]{6}[a-zA-Z]*",tekst)
for str in v:
    print (str+'\n')
file.close()

