# example.py
#
# Examples of simple regular expression matching

import re

# Some sample text
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

# (a) Find all matching dates
print("想使用同一个模式去做多次匹配, 模式字符串预编译为模式对象")
datepat = re.compile(r'\d+/\d+/\d+')
print(datepat.findall(text))

print("findall, # (b) Find all matching dates with capture groups 利用括号去捕获分组")
# (b) Find all matching dates with capture groups
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

# (c) Iterative search
print("finditer,# (c) Iterative search")
print("findall() 方法会搜索文本并以列表形式返回所有的匹配。 如果你想以迭代方式返回匹配，可以使用 finditer() 方法来代替")
for m in datepat.finditer(text):
    print(m.groups())
