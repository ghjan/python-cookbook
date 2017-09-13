import collections

from pprint import pprint

'''
Python’s super() considered super!
http://blog.csdn.net/qq_14898613/article/details/53792270

How to Incorporate a Non-cooperative Class
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
the method being called by super() needs to exist
被super()调用的方法需要存在
'''


class Root:
    def draw(self):
        # the delegation chain stops here
        assert not hasattr(super(), 'draw')


class Shape(Root):
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)

    def draw(self):
        print('(Shape)Drawing.  Setting shape to:', self.shapename)
        super().draw()


class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)

    def draw(self):
        print('(ColoredShape)Drawing.  Setting color to:', self.color)
        super().draw()


class Moveable:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print('(Moveable)Drawing at position:', self.x, self.y)


class MoveableAdapter(Root):
    def __init__(self, x, y, **kwds):
        self.movable = Moveable(x, y)
        super().__init__(**kwds)

    def draw(self):
        self.movable.draw()
        super().draw()


class MovableColoredShape(ColoredShape, MoveableAdapter):
    pass


if __name__ == '__main__':
    print("---------------------------")
    cs = ColoredShape(color='blue', shapename='square')
    cs.draw()
    print("---------------------------")
    MovableColoredShape(color='red', shapename='triangle', x=10, y=20).draw()
