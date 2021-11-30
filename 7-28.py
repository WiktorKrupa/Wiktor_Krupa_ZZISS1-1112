import re
file = open('grades.txt','r')
t = file.read()
v=re.findall(r"(\d.\d)",t)
s=0
for num in v:
    s+=int(num[0])
    s+=int(num[len(num)-1])*0.1
print(s/len(v))

file.close()
