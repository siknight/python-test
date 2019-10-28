try:
    a="abc";
    if len(a)<5:
        raise  Exception("你的长度小于2")
except Exception as info:
    print(info)

print("***************")
class Myexception(Exception):
    def __init__(self):
       print("aa")


try:
    a="abc";
    if len(a)<5:
        raise Myexception()
except Myexception as info:
    print(info.aa)
