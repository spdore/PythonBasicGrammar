"""
求钱包余额小练习
初始50元，在购买了：
冰淇淋10元
可乐5元
钱包最后还剩多少元？
"""

# 定义变量
money = 50
icecream = 10
coke = 5

# 打印
print("当前钱包余额：", money, "元")
print("购买了冰淇淋，花费：", icecream, "元")
print("购买了可乐，花费：", coke, "元")
print("最终，钱包剩余：", money - icecream - coke, "元")