# 字符元素查询
str1 = 'abcdefg'
# # 打印第一个位置字符
# print(str1[0])
# # 打印最后一个位置字符
# print(str1[6])
# print(str1[-1])
# # 打印字符串长度
# print(len(str1))
# # 变量字符串
# for i in str1:
#     print(i)

# 通过字符找下标：字符串变量.find(字符)
print(str1.find('e'))
print(str1.find('x'))  # 元素不存在，返回-1

# 去除字符串前后的空格:字符串变量.strip()
# 定义字符串
str2 = " admin  "
print(str2)
print(str2.strip())

# 字符串大小写转换方法：字符串变量.upper()、字符串变量.lower()
str3 = " SELECT * FROM USERS;"
str4 = "delete from users;"
print(str3.lower().strip())
print(str4.upper())

# 判断字符串是否是数字或者字母：字符串变量.isdigit()、字符串变量.isalpha()
str5 = "123456"
str6 = "aaabbbcc"
print(str5.isdigit())  # 判断是否全数字
print(str6.isalpha())  # 判断是否全字母
# 统计某个字符出现次数：字符串变量.count(字符)
print(str6.count('a'))
print(str6.count('c'))

# 字符串的拆分：字符串变量.split(字符) --> 结果是列表
str7 = "select * from orders;"
# 判断上述语句是否是SQL查询 --> select
print(str7.split())  # ['select', '*', 'from', 'orders;']
print(str7.split("*"))  # 按照指定的字符拆分 --> ['select ', ' from orders;']
print(str7.split("from"))
# for循环变量
for i in str7.split():
    # print(i)
    if i == 'select':
        print("是SQL查询")
