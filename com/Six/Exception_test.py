#FileNotFoundError
#方案一
try:
    print("aa")
    f=open("aa.txt")
except FileNotFoundError:
    print("FileNotFoundError...")
except NameError:
    print("nameerror...");

#NameError
try:
    print("aa")
    print(num)
except FileNotFoundError:
    print("FileNotFoundError...")
except NameError:
    print("nameerror...");
#
print("*"*30)
try:
    print("aa")
    print(num)
except (FileNotFoundError,NameError) as rest:     #方案二 捕获异常
    print("FileNotFoundError...")
    print("nameerror...");
    print("...%s"%rest)
except Exception:  #前面已经捕获，不会再执行了
    print("exception....")
else:
    print("程序没有出错")
finally:
    print("hehe ")
