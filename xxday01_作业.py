# 减肥计划
# 用户输入数据
# 判断
weight = float(input("请输入体重："))
# 先判断体重范围是否合适
if 0 < weight < 500:
    # print("体重正常")
    # 在判断体重在合理范围内减肥计划
    if weight <= 40:
        print("停止减肥")
    elif 40 < weight <= 45:
        print("每天晨跑30分钟")
    elif 45 < weight <= 50:
        print("健身房1小时")
    elif 50 < weight <= 60:
        print("健身房2小时")
    elif 60 < weight <= 80:
        print("健身房3小时")
    elif 80 < weight:
        print("爱咋咋地")
else:
    print("请输入正确的体重")
