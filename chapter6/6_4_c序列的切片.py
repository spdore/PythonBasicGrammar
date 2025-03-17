"""
演示对序列进行切片操作
"""

# 对list进行切片，从1开始，4结束，步长1
my_list = [0, 1, 2, 3, 4, 5, 6]
res1 = my_list[1:4]  # 步长默认是1，可以不写
print(f"结果1：{res1}")

# 对tuple进行切片，从头开始，到最后结束，步长1
my_tuple = (0, 1, 2, 3, 4, 5, 6)
res2 = my_tuple[:]
print(f"结果2：{res2}")

# 对str进行切片，从头开始，到最后结束，步长2
my_str = "012134567"
res3 = my_str[::2]
print(f"结果3：{res3}")

# 对str进行切片，从头开始，到最后结束，步长-1
my_str = "012134567"
res4 = my_str[::-1]
print(f"结果4：{res4}")

# 对list进行切片，从3开始，到1结束，步长-1
my_list = [0, 1, 2, 3, 4, 5, 6]
res5 = my_list[3:1:-1]
print(f"结果5：{res5}")

# 对tuple进行切片，从头开始，到最后结束，步长-2
my_tuple = (0, 1, 2, 3, 4, 5, 6)
res6 = my_tuple[::-2]
print(f"结果6：{res6}")