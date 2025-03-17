text = "itheima itcast boxuegu"
count_it = text.count("it")
new_text = text.replace(" ", "|")
new_text_list = new_text.split("|")
print(f"字符串{text}中有：{count_it}个it字符")
print(f"字符串{text}，被替换空格后，结果{new_text}")
print(f"字符串{new_text}，按照|分隔后，得到{new_text_list}")