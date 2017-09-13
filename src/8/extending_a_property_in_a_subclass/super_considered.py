import collections

from pprint import pprint

'''
Python’s super() considered super!
http://blog.csdn.net/qq_14898613/article/details/53792270
Practical Advice:
    the method being called by super() needs to exist
    the caller and callee need to have a matching argument signature
    and every occurrence of the method needs to use super()

The three techniques listed above provide the means to design cooperative classes that can be composed or reordered by subclasses.
上面列出的三个技术是为了设计协调的类，它们能被子类组合或者重排序。
'''


class LoggingDict(dict):
    def __setitem__(self, key, value):
        print('Settingto(LoggingDict) %r' % (key, value))
        super().__setitem__(key, value)


# 新类的继承树是：LoggingOD, LoggingDict,OrderedDict, dict, object.
class LoggingOD(LoggingDict, collections.OrderedDict):
    pass


'''
和super()相关，类设计的原则
the caller and callee need to have a matching argument signature
调用者和被调用者需要有匹配的参数
'''


class Shape:
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)


class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)


if __name__ == '__main__':
    pprint(LoggingOD.__mro__)
    position = LoggingOD.__mro__.index
    assert position(LoggingDict) < position(collections.OrderedDict)
    assert position(collections.OrderedDict) < position(dict)
    print("---------------------------")
    cs = ColoredShape(color='red', shapename='circle')
    print("cs.shapename:{}".format(cs.shapename))
    print("cs.color:{}".format(cs.color))
