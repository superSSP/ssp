set1 = {'水瓶座','射手座','双鱼座','双子座'}
set2 = {3,1,4,1,5,8,2,6}
set3 = {'泸州老窖',1573,('醉美泸州','欢迎您')}
print(set1)
print(set2)
print(set3)
print('........................')
qq={'球球','猪小明','闰土','冷萌'}
print('选择python语言的学生有:',qq,'\n')
c = {'米线儿','茅台','婷婷','小妹'}
print('选择c语言的学生有:',c)

print("........................")
set1=set("雪花飘飘,北风萧萧,天地一片茫茫")
set2=set([1,2,3,4])
set3=set(('醉美泸州','欢迎您的到来'))
print(set1)
print(set2)
print(set3)

print('.....................')
mr= set(['泸州老窖','贵州茅台','古井贡酒','衡水老白干','五粮液'])
mr.add('剑南春')
print(mr)
print('...........................')
mr=set(['泸州老叫','贵州茅台','古井贡酒','喝水老板干','五粮液','剑南春'])
mr.remove('古井贡酒')
print('使用removr()方法移除制定元素后:',mr)
mr.pop()
print('使用pop()方法移除一个元素后:',mr)
mr.clear()
print('使用cleat()方法清空集合后:',mr)

qq = set(['球球','小明','闰土','冷萌'])
qq.add('婷婷')
print('选择python语言的学生有:',qq,'\n')
c =set(['米线儿','茅台','婷婷','小妹'])
c.remove('婷婷')
print('选择c语言的学生有:',c)
qq = set(['球球','猪小明','婷婷','闰土','冷萌'])
c = set(['米线儿','猪小明','茅台','婷婷','小妹'])
print('选择ptyhon语言的学生有:',qq)
print('选择c语言的学生有:',c)
print('交集运算:',qq&c)
print('并集运算:',qq|c)
print('差集运算:',qq-c)
print("\n===白酒专卖店经销商和白酒品牌的故事===")
qq_set = {'球球','毛台','猪小明','小路','米线儿'}
ww_set = {'翔子','吴妈','冷萌','闰土'}
ee_set = {'妹爷','米线儿','小野','闰土'}
print("泸州老窖在河北授权的白酒专卖店经销商名单:")
print(qq_set)
print("五粮液在河北授权的白酒专卖店经销商名单:")
print(ww_set)
print("剑南春在河北授权的白酒专卖店经销商名单")
print(ee_set)
print('同事获得泸州老将和五粮液两个白酒品牌的专卖店经销商有:',qq_set&ww_set)
print('同事获得泸州老将和剑南春两个白酒品牌的专卖店经销商有:',qq_set&ee_set)
print('同事获得五粮液和剑南春两个白酒品牌的专卖店经销商有:',ww_set&ee_set)
ww_set.add('王炸')
print("河北现有五粮液授权的白酒专卖店经销上名单:")
print(ww_set)
ee_set.remove('妹爷')
print("河北现有剑南春授权的白酒专卖店经销商名单:")
print(ee_set)
