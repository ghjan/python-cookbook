#!/usr/bin/env python
# encoding: utf-8

"""
@author: david
@time: 9/11/17 11:07 AM
"""


def consumer():
    r = 'yield'
    while True:
        # 当下边语句执行时，先执行yield r，然后consumer暂停，此时赋值运算还未进行
        # 等到producer调用send()时，send()的参数作为yield r表达式的值赋给等号左边
        n = yield r  # yield表达式可以接收send()发出的参数
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)  # 调用consumer生成器
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


def gen():
    a = yield 1
    print('yield a %s' % a)
    b = yield 2
    print('yield b %s' % b)
    c = yield 3
    print('yield c %s' % c)


if __name__ == '__main__':
    c = consumer()
    produce(c)
    print("------------")
    r = gen()
    x = next(r)
    print('next x %s' % x)
    y = r.send(10)
    print('next y %s' % y)
    z = next(r)
    print('next z %s' % z)
