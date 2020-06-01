def LenthPan():
    T = ()
    print("请输入一个元组：")
    T = tuple(input())
    print("输入的元组为：{}".format(T))
    print("元组的个数为：{}".format(len(T)))
    print ('是否大于5：{}'.format(len(T)>5))
LenthPan()
