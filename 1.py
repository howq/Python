print(100+200+300)
print('hello world')
print('你好')
print('是吗？','好的','hello')
print('100+200=',100+200)

# name = input()
# print('输入的参数：',name)

a='ABC'
b=a
a='XYZ'
print(a)
print(b)

PI=3.141592653
print(PI)

# list
classmate = ['Michael','Bob','Tracy']
print(classmate,len(classmate),classmate[0],classmate[1])
print(classmate[-1])
classmate.insert(1,'jack')
classmate.pop(2)
classmate[1]=True
classmate[2]=98
print(classmate)

L=[]
print(len(L))

# tuple
myclassmate = ('Michael','Bob','Tracy')
print(myclassmate)

bigger = ('niky','James','Mikey',['m',True,90])
print(bigger)
bigger[3][0]='mm'
bigger[3].pop()
bigger[3].insert(1,'dd')
bigger[3].append('last')
print(bigger)

# 条件判断
# s = input('birth:')
# birth = int(s)
# if birth<2000:
#     print('00前')
# else:
#     print('00后')
#
# sal = input('我的工资:')
# salary = int(sal)
# if salary>=10000:
#     print('高薪')
# elif salary>5000:
#     print('一般')
# else:
#     print('快哭了')

# 循环
names = ['james','niky','whiy']
for name in names:
    print(name)

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

print(list(range(5)))


sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum=0
n=99
while n>0:
    sum = sum + n
    n = n - 2
print(sum)

myNames = ['Bart','Lisa','Adam']
for name in myNames:
    print('hello%s'%(name))

# dict
dictionary = {'Midk':90,'Bob':34,'Track':23}
for key in dictionary.keys():
    print(dictionary[key])

# set
s = set([1,2,3])
s.add(4)
s.remove(1)
print(s)

# 函数
abs(-30)
min(6,5,2)


def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    if x>0:
        return x
    else:
        return -x
m = my_abs(-9)
print(m)

# from 文件名 import 函数名

# pass的使用
def nop():
    pass

z=89
if z>90:
    pass

# 参数检查
# my_abs('m')

# 返回多个值

import math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny

r=move(100,100,60,math.pi/6)
print(r)

# 函数的参数
def pow(x):
    return x*x;

def my_pow(x,n):
    s=1
    while n>0:
        n = n-1
        s = s*x
    return s

m2 = my_pow(5,2)
m3 = my_pow(5,3)

print(m2)
print(m3)

# 默认参数
def more_pow(x,n=2):
    s = 1
    while n>0:
        n = n-1
        s = s*x
    return s

print(more_pow(3))
print(more_pow(3,4))

def add_end_old(L=[]):
    L.append('END')
    return L

def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L

print(add_end([1,2,3]))

print(add_end())
print(add_end())

print(add_end([1,2,3]))


# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

print(calc(1,2,3))
print(calc())

nums=[1,2,3,4]
print(calc(*nums))

# 关键字参数

def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

person('Michael',30)
person('Michael',30,city='beijing',province='siir')

extra={'city':'Beijing','Job':'Engneer','book':'china is the world'}

person('Michael',80,city=extra['city'],Job=extra['Job'])
person('Joson',90,**extra)

# 命名关键字参数
def person_new(name,age,**kw):
    if 'city' in kw:
        pass
    if 'Job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)

person_new('Jicky',77,**extra)

# 参数组合<!----------nd------------>
def f1(a,b,c=0,*args,**kw):
    print('a:',a,'b:',b,'c=:',c,'args=',args,'kw=',kw)

def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',city='jiangsu')
f2(1,2,98,d=0,data='nihk')

