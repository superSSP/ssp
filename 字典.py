pty={'猪小明':'18384978921','球球':'13864532670','米线儿':'17726567780'}
print(pty)
name=['球球','冷檬','米线儿','小美']
sign=['白羊座','射手座','双鱼座','双子座']
pty= dict(zip(name,sign))
print(pty)
d1={'Name':'xiaoming','Age':7,'Class':'First'}
print(d1['Name'])
print(d1['Age'])
prt=dict((('球球','白羊座'),('柠檬','射手座'),('米线儿','双鱼座'),('小美','双子座')))
prt["婷婷"]="巨蟹座"
print(prt)
prt["柠檬"]="水瓶座"
print(prt)
pty={'球球':'白羊座','柠檬':'射手座','米线儿':'双鱼座','小美':'双子座'}
print("小美的星座是:",pty.get('小美'))
print("小明的星座是:",pty.get('小明'))
print("\n===四川泸天化股份有限公司研发部员工信息管理===")
print("操作指令; i 增加 r 删除 c 修改 s 查找")
staff={'Y20180053':'猪小明,男,27岁,大学本科学历',
       'Y20180089':'毛台,男,45岁,大学专科学历',
       'Y20190020':'球球,女,25岁,大学本科学历',
       'Y20170078':'冷檬,女,22岁,大学专科学历',
       'Y20120023':'闰土,男,38岁,大学本科学历',
       'Y20110090':'陈翔,男,32岁,硕士研究生学历',
       'Y20080120':'米线儿,女,22岁,大学专科学历',
       'Y20100003':'小美,女,26岁,大学本科学历'}
end='y'
operC='n'
while end=='y'or end=='Y':
    print("请输入相关操作:",end="")
    operC=input( )
    if str(operC)=='i'
           print("请输入新增加员工工号:",end="")
           iNo=input( )
           if str(iNo) in staff:
               print("该工号已存在,添加失败！")
            else:
                print("请输入新增加员工信息:",end="")
                iInfo=input( )
                staff[]
