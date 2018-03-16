# example1里面的延迟计算方案有一个小缺陷就是计算出的值被创建后是可以被修改的
import math


def lazyproperty(func):
    name = '_lazy_' + func.__name__

    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value

    return lazy


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

    try:
        c.area = 30
        print(c.area)
    except:
        print("...")
    c._lazy_area = 20
    print(c.area)
