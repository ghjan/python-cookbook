#!/usr/bin/env python
# encoding: utf-8

"""
p09_replace_single_method_classes_with_functions
@author: david
@time: 9/13/17 11:21 AM

任何时候只要你碰到需要给某个函数增加额外的状态信息的问题，都可以考虑使用闭包。
相比将你的函数转换成一个类而言，闭包通常是一种更加简洁和优雅的方案
"""

try:  # py3
    from urllib.request import urlopen
except:  # py2
    from urllib2 import urlopen


class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


# Example use. Download stock data from yahoo
def download_stock_data_from_yahoo(lines):
    [print(line.decode('utf-8')) for line in lines]


def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))

    return opener


if __name__ == '__main__':
    print("---------------use class")
    yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
    download_stock_data_from_yahoo(yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'))

    print("---------------use function instead of class")
    # Example use
    yahoo_2 = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
    download_stock_data_from_yahoo(yahoo_2(names='IBM,AAPL,FB', fields='sl1c1v'))
