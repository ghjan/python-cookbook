import time
import random


def old_fib(n):
    res = [0] * n
    index = 0
    a = 0
    b = 1
    while index < n:
        res[index] = b
        a, b = b, a + b
        index += 1
    return res


def fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        yield b
        a, b = b, a + b
        index += 1


def stupid_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_cnt = yield b
        print('let me think {0} secs'.format(sleep_cnt))
        time.sleep(sleep_cnt)
        a, b = b, a + b
        index += 1


# yield from用于重构生成器
def copy_fib(n):
    print('I am copy from fib')
    yield from fib(n)
    print('Copy end')


# yield from的作用还体现可以像一个管道一样将send信息传递给内层协程，并且处理好了各种异常情况
def copy_stupid_fib(n):
    print('I am copy from stupid fib')
    yield from stupid_fib(n)
    print('Copy end')


if __name__ == '__main__':
    # print('-' * 10 + 'test old fib' + '-' * 10)
    # for fib_res in old_fib(20):
    #     print(fib_res)
    #
    # print('-' * 10 + 'test yield fib' + '-' * 10)
    # for fib_res in fib(20):
    #     print(fib_res)

    '''
其中next(sfib)相当于sfib.send(None)，可以使得sfib运行至第一个yield处返回。
后续的sfib.send(random.uniform(0, 0.5))则将一个随机的秒数发送给sfib，作为当前中断的yield表达式的返回值。
这样，我们可以从“主”程序中控制协程计算斐波那契数列时的思考时间，协程可以返回给“主”程序计算结果，Perfect！
    '''
    print('-' * 10 + 'test yield send' + '-' * 10)
    N = 20
    sfib = stupid_fib(N)
    fib_res = next(sfib)
    while True:
        print(fib_res)
        try:
            '''Resumes the generator and "sends" a value that becomes the result of the current yield-expression.'''
            fib_res = sfib.send(random.uniform(0, 0.5))
        except StopIteration:
            break

    print('-' * 10 + 'test yield from' + '-' * 10)
    for fib_res in copy_fib(20):
        print(fib_res)

    print('-' * 10 + 'test yield from and send' + '-' * 10)
    N = 20
    csfib = copy_stupid_fib(N)
    fib_res = next(csfib)
    while True:
        print(fib_res)
        try:
            fib_res = csfib.send(random.uniform(0, 0.5))
        except StopIteration:
            break
