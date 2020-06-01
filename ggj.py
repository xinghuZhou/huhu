def use(co):
                def decro(s):
                                def wrapper(*args,**kwargs):
                                                if co=='y':
                                                                logging(s)
                                                return s(*args,**kwargs)
                                return wrapper
                return decro
def logging(s):
                print("%s is run"%s.__name__)
@use('y')
def fun(x,y):
                print(x+y)
fun(2,3)
