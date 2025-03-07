"""
演示对函数进行文档说明
"""

# 定义函数，进行文档说明
def add(x, y):
    """
    add函数可以接收2个参数，进行2数相加的功能
    :param x: 形参x表示两数相加的其中一个数字
    :param y: 形参y表示两数相加的另一个数字
    :return: 返回值是两数相加的结果 
    """
    result = x + y
    print(f"2数相加的结果是：{result}")
    return result

add(5, 6)