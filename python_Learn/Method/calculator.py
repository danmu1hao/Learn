# 计算器类 / 計算機クラス
class Calculator:
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mul(self, a, b):
        return a * b
    def div(self, a, b):
        if b == 0:
            return '除数不能为0 / 0で割ることはできません'
        return a / b

# 计算方法执行函数 / 計算メソッドを実行する関数
def calculate(func, a, b):
    return func(a, b)

# 用户输入 / ユーザー入力
try:
    x = float(input("1つ目の数字を入力してください: ")) 
    y = float(input("2つ目の数字を入力してください: "))  
    op = input("演算子を選んでください (+, -, *, /): ") 
except Exception as e:
    print("入力エラー / 输入错误:", e)
    exit()

calc = Calculator()

# 运算符到方法的映射 / 演算子とメソッドの対応
ops = {
    '+': calc.add,
    '-': calc.sub,
    '*': calc.mul,
    '/': calc.div
}

if op in ops:
    result = calculate(ops[op], x, y)
    print(f"結果: {result}")  
else:
    print("無効な演算子です / 运算符无效")