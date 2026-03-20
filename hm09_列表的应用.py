# 1.列表元素查询： 列表名[索引]
list1 = ["张三", 22, 1.85]
# 查询下标为2的元素
print(list1[2])
# print(list1[3])  # 越界报错
list2 = [11, 22, 33, 22, "a"]
# 统计元素出现的次数：变量名.count(元素)
print(list2.count(22))  # 2
print(list2.count('a'))  # 1
print(list2.count('x'))  # 0

# 列表元素的增删改
# 2.新增：列表名.append(元素)   每次在列表末尾添加一个元素
list3 = []
list3.append(1)
list3.append(2)
# 查看最后结果
print(list3)  # [1,2]
# 指定位置添加：列表名.insert(索引, 元素)
list3.insert(1, 3)
print(list3)  # [1,3,2]

# 3.修改：列表名[索引] = 元素
list3[1] = "a"
print(list3)  # [1, 'a', 2]
# 4.指定位置删除：列表名.pop(索引)   删除指定索引的元素，并返回该元素
list3.pop(1)
print(list3)  # [1, 2]
# 指定元素删除：列表名.remove(元素)
list3.remove(1)
print(list3)

# 列表的合并：列表名1 + 列表名2
list4 = [1, 2, 3]
list5 = [4, 5, 6]
print(list4 + list5)

# 列表的排序：list.sort()  # 升序可以默认不写，降序指定reverse=True
list6 = [1, 5, 3, 2, 4]
list6.sort()
print(list6)
list6.sort(reverse=True)
print(list6)

# 列表中的元素还是列表：列表嵌套
student_list = [
    ["张三", "18", "功能测试"],
    ["李四", "20", "自动化测试"],
    ["王五", "22", ["python", "java"]]
]
# 获取姓名：张三
print(student_list[0][0])
# 获取java：java
print(student_list[2][2][1])
