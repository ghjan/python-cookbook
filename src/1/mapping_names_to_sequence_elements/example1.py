# example.py

from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


# Some Data
records = [
    ('GOOG', 100, 490.1),
    ('ACME', 100, 123.45),
    ('IBM', 50, 91.15)
]

StockFull = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# Create a prototype instance
stock_prototype = StockFull('', 0, 0.0, None, None)


# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)


if __name__ == '__main__':
    print(compute_cost(records))
    print("-----use _replace----")
    print("命名元组拥有可选或者缺失字段时候， 它是一个非常方便的填充数据的方法。 你可以先创建一个包含缺省值的原型元组，然后使用 _replace() 方法创建新的值被更新过的实例")
    a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
    print(dict_to_stock(a))
    b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
    print(dict_to_stock(b))
    print("最后要说的是，如果你的目标是定义一个需要更新很多实例属性的高效数据结构，那么命名元组并不是你的最佳选择。 这时候你应该考虑定义一个包含 __slots__ 方法的类（参考8.4小节）。")
