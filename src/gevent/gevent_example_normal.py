#!/usr/bin/env python
# encoding: utf-8

"""
@author: david
@time: 9/9/17 1:56 PM
"""

import requests
import time


def request_url(url):
    """
    # 访问一个url并得到响应结果
    :param url:
    :return:
    """
    response = requests.get(url)
    return response.content


if __name__ == "__main__":
    # 准备一个待访问的url列表，该列表共包含4 * 10 = 40个url
    url_list = ['https://github.com/',
                'http://www.missshi.cn:8888/',
                'https://www.python.org/',
                'https://www.yahoo.com/'] * 10
    response_list = []
    begin_time = time.time()  # 记录当前时间
    for url in url_list:
        print(url)

        response_content = request_url(url)
        response_list.append(response_content)
    end_time = time.time()  # 记录结束时间
    used_time = end_time - begin_time  # 计算消耗时间
    print(used_time)
