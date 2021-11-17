def bubblesort(array):
    a=0
    for i in range (0, len(array)):
        for j in range (0,len (array)):
            if (array[i]<array[j]):
                a= array[i]
                array[i]=array[j]
                array[j]=a
    return array
b=[11,22,44,3,2,6,4,5,88,9,100,0]
print (bubblesort(b))