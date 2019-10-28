student={"name":'wanghua',id:100,"sex":'nan'}
print(student['name'])
print(student.get("name"))
print("id为=%s"%student["name"])
student["nvpengyou"]="buzhidao";
print(student);
print("删除后")
# del student;
student.clear();
print(student)
print("***********")
cc={"name":"lisi","age":20}
print("cc=%s"%cc)
cc.pop("name")
print(cc)
print("*******")
dd={"name":"lisi","age":20}
print(dd.keys())
print(dd.values())
aa=dd.popitem();
print(dd)
print(aa)
print(len(dd))
print("******")
a_str = "hello atguigu"
for char in a_str:
    print(char+" ")
print("***list***")
cc02={"name":"lisi","age":20}
for c in cc02.items():
    print(c)
print("你好%s,我是%s"%("aa","bb"))

print("******enumerate*****")
names03=["aa","bb","cc","dd"]
for index,na in enumerate(names03):
    print("%d:%s"%(index,na))
print("******enumerate*****")