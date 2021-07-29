# class A:
#     def __init__(self):
#         print('A')
# class B(A):
#     def __init__(self):
#         print('B')
#         super().__init__()#调用父类的方法

# if __name__=="__main__":       
#     b=B()

#try except finally
#finally通常用来做资源释放，因为无论无何都会调用它
#如果finally中有return语句，那么会调用finally中的return语句
#否则会调用之前的

#上下文管理器
# from _typeshed import Self


# class Sample:
#     def __enter__(self):
#         print ("enter")
#         #获取资源
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         #释放资源
#         print ("exit")
#     def do_something(self):
#         print ("doing something")

# with Sample() as sample:
#     sample.do_something()