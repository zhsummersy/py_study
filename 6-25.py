#函数的参数
#加了*号的会以元组的形式存入
# def printinfo(arg1,**arg2):
#     print('输出')
#     print(arg1)
#     print(arg2)
# printinfo(10,a=10,b=30)
#第一个参数是10,所以打印10，后面是不定长参数

##加了两个*号的会以字典的形式传入参数

#lambda表达式
#可以便捷使用表达式和参数
# sum=lambda arg1,arg2:arg1+arg2
# sub=lambda arg1,arg2:arg1*arg2

# print('sum=',sum(10,20))
# print('sub=',sub(20,30))

#遍历range
# for i in range(11):
#     print(i)

# for i in range(3):
#     print(i)

# a=['jack','mary','mark','jack']
# print(a)
# #列表可以重复
# b={'jack','mary','mark','jack'}
# #集合不重复
# x=set(b)
# print(b)
# print(x)
# b=set(a)
# if(a == b):
#     print('true')
# else:
#     print('false')


# a=['mary','jack','zh','cd']
# for i in range(len(a)):
#     print(i,a[i])
#迭代链表索引

#可迭代的意思是从某种东西中可以连续项到结束
#for也是一个迭代器


# def f(a,L=[]):
#     L.append(a)
#     return L
# print(f(1))
# print(f(1))
# print(f(1))
# print(f(1))
# #输出三角形

# def f(a,L=None):
#     if L is None:
#         L=[]
#     L.append(a)
#     return L
# #如果没有给列表L赋值，那么它就为空
# print(f(1))
# print(f(1))
# print(f(1))
# print(f(1))

#函数的参数要按照顺序给，没有给定形参的要给它接收参数，
#不要换顺序，避免出错
#可变 参数是参数列表中的最后一个，
#因为它们将把所有的剩余输入参数传递给函数

# def concat(*args,sep='/'):
#     return sep.join(args)
# l1=concat('a','b','c','d')
# l2=concat('a','b','c','d',sep='.')
# print(l1)
# print(l2)
#可变参数列表再看看

# from typing import List


# a=list(range(3,6))
# #列表不能迭代
# for i in a:
#     print(i)

# args=[3,6]
# j=list(range(*args))
# for i in j:
#     print(i)

# fun=lambda x:x+1
# f=fun(42)
# print(f)

# list_two=[7,8]
# list_one=[1,2,3,4,5,1]
# list_one.append('x')#结尾加一个元素
# list_one.extend(list_two)#把整个列表都加就去
# list_one.insert(0,'x')#指定位置插入元素
# list_one.pop()#没有参数则删除最后一个元素
# list_one.pop(0)#指定删除元素
# list_one.clear()#删除所有元素
# count=list_one.count(1)#返回元素出现次数
# index=list_one.index(1)
# list_one.sort()#对元素进行排序,只能是数字
# list_one.reverse()#倒排元素
# print(list_one)
# print(list_one)
# print(index)#只能返回第一个，后面还有都返回不了
# print(count)

#列表推导：
# squares=[]
# for x in range(10):
#     squares.append(x**2)
# print(squares)

# name={'name1':'jack','name2':'mark','name3':'boby','name4':'zh'}
# # for i,j in name.items():
# #     print(i,j)
# # #循环输出字典的元素

# for i,j in enumerate(name):
#     print(i,j)
# #得到索引位置的对应值

# words=['a','b','c','d']
# for w in words[:]:
#     if len(w)>0:
#         words.insert(0,w)
# print(words)
# #输出对称的列表

# import sys
# print(dir(sys))

# import time
# #strp字符串转日期
# time_obj=time.strptime('2021-7-28','%Y-%m-%d')
# print(time_obj)

# #把日期转字符串
# time_obj2=time.strftime('%Y-%m-%d',time.localtime())
# print(time_obj2)


# import os
# current_path=os.getcwd()#获取当前路径

#类型转换 很重要
# 直接使用str int float 来转换
sort_str='a b b d e f g c'
# sort_list=sort_str.split(' ')#转换成列表
# print(sort_list)
# sort_str=' '.join(sort_list)
# print(sort_str)

sort_new=sorted(sort_str)
print(sort_new)#把字符串排序