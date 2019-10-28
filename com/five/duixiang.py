class aa(object):
    def first(self):
        print("aa")
    def __sec(self):
        print("bb");
    def third(self):
        self.__sec()
    def __del__(self):
        print("delete")
a=aa();
a.first();
a.third();
del a;
b=aa();
b.third()
b.first()