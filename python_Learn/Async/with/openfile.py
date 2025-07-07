import os
folder_path = os.path.dirname(__file__)
print(folder_path)
# 注意 不管有几个/都会被看作一个/，很有趣
# 注意：いくつ「/」があっても一つの「/」として扱われる。面白い。
new_path=folder_path+'///////text.txt'
print(new_path)

# 不使用with的版本，需要手动打开，关闭  后面的参数是权限，r
# withを使わないバージョン。手動でopen/closeが必要。後ろの引数はモード（rは読み込み）。
# 其他权限有 'w'：只写—会清空原有内容，从头开始 'a'：追加写入-在文件末尾追加
# その他のモード：'w'：書き込み専用（開くと中身が消えて最初から書き込む） 'a'：追記専用（元の内容は消えず末尾に追加される）
file=open(new_path,'r')
text=file.read()
print(text)
file.close()

# 使用with的版本，自动关闭和释放
# withを使うバージョン。自動でcloseとリソース解放。
with open (new_path,'r') as file:
    print(file.read())