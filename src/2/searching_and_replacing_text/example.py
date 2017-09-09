# example.py
#
# Examples of simple regular expression substitution

import re

# Some sample text
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

# (a) Simple substitution
print(datepat.sub(r'\3-\1-\2', text))

# (b) Replacement function
from calendar import month_abbr


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


print(datepat.sub(change_date, text))

print("----------Searching and Replacing Case-Insensitive Text")


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace


text2 = 'UPPER PYTHON, lower python, Mixed Python'

# matchcase('snake') 返回了一个回调函数(参数必须是 match 对象)
print(re.sub('python', matchcase('snake'), text2, flags=re.IGNORECASE))
