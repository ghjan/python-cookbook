# Examples of different ways to filter data
'''
使用列表推导的一个潜在缺陷就是如果输入非常大的时候会产生一个非常大的结果集，占用大量内存。 如果你对内存比较敏感，
那么你可以使用生成器表达式迭代产生过滤的元素
'''

'''
值得关注的过滤工具就是 itertools.compress() ， 它以一个 iterable 对象和一个相对应的 Boolean 选择器序列作为输入参数。
然后输出 iterable 对象中对应选择器为 True 的元素。
和 filter() 函数类似， compress() 也是返回的一个迭代器。因此，如果你需要得到一个列表， 那么你需要使用 list() 来将结果转换为列表类型。
'''
mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# list comprehension example
print("-----list comprehension example----")
# All positive values
pos = [n for n in mylist if n > 0]
print(pos)

# All negative values
neg = [n for n in mylist if n < 0]
print(neg)

# Negative values clipped to 0
neg_clip = [n if n > 0 else 0 for n in mylist]
print(neg_clip)

# Positive values clipped to 0
pos_clip = [n if n < 0 else 0 for n in mylist]
print(pos_clip)

# filter example
print("-----filter example----")
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)

# compress example
print("-----compress example----")
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

more5 = [n > 5 for n in counts]
a = list(compress(addresses, more5))
print(a)
