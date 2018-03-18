from abc import ABCMeta, abstractmethod


# @abstractmethod 还能注解静态方法、类方法和properties 。你只需保证这个注
# 解紧靠在函数定义前即可：
class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @classmethod
    @abstractmethod
    def method1(cls):
        pass

    @staticmethod
    @abstractmethod
    def method2():
        pass
