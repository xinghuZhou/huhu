def fun4(**kwargs):
                print(kwargs)
                for key in kwargs:
                                print("%s的成绩是：%d"%(key,kwargs[key]))
fun4(zhangsan=33,li=44)
