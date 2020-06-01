class toy:
                count=0
                def __init__(self,name):
                                self.name=name
                                toy.count+=1
yi=toy("zhangsan")
er=toy("lisi")
#print("共调用了%d次"%toy.count)
toy.ower="佩佩"
er.name="wangwu"
def setPrice(self,price):
                self.price=price
#动态位实例增加方法，需要导入types模块
import types
er.setPrice=types.MethodType(setPrice,er)
er.setPrice(200)
print("现在调用了%d次"%toy.count)
print(er.name,"价格是",er.price)
