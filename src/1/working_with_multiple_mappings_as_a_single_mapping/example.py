# example.py
#
# Example of combining dicts into a chainmap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

# (a) Simple example of combining
from collections import ChainMap

# 有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某些操作
c = ChainMap(a, b)
print(c['x'])  # Outputs 1  (from a)
print(c['y'])  # Outputs 2  (from b)
print(c['z'])  # Outputs 3  (from a)

# Output some common values
print('len(c):', len(c))
print('c.keys():', list(c.keys()))
print('c.values():', list(c.values()))

# Modify some values
print("ChainMap 使用原来的字典，它自己不创建新的字典。对于字典的更新或删除操作总是影响的是列表中第一个字典")
print("before modifying c, a:", a)
c['z'] = 10
c['w'] = 40
del c['x']
print("after modifying c, a:", a)

# Example of stacking mappings (like scopes)
print("Example of stacking mappings (like scopes)")
values = ChainMap()
values['x'] = 1

# Add a new mapping
values = values.new_child()
values['x'] = 2

# Add a new mapping
values = values.new_child()
values['x'] = 3

print(values)
print(values['x'])

# Discard last mapping
values = values.parents
print(values)
print(values['x'])

# Discard last mapping
values = values.parents
print(values)
print(values['x'])

print("考虑使用 update() 方法将两个字典合并,创建一个完全不同的字典对象")

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged['y'])
print(merged['z'])
print("merged:", merged)
