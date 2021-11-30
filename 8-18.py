stack=[]
a= input('give number: ')
a=int(a)
b=''
while (a>0):
    stack.append(a%2)
    a//=2
while (len(stack)>0):
    b+=str(stack.pop())
print (b)