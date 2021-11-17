def bubblesort(array):
   c=[]
   for i in range (0, len(array)):
        a=0
        for j in range (0,len (array)):
            if (i!=j and array[i]==array[j]):
                a+=1
        if (a==0):
            c+=str(array[i])
   return c
b=[2,3,2,5,8,1,9,8]
print (bubblesort(b))
