import string
name = input("お名前を入力してください: ")  
print(f"こんにちは, {name}さん！")  
# 文字之间可以互相相加
# 文字列同士は連結できる
print(name+str(12345))
try:
    number = input("数字を入力してください: ") 
    print("あなたの数字の10倍は " + str(10 * int(number))) 
except ValueError:
    print("有効な数字を入力してください。") 

