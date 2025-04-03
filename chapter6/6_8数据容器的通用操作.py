"""
演示数据容器的通用操作
"""
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

# len元素个数
print(f"列表元素个数有：{len(my_list)}")
print(f"元组元素个数有：{len(my_tuple)}")
print(f"字符串元素个数有：{len(my_str)}")
print(f"集合元素个数有：{len(my_set)}")
print(f"字典元素个数有：{len(my_dict)}\n")

# max最大元素
print(f"列表最大元素是：{max(my_list)}")
print(f"元组最大元素是：{max(my_tuple)}")
print(f"字符串最大元素是：{max(my_str)}")
print(f"集合最大元素是：{max(my_set)}")
print(f"字典最大元素是：{max(my_dict)}\n")

# min最小元素
print(f"列表最小元素是：{min(my_list)}")
print(f"元组最小元素是：{min(my_tuple)}")
print(f"字符串最小元素是：{min(my_str)}")
print(f"集合最小元素是：{min(my_set)}")
print(f"字典最小元素是：{min(my_dict)}\n")

# 类型转换：容器转列表
print(f"列表转列表的结果是：{list(my_list)}")
print(f"元组转列表的结果是：{list(my_tuple)}")
print(f"字符串转列表的结果是：{list(my_str)}")
print(f"集合转列表的结果是：{list(my_set)}")
print(f"字典转列表的结果是：{list(my_dict)}\n")  # 只保留key，不保留value

# 类型转换：容器转元组
print(f"列表转元组的结果是：{tuple(my_list)}")
print(f"元组转元组的结果是：{tuple(my_tuple)}")
print(f"字符串转元组的结果是：{tuple(my_str)}")
print(f"集合转元组的结果是：{tuple(my_set)}")
print(f"字典转元组的结果是：{tuple(my_dict)}\n")

# 类型转换：容器转字符串
print(f"列表转字符串的结果是：{str(my_list)}")  # 直接转化为真字符串
print(f"元组转字符串的结果是：{str(my_tuple)}")
print(f"字符串转字符串的结果是：{str(my_str)}")
print(f"集合转字符串的结果是：{str(my_set)}")
print(f"字典转字符串的结果是：{str(my_dict)}\n")  # 把value也保留，变为字符串的一部分

# 类型转换：容器转集合
print(f"列表转集合的结果是：{set(my_list)}")
print(f"元组转集合的结果是：{set(my_tuple)}")
print(f"字符串转集合的结果是：{set(my_str)}")  # 集合数据无序
print(f"集合转集合的结果是：{set(my_set)}")
print(f"字典转集合的结果是：{set(my_dict)}\n")  # 集合数据无序

# 无法相互转为字典，因为缺少键值对

# 给容器排序
my_list = [3, 1, 2, 5, 4]
my_tuple = (1, 2, 5, 4, 3)
my_str = "agbcdfe"
my_set = {5, 2, 3, 4, 1}
my_dict = {"key2": 2, "key4": 4, "key1": 1, "key4": 4, "key5": 5}

# 正向排序
print(f"列表对象的排序结果：{sorted(my_list)}")
print(f"元组对象的排序结果：{sorted(my_tuple)}")
print(f"字符串对象的排序结果：{sorted(my_str)}")
print(f"集合对象的排序结果：{sorted(my_set)}")
print(f"字典对象的排序结果：{sorted(my_dict)}\n")

# 逆向排序
print(f"列表对象的排序结果：{sorted(my_list, reverse = True)}")
print(f"元组对象的排序结果：{sorted(my_tuple, reverse = True)}")
print(f"字符串对象的排序结果：{sorted(my_str, reverse = True)}")
print(f"集合对象的排序结果：{sorted(my_set, reverse = True)}")
print(f"字典对象的排序结果：{sorted(my_dict, reverse = True)}")