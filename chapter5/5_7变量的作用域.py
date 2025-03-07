"""
演示函数使用时，定义的变量作用域
"""

# 演示局部变量
"""
def test_a():
    num = 100
    print(num)

test_a()
"""
# print(num)  除了函数局部变量就无法使用  

# 演示全局变量
"""
num = 200

def test__a():
    print(f"test__a:{num}")

def test__b():
    print(f"test__b:{num}")

test__a()
test__b()
print(num)
"""

# 在函数内修改全局变量
"""
num = 200

def test__a():
    print(f"test__a:{num}")

def test__b():
    num = 500  # 在内部新定义的局部变量
    print(f"test__b:{num}")

test__a()
test__b()
print(num)
"""

# global关键字，在函数内声明变量是全局变量
num = 200

def test__a():
    print(f"test__a:{num}")

def test__b():
    global num 
    num = 500  # 声明局部变量为全局变量
    print(f"test__b:{num}")

test__a()
test__b()
print(num)