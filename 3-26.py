a = '0805'
c = 0
while (c<3):
    b=input ('Enter the PIN code: ')
    if (b==a):
        c=4
        print ('Correct')
    else:
        c+=1
        print ('Incorrect...')
if (c==3):
    print ('Sorry, your payment card has been blocked.')