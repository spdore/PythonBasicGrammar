"""
演示函数作为参数传递
"""

# 定义一个函数，接受另一个函数作为传入参数
def test_func(compute):
    result = compute(1, 2)  # compute是参数
    print(f"compute的类型是：{type(compute)}\n计算结果是{result}")

# 定义一个函数，准备作为参数传入另一个函数
def compute(a, b):
    return a + b

# 调用并传入函数
test_func(compute)