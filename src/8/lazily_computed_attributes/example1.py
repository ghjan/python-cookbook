# -*- coding: utf-8 -*-
# 很多时候，构造一个延迟计算属性的主要目的是为了提升性能。例如，你可以避免
# 计算这些属性值，除非你真的需要它们。这里演示的方案就是用来实现这样的效果的，
# 只不过它是通过以非常高效的方式使用描述器的一个精妙特性来达到这种效果的。
# 正如在其他小节(如8.9 小节) 所讲的那样，当一个描述器被放入一个类的定义时，
# 每次访问属性时它的get () 、set () 和delete () 方法就会被触发。不过，
# 如果一个描述器仅仅只定义了一个get () 方法的话，它比通常的具有更弱的绑定。
# 特别地，只有当被访问属性不在实例底层的字典中时get () 方法才会被触发。

import math


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    c = Circle(4.0)

    print(vars(c))
    print(c.area)
    print(vars(c))  # var(c) 等价于 c.__dict__
    print(c.area)
    print(c.perimeter)
    print(vars(c))
    print(c.perimeter)

    c.area = 30
    print(c.area)
