# **coding: utf8**
import subprocess
data = subprocess.check_output(['cat', 'hello.py'])
print(data)

# def func(f):
#
#     def func_1(a):
#         print("调用 " + a)
#         return f(a)
#
#     return func_1
#
# @func
# def hello(a):
#     print("hello")
#
# hello("a")

b = {
    "a": 5,
    "b": 9
}


# def a(a, b):
#     print(a)
#     print(b)
#
# a(**b)
