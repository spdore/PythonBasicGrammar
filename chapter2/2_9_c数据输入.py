"""
演示Python的input语句
获取键盘输入的信息
"""
name = input("请告诉我你是谁？")  # 获取键盘输入的信息
print(f"我知道了，你是：{name}")

# 输入数字类型
num = input("请告诉我你的银行卡密码：")
print(f"你银行卡密码的类型是：{type(num)}")  # input的内容统统为字符串类型

# 数据类型转换
print(f"你银行卡密码的类型是：{type(int(num))}")  # 自行转换类型