a=(2,3,4)
print(a);
print(type(a))
print()
b=(2,)
c=(2,3,[4,5],2)
c[2].append(6);
print(c)

print(c.index(2))
print(c.count(2))

d=["a","b","c"];
print(tuple(d))
print(tuple("abc"))


e=[(1,2),(2,3)]
print(e[1])
print(e[1][0]);