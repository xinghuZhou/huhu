def sum(*args):
                s=0
                for x in args:
                                s=s+x
                return s#若返回语句与s位置一样，则智能返回1
re = sum(1,2,5)
print(re)
