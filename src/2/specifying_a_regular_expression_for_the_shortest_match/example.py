# example.py
#
# Example of a regular expression that finds shortest matches

import re

# Sample text
text = 'Computer says "no." Phone says "yes."'

# (a) Regex that finds quoted strings - longest match
str_pat = re.compile(r'\"(.*)\"')
print(str_pat.findall(text))

# (b) Regex that finds quoted strings - shortest match
# 非贪婪模式
# 通过在 * 或者 + 这样的操作符后面添加一个 ? 可以强制匹配算法改成寻找最短的可能匹配。
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text))



