a='atguigu';
print("lenght="+str(len(a))+'\n');
# name = input("请输入你的姓名")
# age = input("请输入你的age")
# print("name=%s"%(name));
# print("age=%s"%(age));

print("********")
for temp in a:
    print(temp)
# 字符串的下标
print("***sssssssss\n")
print(a[0])
print(a[1])
print("***sssssssss\n")
print(a[len(a)-1])
print(a[-1])
print(a[-2])
#切片
print("***************333333")
content='asdfghjkl'
print(content[0:3])
print(content[1:3])
print(content[2:])
print(content[1:-1])
print(content[::-1])


print("******nameList*********")
nameList=[1,"xiaosi",'dajiang']
print(nameList[0])
print(nameList[1])
nameList.append("nihao")
print(nameList)
print("******6666*********")
a=[1,2]
b=[3,4]
a.append(a)
print(a)
a.extend(b)
print(a)
c=[1,2]
c.insert(1,3)
print(c)

# del c[0]
# print(c)
# c.remove(c[0])
# print(c)

c.pop(2)
print(c)

if 1 in c:
    print("1存在")
print(c.index(1,0,3))
print(c.count(1))
c.reverse()
print(c)

d=[1,3,2,4]
d.sort(reverse=False)
print(d)

print(type(d))
