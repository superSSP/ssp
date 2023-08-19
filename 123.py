num = int(input("请输入一个三位正整数:"))
a = str(num)[0]
b = str(num)[1]
c = str(num)[2]
if a>b:
    if a>c:
        max_num = a
    else:
        max_num = c
else:
    if b>c:
        max_num=b
    else:
        max_num =c
print(num,"中最大的数字是:",max_num)
num = int(input("请输入一个三位正整数:"))
a = str(num)[0]
b = str(num)[1]
c = str(num)[2]
if a>b and a>c:
    max_num =a
if b>a and b>c:
    max_num =b
if c>a and c>b:
    max_num = c
print(num,"中最大的数字是:",max_num)
print("\n中国酒城·最美泸州 四川省泸州市欢迎您!\n")
print("美酒虽好·请不要贪杯哦!为了您和他人的安全,严禁酒后驾车!\n")
proof = int(input("请输入驾驶员没100mL血液的酒精含量:"))
if proof<20:
    print("\n您还不构成饮酒行为,可以开车,但要注意安全!")
else:
    if 80>proof>=20:
     print("\n已经达到酒后驾车标准,请不要开车!")
    else:
         print("\n已经达到醉酒驾车标准,千万不要驾车!")
print("-----------------------------")
sale = 6000
if sale <=5000:
    print("无提成")
elif sale<=10000:
    print("最高提成10%")
elif sale <=50000:
    print("最后提成20%")
else:
    print("最高提成20%")
