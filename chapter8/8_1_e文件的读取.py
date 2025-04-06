# 方法1
f = open("/Users/spdor/Desktop/CodeSpace/Python/chapter8/word.txt", 'r', encoding = "UTF-8")
# content = f.read()
# count = content.count("itheima")
# print(f"itheima的个数是{count}")

# 方法2
count = 0

for line in f:
    line = line.strip()  # 取出开头与结尾的空格与换行符
    words = line.split(" ")
    for word in words:
        if word == "itheima":
            count += 1

print(f"itheima的个数是{count}")

f.close()