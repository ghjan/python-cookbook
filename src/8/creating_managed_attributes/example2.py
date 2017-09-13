#!usr/bin/env python
# -*- coding:utf-8 -*-

# Example of managed attributes via properties
# 在已存在的get和set方法基础上定义property
class Person:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    # Getter function
    def get_first_name(self):
        return self._first_name

    # Setter function
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    # Make a property from existing get/set methods
    name = property(get_first_name, set_first_name, del_first_name)


if __name__ == '__main__':
    a = Person('Guido')
    print(a.name)
    a.name = 'Dave'
    print(a.name)
    try:
        print("-----try to set a property to strange type")
        a.name = 42
    except TypeError as e:
        print(e)
    print("-----try to delete a property")
    try:
        del a.name
    except AttributeError as e:
        print(e)
    print("-----use getter and setter functions(Python代码被集成到一个大型基础平台架构或程序中)")
    print("a.get_first_name():{}".format(a.get_first_name()))
    a.set_first_name('Larry')
    print("a.get_first_name():{}".format(a.get_first_name()))
