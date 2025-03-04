num = int(input("请输入第一次猜想的数字："))

if num == 10:
    print("恭喜你猜对了")
elif int(input("猜错了，再猜一次：")) == 10:
    print("你猜对了")
elif int(input("猜错了，最后猜一次：")) == 10:
    print("猜对了")
else:
    print("Sorry，猜错了。")