# setattr(instance, name, value)和instance.__dict__[name]=value是否等价？
# https://www.zhihu.com/question/268908178

# 最后要指出的一点是，如果你只是想简单的自定义某个类的单个属性访问的话就不
# 用去写描述器了。这种情况下使用8.6 小节介绍的property 技术会更加容易。当程序
# 中有很多重复代码的时候描述器就很有用了(比如你想在你代码的很多地方使用描述器
# 提供的功能或者将它作为一个函数库特性)。
# Descriptor for a type-checked attribute
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


# Class decorator that applies it to selected attributes
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            # Attach a Typed descriptor to the class
            setattr(cls, name, Typed(name, expected_type))
        return cls

    return decorate


# Example use
@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


if __name__ == '__main__':
    s = Stock('ACME', 100, 490.1)
    print(s.name, s.shares, s.price)
    s.shares = 50
    try:
        s.shares = 'a lot'
    except TypeError as e:
        print(e)
