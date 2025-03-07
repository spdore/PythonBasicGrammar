"""
演示：定义函数返回值的语法格式
"""

# 定义一个函数，完成两数相加的功能
def add(a, b):
    result = a + b
    return result
    print("我完事了")  # return退出函数，无法执行该语句

r = add(5, 6)
print(r)