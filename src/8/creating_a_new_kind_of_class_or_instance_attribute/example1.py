# -*- coding: utf-8 -*-
# Descriptor attribute for an integer type-checked attribute
# python描述符是一个“绑定行为”的对象属性，在描述符协议中，它可以通过方法重写属性的访问。
# 这些方法有 __get__(), __set__(), 和__delete__()。如果这些方法中的任何一个被定义在一个对象中，这个对象就是一个描述符。

# 描述器可实现大部分Python 类特性中的底层魔法， 包括@classmethod 、
# @staticmethod 、@property ，甚至是slots 特性。
# 通过定义一个描述器，你可以在底层捕获核心的实例操作(get, set, delete)，并且
# 可完全自定义它们的行为。这是一个强大的工具，有了它你可以实现很多高级功能，
# 并且它也是很多高级库和框架中的重要工具之一。
# 描述器的一个比较困惑的地方是它只能在类级别被定义，
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            # 如果一个描述器被当做一个类变量来访问，那么instance参数被设置成None
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if isinstance(value, Integer):
            instance.__dict__[self.name] = value.name
        elif not isinstance(value, int):
            raise TypeError('Expected an int')
        else:
            instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    p = Point(2, 3)
    print(p.x)
    p.y = 5
    print(p.x)
    print(Point.x)
    try:
        p.x = 2.3
    except TypeError as e:
        print(e)
