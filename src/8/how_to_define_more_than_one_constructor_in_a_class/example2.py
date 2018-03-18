import time

'''
类方法的一个主要用途就是定义多个构造器。它接受一个 class 作为第一个参数(cls)。
你应该注意到了这个类被用来创建并返回最终的实例。在继承时也能工作的很好
这次在类方法里面使用了__new__(cls),效果等同于cls(t.tm_year, t.tm_mon, t.tm_mday)
'''


class Date:
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        d = cls.__new__(cls)
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d


if __name__ == '__main__':
    a = Date(2012, 12, 21)
    b = Date.today()
    print(a.year, a.month, a.day)
    print(b.year, b.month, b.day)


    class NewDate(Date):
        pass


    c = Date.today()
    d = NewDate.today()
    print('Should be Date instance:', Date)
    print('Should be NewDate instance:', NewDate)
