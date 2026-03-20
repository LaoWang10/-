# 登录需求：
# 用户输入手机号、密码、验证码
# 对于输入的手机号、密码、验证码去除两端空格
phone = input("请输入手机号：").strip()
password = input("请输入密码：").strip()
code = input("请输入验证码：").strip()
# 手机号为空时，提示“手机号不能为空”
if phone == "":
    pass
# if phone is not None:  #  if 条件成立时，才执行print语句;python中空值即为假
if not phone:  # if 条件成立时，才执行print语句
    print("手机号不能为空")
# 密码为空时，提示“密码不能为空”
if not password:
    print("密码不能为空")
# 验证码为空时，提示“验证码不能为空”
if not code:
    print("验证码不能为空")
# 手机号格式不正确时，提示"手机号格式错误，请输入11位数字"
if len(phone) == 11 and phone.isdigit():
    print("手机号格式正确")
else:
    print("手机号格式错误，请输入11位数字")
# 验证码统一转换为小写进行判断，正确验证码为"8888"，验证码错误、提示"验证码与图片内容不一致"
if code.lower() == "8888":
    print("验证码正确")
else:
    print("验证码与图片内容不一致")
# 正确手机号为"13488888888"，手机号错误时，提示"手机号不存在"
# 正确密码为"123456"，密码错误时，提示"密码与账号不匹配"
# 手机号为"13488888888"、密码为"123456"、验证码为”8888”时，输出“登录成功”
if phone == "13488888888" and password == "123456" and code.lower() == "8888":
    print("登录成功")
elif phone != "13488888888":
    print("手机号不存在")
elif password != "123456":
    print("密码与账号不匹配")


