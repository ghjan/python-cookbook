#!/usr/bin/env python
# encoding: utf-8

"""
@author: david
@time: 9/9/17 1:56 PM
"""

import gevent
import requests
import time


def request_url(url):
    """
    # 访问一个url并得到响应结果
    :param url:
    :return:
    """
    from gevent import monkey
    monkey.patch_socket()  # 引入猴子补丁
    print(url)

    response = requests.get(url)
    print("response of url:", url)

    return response.content


if __name__ == "__main__":
    url_list = ['https://github.com/',
                'http://www.missshi.cn:8888/',
                'https://www.python.org/',
                'https://www.yahoo.com/'] * 10
    task_list = []
    response_list = []
    begin_time = time.time()
    for url in url_list:
        task_list.append(gevent.spawn(request_url, url))
    result = gevent.joinall(task_list)
    end_time = time.time()
    used_time = end_time - begin_time
    print(used_time)
    print(type(result))
    print(result[0])
    print(task_list[0])
