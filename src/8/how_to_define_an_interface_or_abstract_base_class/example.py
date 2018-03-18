# Defining a simple abstract base class

from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


# Example implementation
class SocketStream(IStream):
    def read(self, maxbytes=-1):
        print('reading')

    def write(self, data):
        print('writing:{}'.format(data))


# Example of type checking
def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    print('serializing:{}'.format(obj))


# Examples
if __name__ == '__main__':
    # Attempt to instantiate ABC directly (doesn't work)
    try:
        a = IStream()
    except TypeError as e:
        print(e)

    # Instantiation of a concrete implementation
    a = SocketStream()
    a.read()
    a.write('data writen')

    # Passing to type-check function
    serialize(None, a)

    # Attempt to pass a file-like object to serialize (fails)
    import sys

    try:
        print("to serialize to sys.stdout")
        serialize(None, sys.stdout)
    except TypeError as e:
        print(e)

    # Register file streams and retry
    import io

    # 除了继承这种方式外，还可以通过注册方式来让某个类实现抽象基类
    # Register the built-in I/O classes as supporting our interface
    IStream.register(io.IOBase)
    # Open a normal file and type check
    f = open('foo.txt')
    print("isinstance(f, IStream):{}".format(isinstance(f, IStream)))  # Returns True
    print("After register io.IOBase to IStream, to serialize to sys.stdout again")
    serialize(None, sys.stdout)
