# example.py
#
# Example of using shell-wildcard style matching in list comprehensions
# fnmatch() 函数使用底层操作系统的大小写敏感规则(不同的系统是不一样的)来匹配模式, on windows...
# fnmatchcase() can be used then if you need to
# fnmatch() 函数匹配能力介于简单的字符串方法和强大的正则表达式之间。
# 如果在数据处理操作中只需要简单的通配符就能完成的时候，这通常是一个比较合理的方案。

from fnmatch import fnmatchcase as match

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

a = [addr for addr in addresses if match(addr, '* ST')]
print(a)

b = [addr for addr in addresses if match(addr, '54[0-9][0-9] *CLARK*')]
print(b)
