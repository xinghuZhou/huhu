class Ahuang():
                def __init__(self,fun):
                                self.fun=fun
                def __call___(self,*args,**kwargs):
                                print('funtion {fun}() is run '.format(fun=self.fun.__name__))
                                return self.fun(*args,**kwargs)
                
@Ahuang
def dun():
                print('dun is runi')
dun()
