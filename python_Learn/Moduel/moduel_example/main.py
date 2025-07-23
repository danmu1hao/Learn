# 同一个目录下，可以直接访问
# 同じディレクトリ内は直接インポート可能
import moduel_example.b as b
# 当前目录的子目录 可以通过from访问
# 現在のディレクトリのサブディレクトリはfromでインポートできる
import moduel_example.folder.c as c
def test():
    b.test()
    c.test()

# 但是，无法访问当前文件的文件夹的外部的脚本
# ただし、現在のフォルダの外部にあるスクリプトはインポートできない
# import example.py