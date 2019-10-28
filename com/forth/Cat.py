class Cat:
    a=10;
    #self是对象本身，不用自己传，相当于java中的构造方法
    def __init__(self,name,age):
        print("init")
        self.name=name
        self.age=age;
    def eat(self):
        print("猫在吃鱼");
    def drink(self):
        print("喝")
tom=Cat("hehe",10);
tom.eat();
tom.drink();
print(tom.name)
print(tom.age)
print(id(tom)) #id为打印内存地址
