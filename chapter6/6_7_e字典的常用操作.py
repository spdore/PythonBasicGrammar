stuff_dict = {
    "王力宏": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    "周杰伦": {
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    },
    "林俊杰": {
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    },
    "张学友": {
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },
    "刘德华": {
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    },
}

print(f"全体员工信息如下：\n{stuff_dict}")

for name in stuff_dict:
    if stuff_dict[name]["级别"] == 1:
        stuff_dict[name]["级别"] += 1
        stuff_dict[name]["工资"] += 1000

print(f"全体员工级别为1的员工完成升职加薪操作，操作后:\n{stuff_dict}")