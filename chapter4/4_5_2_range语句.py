"""
演示Python中的range()语句的基本使用
"""

# range语法1 range(num)
for x in range(10):
    print(x, end = '')  # 不包括10

print()

# range语法2 range(num1, num2)
for x in range(5, 10):
    # 从5开始10结束（不包含10本身）的一个数字序列
    print(x, end = '') 

print()

# range语法2 range(num1, num2, step)
for x in range(5, 10, 2):
    # 从5开始10结束,步长为2（不包含10本身）的一个数字序列
    print(x, end = '')