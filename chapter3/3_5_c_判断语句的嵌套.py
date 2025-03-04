"""
演示判断语句的嵌套
"""

# if int(input("您的身高是多少：")) > 120:
#     print("身高超出限制不能免费。")
#     print("但是vip等级大于3就可以免费。")

#     if int(input("你的vip级别是多少：")) > 3:
#         print("恭喜你vip等级达标，可以免费。")
#     else:
#         print("Sorry你需要买票10元。")
    
# else:
#     print("欢迎你，小朋友。")

age = 20
year = 1
level = 5

if age >= 18:
    print("你是成年人")

    if age < 30:
        print("您的年龄达标了")
        if year > 2:
            print("恭喜你，年龄和入职时间都达标，可以领取礼物。")
        elif level > 3:
            print("恭喜你，年龄和级别都达标，可以领取礼物。")
        else:
            print("不好意思，尽管年龄达标，但是入职时间和级别都不达标。")
    else:
        print("不好意思，年龄太大了。")
    
else:
    print("不好意思，小朋友不能领取礼物哦。")