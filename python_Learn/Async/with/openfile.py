import os
#__file__:スクリプトパス　os.path.dirname:ファイル名除くパス
folder_path = os.path.dirname(__file__)
print(folder_path)
new_path=folder_path+'///////text.txt'
print(new_path)
file=open(new_path,'r')
text=file.read()
print(text)
file.close()

with open (new_path,'r') as file:
    print(file.read())