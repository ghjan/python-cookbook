import math


class Structure:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the remaining keyword arguments
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))

        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))


# Example class definitions
class Stock(Structure):
    _fields = ['name', 'shares', 'price']


# Example use
if __name__ == '__main__':
    # s1 = Stock('ACME', 50, 91.1)
    # print(s1.name, s1.shares, s1.price)
    s2 = Stock('ACME', 50, price=91.1)
    print(s2.name, s2.shares, s2.price)
    s3 = Stock('ACME', shares=50, price=91.1)
    print(s3.name, s3.shares, s3.price)
    try:
        s4 = Stock('ACME', 50, 91.1, price=99.1)
        print(s4.name, s4.shares, s4.price)
    except Exception as e:
        print(e)

    try:
        s5 = Stock('ACME', shares=50, price=91.1, aa=1)
        print(s5.name, s5.shares, s5.price)
    except Exception as e:
        print(e)
        print("解决方案请看example3")
