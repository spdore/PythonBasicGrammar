"""
演示for循环的嵌套应用
"""
i = 0

# 坚持表白100天，每天都送10朵花
for i in range(1, 101):
    print(f"今天是向小美表白的第{i}天，加油坚持。")

    # 写内层循环
    for j in range(1, 11):
        print(f"给小美送的第{j}朵玫瑰花")

    print("小美我喜欢你")

print(f"第{i}天，表白成功")