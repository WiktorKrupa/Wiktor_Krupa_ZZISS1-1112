num = [-15,8,-31,47,2,19]
mx=num[0]
mn=num[0]
for i in range (1,len(num)):
    if num[i]>mx: mx=num[i]
    if num[i]<mn: mn=num[i]
print (f"Najmniejsza liczba: {mn}")
print (f"największa liczba: {mx}")