print("欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！")

def check(temperature):
    if temperature <= 37.5:
        print(f"体温测量中，您的体温是：{temperature}，体温正常请进！")
    else:
        print(f"体温测量中，您的体温是：{temperature}，需要隔离！")

check(36)
check(38.6)