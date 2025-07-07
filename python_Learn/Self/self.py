
class A:
    def hello(self, name):
        print("Hello,", name)

def call_func(func, obj, arg):
    func(obj, arg)

a = A()
call_func(A.hello, a, "Python")  # 直接把类的方法和对象传进去