"""
演示对list列表的循环，使用while和for循环两种方式
"""

def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return:None
    """
    my_list = ["传智教育", "黑马程序员", "Python"]
    # 循环控制变量通过下标索引变量控制，默认0
    # 每一次循环将下标索引变量+1
    # 循环条件：下标索引变量 < 列表元素数量
    index = 0

    while index < len(my_list):
        # 通过index变量取出对应下标的元素
        element = my_list[index]
        print(f"列表的元素：{element}")

        # 至关重要 将循环变量(index)每次一循环都+1
        index += 1
    
    return index

def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return:None
    """
    my_list = [1, 2, 3, 4, 5]

    # for 临时变量 in 数据容器:
    for element in my_list:
        print(f"列表中的元素有：{element}")

list_while_func()
list_for_func()