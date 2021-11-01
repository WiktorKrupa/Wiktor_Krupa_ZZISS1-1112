#GAME:)
import mymath
a=mymath.read_number()
b=mymath.generate_number()
print(f"your number: {a},4 correct number: {b} ")

if a==b:
    print ('you won')
else:
    print ('you lose')
