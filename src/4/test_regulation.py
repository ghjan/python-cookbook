import re

'''

该题目是mastering regular expression 上作者反复讲解的一个例子。
具体要求：通常是保留小数点后两位数字，如果第3位不为0，也需要保留。
为实现这一功能，可以使用下面的代码。
注意正则末尾部分是\d*，而非\d+，否则就会出上楼主所说的情况，
由于后面需要吃进字符，以致于在匹配0.625这样的数字时在?这里回溯。

'''
s = ['12.375000000', '12.301', '12.300', '12.34']
for item in s:
    item = re.sub(r'''(\.\d\d[1-9]?)\d*''', r'\1', item)
    print(item)