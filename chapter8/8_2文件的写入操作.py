"""
演示文件的写入
"""
import time

# 打开文件，不存在的文件
f = open("chapter8/test.txt", 'w', encoding = "UTF-8")

# write写入
f.write("Hello World！")

# flush刷新
#f.flush()

# close关闭
f.close()  # close方法内置flush功能

# 打开一个存在的文件
f = open("chapter8/test.txt", 'w', encoding = "UTF-8")  # 文件存在时，先清空再写入

# write写入，flush刷新
f.write("黑马程序员")

# close关闭
f.close()