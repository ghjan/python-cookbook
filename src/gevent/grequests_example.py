#!/usr/bin/env python
# encoding: utf-8

"""
@author: david
@time: 9/9/17 2:32 PM
"""
import grequests
import requests
import cProfile

url_list = ['https://github.com/',
            'http://www.missshi.cn:8888/',
            'https://www.python.org/',
            'https://www.yahoo.com/'] * 10


def haha(urls):
    rs = (grequests.get(u) for u in urls)
    return grequests.map(rs)

results1 = haha(url_list)
# cProfile.run("haha(url_list)")

print(len(results1))
print(results1[0])
#
# def hehe(urls):
#     hehe = [requests.get(i) for i in urls]
#     return hehe
#
#
# cProfile.run("hehe(url_list)")
