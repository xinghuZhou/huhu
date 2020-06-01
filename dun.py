def use(s):
                def wrappe(*args,**kwargs):
                                logging(s)
                                return s(*args,**kwargs)
                return wrappe
def logging(s):
                print("%s is run"%s.__name__)
@use
def dun(x,y):
                print(x+y)
#dun=use(dun)
dun(2,3)
