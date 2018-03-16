# -*- coding: utf-8 -*-
# python中的类属性和实例属性 https://www.cnblogs.com/scolia/p/5582268.html
# 属性就是属于一个对象的数据或者函数，我们可以通过句点（.）来访问属性，同时 python 还支持在运作中添加和修改属性。
# 而数据变量，类似于： name = 'scolia' 这样的形式，会称其为字段；
# 而类里面的函数，又称为方法。
# 而方法又分为实例方法，类方法和静态方法
class Test(object):
    name = 'scolia'


def normal():
    a = Test()
    print(Test.name)  # 通过类进行访问
    print(a.name)  # 通过实例进行访问


# 通过类进行修改
def modify_prop1():
    a = Test()
    Test.name = 'scolia good'  # 通过类进行修改
    print(Test.name)
    print(a.name)


# 通过实例进行修改
def modify_prop2():
    a = Test()
    a.name = 'scolia good'  # 通过实例进行修改
    print(Test.name)
    print(a.name)


# 函数  dir()  就能查看对象的属性
def list_prop():
    a = Test()
    a.abc = 123
    print(dir(Test))
    print(dir(a))


if __name__ == '__main__':
    print("------normal-----")
    normal()
    print("------modify_prop1-----")
    modify_prop1()
    print("------modify_prop2-----")
    modify_prop2()
    print("------list_prop-----")
    list_prop()
