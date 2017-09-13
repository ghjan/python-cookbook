# Example of managed attributes via properties
'''
一个描述器就是一个实现了三个核心的属性访问操作(get, set, delete)的类， 分别为 __get__() 、__set__() 和 __delete__()
这三个特殊的方法。 这些方法接受一个实例作为输入，之后相应的操作实例底层的字典。
'''


class String:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        instance.__dict__[self.name] = value


class Person:
    name = String('name')

    def __init__(self, name):
        self.name = name


class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


if __name__ == '__main__':
    a = Person('Guido')
    print(a.name)
    a.name = 'Dave'
    print(a.name)
    try:
        a.name = 42
    except TypeError as e:
        print(e)
