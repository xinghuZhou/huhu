product = 0
for i in range(1,10):
    for j in range(1,i+1):
        product = i * j
        print("%d*%d=%d"%(i,j,product),end="\t")#\t横向制表符
    print()
