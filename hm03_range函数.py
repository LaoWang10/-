# 获取1~9之间的整数:range() 在指定的范围内获取整数
# range(1,10)  --> [1,2,3,4,5,6,7,8,9]
# for 循环：在指定范围内循环做某个事情
# 语法：for 变量 in 容器:
# 容器：字符串，列表，元组，字典，集合，range函数
# for i in range(1,11):
#     print(i)

# 输出1~10的奇数的整数
# for i in range(1,11,2):
#     print(i)

# 初始值不写，默认从0开始,初始值可以不写,常常用于做计数器
# for i in range(11):
#     print(i)

# 打印10次：媳妇，我错了
# for i in range(10):
#     print("媳妇，我错了")


# # 计算1~100的累加和，使用for循环实现
# result = 0
# for i in range(1,101):
#     # print(i)
#     # 累加和
#     result = result + i
# print(result)

# 计算1~100的偶数累加和，使用for循环实现，通过两种方式实现
result = 0
for i in range(1,101):
    if i % 2 == 0:
        # 累加和
        result = result + i
print(result)