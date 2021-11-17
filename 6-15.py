f = open("6-15.txt","w")
a=["Czerwony", "Zielony", "Pomaranczowy",
   "Niebieski", "Różowy"]
for i in range (0, len(a)):
    f.write(a[i]+'\n')
f.close()