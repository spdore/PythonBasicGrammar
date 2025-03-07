"""
演示特殊字面量：None
"""

# 无return语句函数返回值
def say_hi():
    print("你好啊")

result = say_hi()
print(f"无返回值的函数，返回的内容是：{result}")
print(f"无返回值的函数，返回内容的类型是：{type(result)}")

# 主动返回none的函数
def say_hi2():
    print("你好呀")
    return None

result = say_hi2()
print(f"无返回值的函数，返回的内容是：{result}")
print(f"无返回值的函数，返回内容的类型是：{type(result)}")

# None用于if判断
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None

result = check_age(16)
if not result: 
    # 进入if表示result是None值，也就是False
    print("未成年，不可以进入")

# None声明无初始值的变量
name = None