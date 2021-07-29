# #b和byte类型的转换
# c='hello,晖'
# d=c.encode('utf-8')#编码
# print(d,type(d))
# print(d.decode('utf-8'))#解码

# from _typeshed import Self


# from _typeshed import Self

# 类
# class Person(object):
#     name='晖晖'
#     def dump(self):
#         # print(f'{self.name}is dumping')
#         #格式化数据
#         print(f'{self.name} is dumping')
# hui=Person()
# print(hui.name)
# hui.dump()

# self是必传参数，是类的实例，必须放在第一个位置


# class Test(object):
#     #构造函数
#     def __init__(self,a):
#         self.a=a
#     def run(self):
#         print(self.a)

# t=Test(3123)
# t.run()

# class Person():
#     def __init__(self,name='',sex='',age=''):
#         self.name=name
#         self.sex=sex
#         self.age=age
#         print('我的名字是'+name+',我今年'+age+'岁了,'+'我是'+sex+'生')

# #定义的函数要有self，不然会报错
#     def sayhello(self):
#         print('hello!')
#         return print

# ming=Person(name='zh',sex='男',age='20')
# ming.sayhello()

# 实例不能调用私有函数
# 但是可以用首字符大写的方法调用


#装饰器
# def check_str(func):
#     def inner(*args, **kargs):
#         result = func(*args, **kargs)
#         if result=='ok':
#             return 'result is %s'% result
#         else:
#             return 'result is faild:%s'% result
#     return inner
#
# @check_str
# def test(data):
#     return data
#
# result=test('no')
# print(result)



#数据库通过redo,undo日志文件来完成事务操作
#ACID
 #事务的原子性。事务执行后，要么成功，要么失败，不会停留在中间
 #事务的一致性。事务执行后，保证结果一致，不会歧义
 #事务的隔离性。事务内的数据不受其他数据影响。
 #事务的持久性。事务提交后，可以靠日志来完成事务的持久化。

 #mysql默认事务级别是查询不受其他事务的影响


# 数据库部分
# import mysql.connector
# con=mysql.connector.connect(
#     host='localhost',port='3306',
#     user='root',password='573624517',
#     database='demo',
# );
# con.close()
# ctrl+shift+f10调试
# mysql利用游标cursor执行sql语句
# c=con.cursor()
# sql='SELECT empno,ename,hiredate FROM t_emp;'
# c.execute(sql)
# for one in c:
#     print(one[0],one[1],one[2])

# sql预编译机制抵御sql注入攻击
# 异常处理，使用try语句去捕获异常
# 网络链接对数据库的开销最大，因为使用了TCP三次握手
# 数据库连接池，预先创建出一些数据库链接，然后缓存起来，避免程序语言反复查询

# 装饰器
# classmethod 可以不用实例化对象 执行类里面的函数

class Test(object):
    @classmethod
    def add(cls,a,b):
        return a+b
Test.add(2,2)


















