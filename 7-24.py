import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
s=0
for num in temperatures:
    s+=int(num)
print (s/len(temperatures))
