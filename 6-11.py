def compare(array1, array2):
    if len(array1)!=len(array2): return False
    else:
        for i in range(0,len(array1)):
            if array1[i]!=array2[i]: return False
    return True
a= ['water','book','sky']
a1= ['water','book','sky']
b=[True,False]
b1=[True,False,True]
c=[5,3,1]
c1=[5,3,1]
d=[3,2,1]
d1=[3,2]
print (compare(d,d1))