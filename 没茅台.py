for i in range(1,10):
   print()
   for j in range(1,i+1):
       print("%d*%d=%d"%(i,j,i*j),end="")

print('============================')
import math
def lsPrime(v):
    n=int(math.sqrt(v)+1)
    for l in range(2,n):
        if v%l==0:
            return'NO'
        else:
            return'Yes'
print(lsPrime(6))
print('------------------------')
list01=[1,1,6,3,1,5,2]
def duplicate(lists):
     L=[]
     for i in lists:
            if i not in L :
                  L.append(i)
     return L
print(duplicate(list01))
print("-------------------------")
from math import pi as Pl
def Circle(r):
    if isinstance(r,int)or isinstance(r,float):
        return Pl*r*r
    else:
        return("请给定数值型数据")
print(Circle(2))
print("-------------------------")
def fact(n):
    if n ==1:
       return 1
    return n*fact(n-1)
print(fact(4))
print("--------------------------")
sum1=0
sum2=0
for i in range(1,101):
    if i % 2 ==0:
          sum1=sum1 +i
    else:
        sum2=sum2+i
print("1-100之间偶数的和是:{},奇数的和是:{}".format(sum1,sum2))
print("-------------------------------")
pn = input('Please enter a number:')
i =0
j = len(pn)-1
flag = True
while i <=j:
    if pn[i]!=pn[j]:
          print('NO')
          flag=False
          break
    i,j = i+1,j-1
if flag:
    print('Yes')
print("---------------------------")
user=['redhat','westos']
passwd=['123','456']
for i in range(3):
    us = input('请输入用户名:')
    if us ==user[0]or us == user[1]:
          pa=input('请输入密码:')
          if us== user[0]:
              if pa==passwd[0]:
                    print('登录成功')
                    break
               else:
                   print('密码错误')
           if us == [1]:
               if pa ==passwd[1]:
                   print('登录成功')
                   brint
                else:
                    print('密码错误')
        
