namesList=["lisi","jiang","xuyuan",6]
# print 默认换行
print(namesList[0]);
print(namesList[1])
print(namesList[2])
print(namesList[3])

print("*********1")
for name in  namesList:
    print(name)
print("*********2")
i=0;
while i<len(namesList)-1:
    print(namesList[i])
    i+=1;
# print("*******add list*****")
# a=input("添加一个元素")
# namesList.append(a);
# for name in namesList:
#     print(name)
print("*******add list*****")
namesList02=["keai01","keai02","keai03"]
namesList.extend(namesList02)
print(namesList)
# for name in namesList:
#     print(name)
print("****insert****")
c=["aa","bb"];
c.insert(1,22);
print(c)
c[0]="si";
print(c[0])
print(c)

print("*******contain****")
if "bb" in c:
    print(True);
else :
    print(False);
d=[4,8,7,10]
d.sort()
print(d)
d.reverse()
print(d)

print("*********last")
c,d=20,30
print("c=%d"%c)
print("c=%d"%d)
