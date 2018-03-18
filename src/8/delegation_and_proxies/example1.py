class A:
    def spam(self, x):
        print('A.spam')

    def foo(self):
        print('A.foo')


class B:
    def __init__(self):
        self._a = A()

    def bar(self):
        print('B.bar')

    # Expose all of the methods defined on class A   
    def __getattr__(self, name):
        """这个方法在访问的attribute不存在的时候被调用
            the __getattr__() method is actually a fallback method
            that only gets called when an attribute is not found"""
        return getattr(self._a, name)


if __name__ == '__main__':
    b = B()
    b.bar()
    b.spam(42)
    b.foo()
