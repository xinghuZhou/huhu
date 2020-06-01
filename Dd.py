class Dd:
                def __init__(self,name):
                                print('初始化方法')
                                self.name=name
                def eat(self):
                                print("%s爱吃骨头汤"%self.name)

tom=Dd('tom')
tom.eat()
jack=Dd('jack')
jack.eat()
