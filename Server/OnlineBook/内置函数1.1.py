# **coding: utf8**


class Person:

    """
    介绍__init__, __repr__, __str__, format__, __call__, __gt__, __ge__, __lt__, __le__ 和　__eq__的基本用法
    """

    _formats = {
        'en': 'I am {0.age} years  old!',
        'cn': '｛我{0.age}了！｝'
    }

    # 初始化操作
    def __init__(self, age):
        self.age = age

    # 交互显示器显示
    def __repr__(self):
        return '年龄：{0.age}'.format(self)

    # str()或print()输出
    def __str__(self):
        return '年龄：{0.age}'.format(self)

    # 自定义字符串的格式化
    # 第二参数：format_spec(格式化方式)
    def __format__(self, format_spec):
        if format_spec == '':
            format_spec = 'cn'
        fmt = self._formats[format_spec]
        return fmt.format(self)

    # 一个类实例也可以变成一个可调用对象，需要实现一个特殊方法__call__()
    def __call__(self):
        print("调用call")

    # 大于操作
    def __gt__(self, other):
        return self.age > other.age

    # 大于等于操作
    def __ge__(self, other):
        return self.age >= other.age

    # 小于操作
    def __lt__(self, other):
        return self.age < other.age

    # 小于等于操作
    def __le__(self, other):
        return self.age <= other.age

    # 等于操作
    def __eq__(self, other):
        return self.age == other.age


# __init__
person = Person(10)

# __repr__

# __str__
print(person)  # 年龄：10

# __format__
print(format(person, 'en'))  # I am 10 years  old!

# __call__
person()  # 调用call

person_18 = Person(18)
person_60 = Person(60)
# __gt__
print(person_60 > person_18)  # True
# __ge__
print(person_60 >= person_18)  # True
# __lt__
print(person_60 < person_18)  # False
# __le__
print(person_60 <= person_18)  # False
