# Tricky initialization problem involving multiple inheritance.
# Uses super().spam() in Class A will use Class B.spam()

class Base:
    def __init__(self):
        print('Base.__init__')

    def spam(self):
        print('Base.spam')


class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')

    def spam(self):
        print('A.spam')
        super().spam()


class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')

    def spam(self):
        print('B.spam')


class C(A, B):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('C.__init__')


if __name__ == '__main__':
    print("---------mro")
    print("C.__mro__:{}".format(C.__mro__))
    print("---------init")
    # Observe that each class initialized only once
    c = C()
    print("---------spam")
    c.spam()
