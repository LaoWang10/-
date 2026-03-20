# 示例：从1~10之间随机的获取一个整数
# 导包
# import random
# 调用方法获取一个随机数
# print(random.randint(1, 10))

# 石头剪刀布
# 分析：
# 让电脑和人一样能听懂 并且能够玩耍 --> 转数字
# 定义两个角色：人、电脑
# 出拳：1、石头 2、剪刀 3、布
# 结果：平局 电脑赢 人赢
# 输赢：电脑赢-->
# 电脑：1石头  人：2剪刀
# 电脑：2剪刀  人：3布
# 电脑：3布    人：1石头

import random
# 定义变量
computer = random.randint(1, 3)
player = int(input("请输入数字(1~3)："))
# 判断
if player == computer:
    print("平局")
# 电脑出的是1人出的2的情况下，电脑赢；...
elif (computer == 1 and player == 2) or (computer == 2 and player == 3) or (computer == 3 and player == 1):
    print("电脑赢")
else:
    print("人赢")
