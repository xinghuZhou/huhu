mysum = 0
for x in range(10):
    mysum  += x
    print("%d"%x,end="")#end是不换行
    if x < 9:
        print("+",end="")
print("=%d"% mysum)
