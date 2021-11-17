a=['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
mxl=0
l=0
for i in range (0,len(a)):
    if len(a[i])>l:
        mxl = i
        l=len(a[i])
print (a[mxl])