a='bbatguigu';
b="atg";
c="atgaaaaaa";
#find 是从做右往左找
# 如果找到输出字符串首次找到的位置
find01 = a.find(b);
print(find01);
print("*********")
find02=a.find(c);
# 结果-1表示没有找到
print(find02);
print("*********")
d="ba";
find03=a.find(d,1,len(a));
print(find03)
print("*********")
print(a[len(a)-1]);
# rfind  类似于 find()函数，不过是从右边开始查找.
print("****refind*****")
print(a.find("atguigu"));
print(a.find("ba"));
print("****index*****");
# index()跟find()方法一样，只不过如果str不在 mystr中会报一个异常.
print(a.index("at"));
print("****rindex*****");
print(a.rindex("at"))
print("****replace*****");
print(a.replace("at","cc"));
print("****split*****");
ff="hello xisi and jiang"
print(ff.split(" "));
print("****partition*****");
print(ff.partition("and"))
print("****rpartition*****");
print(ff.rpartition("and"))
print("****upper****");
print(ff.upper())
print(ff)
print("****isspace****");
print(ff.isspace())
print("null")
dd="         "
print(dd.isspace())
print("****join****");
print(dd.join(ff))
print("****join2****");
name = ['hello', 'world', 'atguigu', 'and', 'atguiguPython']
mystr=" "
print(mystr.join(name))
mystr="_"
print(mystr.join(name))
print("****count****");
ccc="aabcdef"

print(ccc.count("a"))
print(ccc.count("b"))
print("****ljust****");
print(ccc.ljust(30));
print(ccc.center(30))
print(ccc.rjust(30))
print("**isalnum**")
print(ccc.isalnum());