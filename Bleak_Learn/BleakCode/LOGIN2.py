class test:
    __name__ = "sd"
    a = 10
    
    def __repr__(self):
        return f"test(name={self.__name__}, a={self.a})"

# 实例化后打印对象
t = test()
print(t)  # 输出: test(name=sd, a=10)