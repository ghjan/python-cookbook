'''
Python: 你不知道的 super
http://python.jobbole.com/86787/
----------------------------------------------
如果你认为 super 代表『调用父类的方法』，那你很可能会疑惑为什么 enter A 的下一句不是 enter Base 而是 enter B。
原因是，super 和父类没有实质性的关联，现在让我们搞清 super 是怎么运作的。
----------------------------------------------
super(cls, inst)
其中，cls 代表类，inst 代表实例，上面的代码做了两件事：

获取 inst 的 MRO 列表
查找 cls 在当前 MRO 列表中的 index, 并返回它的下一个类，即 mro[index + 1]
当你使用 super(cls, inst) 时，Python 会在 inst 的 MRO 列表上搜索 cls 的下一个类。

事实上，super 和父类没有实质性的关联。
super(cls, inst) 获得的是 cls 在 inst 的 MRO 列表中的下一个类。
'''
'''
Python:super函数
http://gohom.win/2016/02/23/py-super/
Python3中,super函数多了一种用法是直接super(),相当于super(type,首参), 这个首参就是一般的传入的self实例本身啦.
'''

class Base(object):
    def __init__(self):
        print("enter Base")
        print("leave Base")


class A(Base):
    def __init__(self):
        print("enter A")
        super(A, self).__init__()
        print("leave A")


class B(Base):
    def __init__(self):
        print("enter B")
        super(B, self).__init__()
        print("leave B")


class C(A, B):
    def __init__(self):
        print("enter C")
        super(C, self).__init__()
        print("leave C")


if __name__ == '__main__':
    c = C()
