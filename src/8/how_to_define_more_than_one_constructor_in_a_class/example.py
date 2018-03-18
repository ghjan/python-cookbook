import time

'''
类方法的一个主要用途就是定义多个构造器。它接受一个 class 作为第一个参数(cls)。
你应该注意到了这个类被用来创建并返回最终的实例。在继承时也能工作的很好
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
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


if __name__ == '__main__':
    a = Date(2012, 12, 21)
    b = Date.today()
    print(a.year, a.month, a.day)
    print(b.year, b.month, b.day)


    class NewDate(Date):
        pass


    print("----------")
    c = Date.today()
    d = NewDate.today()
    print("----------")
    print('Should be Date instance:', Date)
    print('Should be NewDate instance:', NewDate)
