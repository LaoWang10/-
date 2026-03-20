# 计算1~100的累加和
# 人工：1+2+3+...+100=5050

# 分析：求和动作重复 --> 循环
# 0+1 = 1
# 1+2 = 3
# 3+3 = 6
# 6+4 = 10
# 10+5 = 15
# ...
# 上一次结果 + 100 = 最终结果
# 上一次结果 + 计数器 = 最终结果
# 上一次结果初始值0
# 最终结果就是上一次结果，看循环次数
# 定义变量
# result = 0
# result + count = result
# result = result + count

# while步骤：
# 1.定义计数器
count = 1
# 计算结果的初始值
result = 0
# 2.设置循环条件
while count <= 100:
    # 3.编写循环代码
    result += count
    # 4.修改计数器
    count += 1
# 5.输出结果
print(result)


# 计算1~100的偶数的累加和
# 1.定义计数器
count = 1
# 计算结果的初始值
result = 0
# 2.设置循环条件
while count <= 100:
    # 判断是偶数
    if count % 2 == 0:
        # 3.编写循环代码
        result += count
    # 4.修改计数器
    count += 1
# 5.输出结果
print(result)