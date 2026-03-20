# 吃苹果，吃5个
count = 1
while count <= 5:
    print(f"吃了第{count}个苹果")
    # 第三个就吃饱
    if count == 3:
        print("吃饱了")
        break  # 结束循环
    count += 1
