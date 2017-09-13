import collections

from pprint import pprint

'''
Python’s super() considered super!
http://blog.csdn.net/qq_14898613/article/details/53792270
Complete Example – Just for Fun
'''

from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first seen'

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__,
                           OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)


if __name__ == '__main__':
    print("---------------------------")
    oc = OrderedCounter('abracadabra')
    print(oc)
