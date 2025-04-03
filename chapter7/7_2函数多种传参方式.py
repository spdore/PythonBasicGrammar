"""
演示多种参数传入形式
"""
def user_info(name, age, gender):
    print(f"姓名是：{name}，年龄是：{age}，性别是：{gender}")

# 位置参数
user_info("小明", 20, "男")

# 关键字参数
user_info(name = "小王", age = 99, gender = "女")
user_info(age = 99, name = "潇潇", gender = "女")  # 可以不按照定义的顺序传参
user_info("大刘", age = 49, gender = "女")

# 缺省参数(默认值)
def user_info(name, age, gender = '男'):  # 默认值在最后
    print(f"姓名是：{name}，年龄是：{age}，性别是：{gender}")

user_info(name = "小天", age = 22)
user_info(name = "小胡", age = 22, gender = "女")

# 不定长 - 位置不定长， *号
# 不定长定义的形式参数会作为元组存在，接受不定长参数的传入
def user_info(*args):
    print(f"args参数的类型是：{type(args)}，内容是{args}")

user_info(1, 2, '是你的卡', True)

# 不定长 - 关键字不定长， **号
def user_info(**kwargs):
    print(f"args参数的类型是：{type(kwargs)}，内容是{kwargs}")

user_info(age = 11, correct = True, name = "Jackson")  # 字典形式传入