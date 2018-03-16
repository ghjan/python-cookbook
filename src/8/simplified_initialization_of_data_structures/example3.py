# 你还能将不在fields 中的名称加入到属性中去
class Structure:
    # Class variable that specifies expected fields
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

        # Set the additional arguments (if any)
        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))
        if kwargs:
            raise TypeError('Duplicate values for {}'.format(','.join(kwargs)))


class Stock(Structure):
    _fields = ['name', 'shares', 'price']


# Example use
if __name__ == '__main__':
    s1 = Stock('ACME', 50, 91.1)
    print(s1.name, s1.shares, s1.price)
    s2 = Stock('ACME', 50, 91.1, date='8/2/2012')
    print(s2.name, s2.shares, s2.price, s2.date)

    try:
        s5 = Stock('ACME', shares=50, price=91.1, aa=1)
        print(s5.name, s5.shares, s5.price, s5.aa)
    except Exception as e:
        print(e)
