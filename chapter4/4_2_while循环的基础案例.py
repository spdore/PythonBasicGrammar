"""
演示while循环的基础案例 - 猜数字
"""
import random
num = random.randint(1,100)
guess = int(input("请输入你猜的数字："))
time = 1

# 判定条件
while guess != num:
    if guess > num:
        guess = int(input("猜大了，请重猜："))
        time += 1
    else:
        guess = int(input("猜小了，请重猜："))
        time += 1

print(f"恭喜你猜对了，数字是{num}，你猜了{time}次")