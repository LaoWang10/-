words = "user=root,pwd=123456"

# 1. 以 , 为分隔符，使用split()切割，得到 ["user=root", "pwd=123456"]
list_data = words.split(',')
print(list_data)               #  ['user=root', 'pwd=123456']

# 2. 遍历列表，取出元素，以 = 为分隔符，使用split()切割 得到 ["user"， "root"]
for i in list_data:
    word_list = i.split('=')
    print(word_list)       #['user', 'root']   ['pwd', '123456']

    #3. 通过列表的取值来操作 索引操作 索引值 1
    word = word_list[1]
    print(word)

# 少小离家老大回,乡音无改鬓毛衰,儿童相见不相识,笑问客从何处来
# 少小离家老大回
# 乡音无改鬓毛衰
# 儿童相见不相识
# 笑问客从何处来
# str="少小离家老大回,乡音无改鬓毛衰,儿童相见不相识,笑问客从何处来"
# list=[]
# for i in str.split(','):
#     list=i
#     print(list)
