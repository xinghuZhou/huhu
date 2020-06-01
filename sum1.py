a = eval(input("请输入第一个整数："))
b = eval(input("请输入第二个整数："))
def num():
    sum = 0
    for s in range(a,b):
        if s%2 == 0:
            pass
        else:
            sum=sum+s
    print("sum=%d" % sum)
num()
