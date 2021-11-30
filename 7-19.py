dest = open('shoppinglist.txt','a')
src1 = open('MeatAndFish.txt','r')
src2 = open('GrainsAndBread.txt','r')
for line in src1:
    dest.write(line)
for line in src2:
    dest.write(line)
dest.close()
src1.close()
src2.close()
