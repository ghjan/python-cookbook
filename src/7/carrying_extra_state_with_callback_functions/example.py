# This example is about the problem of carrying extra state around
# through callback functions.   To test the examples, this very
# simple code emulates the typical control of a callback.

def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)


# A simple function for testing
def add(x, y):
    return x + y


# (a) A simple callback example


def print_result(result):
    print("Got:", result)


# (b) Using a bound method


class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))


# (c) Using a closure


def make_handler_closure():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

    return handler


# (d) Using a coroutine


def make_handler_coroutine():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


# (e) Partial function application

class SequenceNo:
    def __init__(self):
        self.sequence = 0


def handler_partial(result, seq):
    seq.sequence += 1
    print('[{}] Got: {}'.format(seq.sequence, result))


if __name__ == '__main__':
    print('# --- Simple Example')
    apply_async(add, (2, 3), callback=print_result)
    apply_async(add, ('hello', 'world'), callback=print_result)

    print('# --- Using a bound-method')
    r = ResultHandler()
    apply_async(add, (2, 3), callback=r.handler)
    apply_async(add, ('hello', 'world'), callback=r.handler)

    print('# --- Using a closure')
    handler = make_handler_closure()
    apply_async(add, (2, 3), callback=handler)
    apply_async(add, ('hello', 'world'), callback=handler)

    print('# --- Using a coroutine')
    handler = make_handler_coroutine()
    next(handler)  # Advance to the yield
    apply_async(add, (2, 3), callback=handler.send)
    apply_async(add, ('hello', 'world'), callback=handler.send)

    print('# --- Using partial')
    seq = SequenceNo()
    from functools import partial

    apply_async(add, (2, 3), callback=partial(handler_partial, seq=seq))
    apply_async(add, ('hello', 'world'), callback=partial(handler_partial, seq=seq))
