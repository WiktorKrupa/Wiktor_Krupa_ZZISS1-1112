a=input ("Enter the dog's age in human years: ")

b=0
for i in range (int(a),0,-1):
    if (i>2):b+=4
    else: b+=10.5
    
print(f"The dog's age in dog’s years is {b} years.") 
