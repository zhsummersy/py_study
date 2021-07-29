class A:
    aa=1
    bb=2
    def __init__(self,x,y):
        #把值传给实例self
        self.x=x
        self.y=y

a=A(7,8)
print(a.x,a.y,a.aa)
#aa是类的变量
#类.对象修改的是类里面的变量
#对象.属性修改的是对象里面的变量