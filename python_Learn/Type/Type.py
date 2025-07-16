from unittest import TestCase

# 这是正常的情况
# これは正常なケース

def add_numbers(x: int, y: int) -> int:
    '''
    # 返回两个整数的和
    # 2つの整数の和を返す
    '''
    return x + y
add_numbers(1, 2)

class Animal:
    '''
    # 动物类，包含一个叫喊方法
    # 動物クラス、Shoutメソッドを持つ
    '''
    def shout(self):
        print("oof")

def call_shout(animal: Animal):
    '''
    # 调用传入对象的shout方法
    # 渡されたオブジェクトのshoutメソッドを呼び出す
    '''
    animal.shout()

def call_shout_no_type(obj):
    '''
    # 调用传入对象的shout方法（无类型提示）
    # 渡されたオブジェクトのshoutメソッドを呼び出す（型ヒントなし）
    '''
    obj.shout()

my_animal = Animal()
call_shout(my_animal)
call_shout_no_type(my_animal)

# 类型提示示例
# 型ヒント例
number: int = 0
print(number)

wrong_type: int  
# 这会被类型检查工具警告,但是只要没出现问题python就不会管
# これは型チェックツールで警告されるが、問題が発生しなければPythonは気にしない

# wrong_type = "this is wrong type"  
# print(wrong_type)

# def WrongType(x:int , y:int):
#     print(x)
# WrongType("this is wrong type",1)

