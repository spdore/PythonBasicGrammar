"""
演示对文件的读取
"""
import time

# 打开文件
# f = open("/Users/spdor/Desktop/CodeSpace/Python/chapter8/测试.txt", "r", encoding = "UTF-8")  # encoding的顺序不是第三位，不能使用位置传参
# print(f"{type(f)}")

# 读取文件 - read()
#print(f"读取10个字节的结果是:\n{f.read(10)}")
#print(f"read方法读取全部内容的结果是:\n{f.read()}\n")  # 不是从头开始，而是继续读取

# 读取文件 - readlines()
#lines = f.readlines()  # 读取文件的全部行，封装到列表中
#print(f"lines对象的类型是：{type(lines)}")
#print(f"lines对象的结果是：{lines}")  # 还读取了特殊字符“\n”

# # 读取文件 - readline()
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行的数据是{line1}")
# print(f"第一行的数据是{line2}")
# print(f"第一行的数据是{line3}")
# print("---------------------------\n")

# # for循环读取文件行
# for line in f:
#     print(f"每一行数据：{line}")

# # 文件的关闭
# #time.sleep(500000)
# f.close()  # 停止文件的占用

# with open 语法操作文件
with open("/Users/spdor/Desktop/CodeSpace/Python/chapter8/测试.txt", "r", encoding = "UTF-8") as f:
    for line in f:
        print(f"文件的每一行是{line}")

time.sleep(500)