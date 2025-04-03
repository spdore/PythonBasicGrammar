"""
演示函数的多返回值的事例
"""

# 演示使用多个变量，接受多个变量
def test_return():
    return 1, "Hello", True

x, y, z = test_return()

print(x)
print(y)
print(z)