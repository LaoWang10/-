# 字符串：使用引号包裹的数据信息
# 空字符串
info = ""
# 非空字符串
info1 = "hello world"
# 使用方法
# 1.查询字符串中某个字符：变量名[下标]
print(info1[6])
print(info1[4])
# 如果下标越界（不存在），程序会报错
# print(info1[12])
# 2.查看字符串长度：len(变量名)
print(len(info1))