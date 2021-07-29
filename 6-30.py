#继续巩固基础知识
#变量赋值：
#从左到右依次赋值
# a,b,c=1,2,3
# print(a,b,c)

# 数字、字符串、列表、元组、集合、字典
#其中，列表、集合、字典可变，其他不可变

#isinstance type 
#type不会认为子类是一种父类型
# class A:
#     pass
# class B(A):
#     pass

# print(isinstance(A(),A))
# print(type(B())==A)

# l1='zhsummersyyyyyyyyyyyyyyy'
# l2='上面是一个字符串'
# print(type(l1))
# l3=set(l1)#set可以去重复对象
# print(l3)

#关于切片，左闭右开
# list=['z','h','s','u','m','m','s','y']
# print(list[0:3])#zhs
# print(list[:-1])#逆向
# print(list[-1])#输出最后一个
# print(list[-5:-1])#也还是左边往右边数
# print(list[3:])#第4个到最后一个
# print(list[-1::-1])#翻转字符

#元组不可修改
#set不可重复
# s1=set()#声明空的集合，集合可以去重复

# #字典——键值对 name:value
# dic={
#     'name':'姓名','sex':'性别','age':'年龄'
# }
# print(dic)#输出字典
# dic['name']='修改后的姓名'
# print(dic)

#迭代器和生成器
#概念：迭代器是可以记住遍历位置的对象 基本方法：iter()、next()
# list=[1,2,3,4]
# it=iter(list)#创建迭代器
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# for i in it:
#     print(next(it))#会输出2和4——间隔是1
#同一对象的迭代器不能同时使用
# for i in it:
#     print(i,end=' ')
# import sys
# list=[5,6,7,8]
# it=iter(list)#创建迭代器

# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()
# #出现问题之前，一直迭代下去

#使用yield的函数是生成器
#生成器是返回迭代器的函数，只能用户迭代操作

#变量没有类型，只是一个指向对象的指针

#lambda表达式 匿名函数
# sum=lambda arg1,arg2:arg1+arg2
#lambda [arg1 [,arg2,.....argn]]:expression
#表达式可以做出很多花样
#每个模块都有一个__name__属性，当其值是'__main__'时
# 表明该模块自身在运行，否则是被引入。

# class complex:
#     #实例化对象
#     def __init__(self,realpart,imagepart):
#         #构造函数
#         self.r=realpart
#         self.i=imagepart
# x=complex(7,8)
# print(x.r,x.i)

#方法重写
# class A:
#     def method1(self):
#         print('方法1')
# class B(A):
#     #重写了父类A的方法1
#     def method1(self):
#         print('方法2')
# a=A()#实例化对象
# a.method1()
# b=B()
# b.method1()
