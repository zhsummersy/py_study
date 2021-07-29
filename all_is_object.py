def ask(name='zh'):
    print(name)

class person:
    def __init__(self):
        print('zh1')

#调用ask函数
ask()

#实例化对象
my_person=person()
my_person

#装饰器可以返回函数
def decorator_func():
    print('dec start')
    return ask
my_ask=decorator_func() 
# 装饰器要带括号
my_ask()