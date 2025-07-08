# 同一个目录下，可以直接访问
import b
# 当前目录的子目录 可以通过from访问
from folder import c
b.test()
c.test()

#但是，无法访问当前文件的文件夹的外部的脚本，无论如何
# import example.py