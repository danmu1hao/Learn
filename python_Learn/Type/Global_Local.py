import glob
import math

def Add_One_Local(math : int):
    # 局部变量使用固有词也没事
    # ローカル変数で組み込み名を使っても問題ない
    math+=1

int_x=1
Add_One_Local(int_x)
# 依旧是1
# それでも1のまま
print(int_x)

def Add_One_Global(target):
    # 这只是把target变成全局变量然后修改，而不是修改了传入的参数的地址的对应变量
    # これは単にtargetをグローバル変数にして変更しているだけで、渡された引数のアドレスが指す変数自体を変更しているわけではない
    global targe 
    target+=1

    #定义全局变量和外界同步，但是难以维护
    # グローバル変数として外部と同期できるが、管理が難しい
    global int_x
    int_x+=1

def Add_One_Normal(target):
    return target+1

int_x=Add_One_Normal(int_x)
print(int_x)