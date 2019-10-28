# 定义一个函数。
def test02():
    print("aaaaa");
# 调用函数
test02();

def sum(a,b):
    print("a+b=%d"%(a+b))
sum(100,200)

def get_temperature():
    return 44;
print(get_temperature())

'''
 有参数由返回值
'''
def so(num=3):
    return num;


print(so())
print("****")
def nn(a,b,*args,**wargs):
    print(a)
    print(b)
    print(args)
    print(wargs)
nn(1,2,3,name="aa")

def re():
    return 1,2,3;

print(re())
print("**********")
def divid(a,b):
    aa=a//b;
    bb=a%b;
    return aa,bb;
print(divid(5,2));

print("-"*30)

print("****")
a=20;
def aa():
    global a
    a=200;
aa()
print(a);

print("****")
sumab=lambda args,args02:args+args02;
print(sumab(10,20));



