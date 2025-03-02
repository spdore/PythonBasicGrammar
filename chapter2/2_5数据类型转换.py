# 将数字类型转化为字符串
num_str = str(11)
print(type(num_str), num_str)

float_str = str(11.345)
print(type(float_str), float_str)

# 将字符串转化为数字
num1 = int("11")
print(type(num1), num1)

num2 = float("11.345")
print(type(num2), num2)

"""
错误示例，想要将字符串转为数字，必须要求字符串中内容都是数字

num3 = int("黑马程序员")
print(type(num3), num3)
"""

# 整数转浮点数
float_num = float(11)
print(type(float_num), float_num)

# 浮点数转整数
int_num = int(11.543)
print(type(int_num), int_num)