# 三角形判断

# 输入三边
a = float(input("请输入三角形的边a："))
b = float(input("请输入三角形的边b："))
c = float(input("请输入三角形的边c："))
# 判断三角形
if a + b > c and a + c > b and b + c > a:
    print("是三角形")
    # 进一步判断:越特殊越靠前
    if a == b == c:
        print("等边三角形")
    elif a == b or a == c or b == c:
        print("等腰三角形")
    else:
        print("普通三角形")
else:
    print("不是三角形")