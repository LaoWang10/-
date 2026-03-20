# 猜数字:提高题最后一题

# 导包：必须放在最上面
import random
num = random.randint(0, 10)
# print(num)

# 1.定义计数器
count = 1
# 2.设置循环条件
while True:
    # 3.编写循环代码
    num1 = int(input("请输入数字："))
    if num1 > num:
        print("猜大了")
    elif num1 < num:
        print("猜小了")
    else:
        print(f"猜对了,猜了{count}次")
        # 结束循环
        break
    # 4.修改计数器
    count += 1
