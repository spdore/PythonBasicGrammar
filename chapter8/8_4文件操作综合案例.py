"""
演示文件操作综合案例
"""

# 打开文件得到文件对象，准备读取
fr = open("chapter8/bili.txt", 'r', encoding = "UTF-8")

# 打开文件得到文件对象，准备写入
fw = open("chapter8/bili.txt.bak", 'w', encoding = "UTF-8")

# for循环读取文件
for line in fr:
    line = line.strip()
    # 判断内容，将符合条件的内容写入
    if line.split(",")[4] == "测试":  # 按照逗号分开，判断第四个元素是否为测试
        continue  # 为测试则跳过不写入
    fw.write(line)
    fw.write("\n")

# close两个文件对象
fr.close()
fw.close()