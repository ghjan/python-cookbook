class Student(object):
    pass


s = Student()
s.name = 'Michael'  # 动态给实例绑定一个属性
print(s.name)


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


from types import MethodType

try:
    s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
except:
    s.set_age = MethodType(set_age, s, Student)  # 给实例绑定一个方法
s.set_age(25)  # 调用实例方法
print(s.age)  # 测试结果

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()  # 创建新的实例
try:
    s2.set_age(25)  # 尝试调用方法
except AttributeError as e:
    print(e)


def set_score(self, score):
    self.score = score


try:
    Student.set_score = set_score
except:
    Student.set_score = MethodType(set_score, None, Student)
print("-------------")
s.set_score(100)
print(s.score)
s2.set_score(99)
print(s2.score)

print("----  use __slots__")


class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'
try:
    s.score = 99  # 绑定属性'score'
except AttributeError as e:
    print(e)
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # AttributeError: 'Student' object has no attribute 'score'

print("---- 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的")


class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 9999
