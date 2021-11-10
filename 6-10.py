def sum(array):
    a=0
    for i in array:
        a+= i
    return a
def array2str(array):
    a=''
    for i in array:
        a+=str(i)
    return a

tablica = [5,6,7,8,9]
print (sum(tablica))
print (array2str(tablica))