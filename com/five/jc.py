#继承
class Animal():
    def eat(self):
        print("好吃")
    def drink(self):
        print("好喝")
    def __haode(self):
        print("私有")
class Dog(Animal):
    def tiao(self):
        print("tiao")
dog=Dog();
dog.eat();
dog.tiao();

class Cat(object):

    def __init__(self, name, color="白色"):
        self.name = name
        self.color = color

    def run(self):
        print("%s--在跑"%self.name)

class Bosi(Cat):
    def set_name(self, newName):
        self.name = newName

    def eat(self):
        print("%s--在吃"%self.name)
bs=Bosi("aa");
# bs.set_name(22)
bs.eat();

class base(object):
    def test(self):
        print('----base test----')

class A(base):
    def test(self):
        print('----A test----')
# 定义一个父类

class B(base):
    def test(self):
        print('----B test----')

# 定义一个子类，继承自A、B
class C(A,B):
    pass
obj_C = C()
obj_C.test()

print(C.__mro__)