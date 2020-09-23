# python 基本语法练习
import support
from sup import support as sup2


def print_str(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# 列表类似于java 数组，要用[] ,
# 列表（数组）： ['Google', 'Runoob', 1997, 2000]
# 元组（不可变数组）： ('Google', 'Runoob', 1997, 2000)
# 字典（map）： {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
# 集合 (list)： {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
def f_list():
    list = [1, 2, 3]
    print("this is a list : ", list)
    print("this is the first one", list[1])


# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
def f_first():
    a, b = 0, 1
    while b < 1000:
        print(b, end=',')
        a, b = b, a + b


if __name__ == '__main__':
    print_str('PyCharm')
    f_list()
    f_first()
    print()
    support.f_print("PyCharm")
    sup2.f_print("2")
