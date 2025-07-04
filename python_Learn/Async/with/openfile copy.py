import os
#__file__:スクリプトパス　os.path.dirname:ファイル名除くパス
folder_path = os.path.dirname(__file__)
print(folder_path)
folder_path_new=folder_path+'\sample.txt'
file=open(folder_path_new,'rb')
text=file.read()
print(text)
