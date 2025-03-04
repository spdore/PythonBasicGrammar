import random
num = random.randint(1,10)
guess= int(input("请输入你猜的数字："))

if guess == num:
    print("恭喜你，猜对了。")
elif guess > num:
    guess = int(input("你猜的大了，请重新猜："))

    if guess == num:
        print("恭喜你，猜对了。")
    elif guess > num:
        guess = int(input("你猜的大了，请重新猜："))

        if guess == num:
            print("恭喜你，猜对了。")
        else:
            print = int(input("你猜错了"))

    else:
        guess = int(input("你猜的小了，请重新猜："))

        if guess == num:
            print("恭喜你，猜对了。")
        else:
            print = int(input("你猜错了"))

else:
    guess = int(input("你猜的小了，请重新猜："))
    
    if guess == num:
        print("恭喜你，猜对了。")
    elif guess > num:
        guess = int(input("你猜的大了，请重新猜："))

        if guess == num:
            print("恭喜你，猜对了。")
        else:
            print = int(input("你猜错了"))
    
    else:
        guess = int(input("你猜的小了，请重新猜："))

        if guess == num:
            print("恭喜你，猜对了。")
        else:
            print = int(input("你猜错了"))