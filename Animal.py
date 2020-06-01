class Animal:
                def eat(self):
                                print("吃==")
                def drink(self):
                                print("喝==")
class Dogs(Animal):
                def bark(self):
                                print("汪汪")
class Tian(Dogs):
                def fly(self):
                                print("他会飞")
                def bark(self):
                                print("神一样的节能")
                super( ).bark( )
                print("lalal")
gou=Tian()
gou.bark()
