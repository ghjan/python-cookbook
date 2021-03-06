# example.py
#
# Some examples of using generators in arguments

import os

files = os.listdir('.') or os.listdir(os.path.expanduser('~'))
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
# 当生成器表达式作为一个单独参数传递给函数时候的巧妙语法（你并不需要多加一个括号）
# 相比列表表达式，生成器方案会以迭代的方式转换数据，因此更省内存;
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

# 在使用一些聚集函数比如 min() 和 max() 的时候你可能更加倾向于使用生成器版本， 它们接受的一个 key 关键字参数或许对你很有帮助
# Alternative: Returns {'name': 'AOL', 'shares': 20}
min_shares2 = min(portfolio, key=lambda s: s['shares'])
print(min_shares2)
