# example.py
#
# Regular expression that matches multiline patterns

import re

text = '''/* this is a
              multiline comment */
'''

# 非捕获组-如何关闭圆括号的捕获能力？而只是用它来做分组，方法是在左括号的后边加上?:
# 通过在 * 或者 + 这样的操作符后面添加一个 ? 可以强制匹配算法改成寻找最短的可能匹配。
# 非捕获组
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
# 捕获组
comment2 = re.compile(r'/\*((.|\n)*?)\*/')
# 标志参数叫 re.DOTALL ，在这里非常有用。 它可以让正则表达式中的点(.)匹配包括换行符在内的任意字符
comment3 = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text))
print(comment2.findall(text))
print(comment3.findall(text))
