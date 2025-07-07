import sqlite3
import os
# 这个是sqlinsert的测试代码
# このコードはsqlinsertのテストコード

folder_path = os.path.dirname(__file__)
db_path = os.path.join(folder_path, 'login.db')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS login (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
''')
cursor.execute("INSERT INTO login (username, password) VALUES (?, ?)", ("admin", "123456"))
conn.commit()

username = input("ユーザー名を入力してください：")
password = input("パスワードを入力してください：")

# 不安全的SQL拼接（容易被注入）
# 安全でないSQLの連結（SQLインジェクションされやすい）
sql = f"SELECT * FROM login WHERE username = '{username}' AND password = '{password}'"
print("実行するSQL文：", sql) 
cursor.execute(sql)

# 用户名设置为' OR '1'='1' --的话，此时的sql文是
# ユーザー名を ' OR '1'='1' -- に設定した場合、このときのSQL文は
# SELECT * FROM login WHERE username = '' OR '1'='1' -- ' AND password = '1'

result = cursor.fetchone()
if result:
    print("ログイン成功！現在のユーザー：", result[1])  
else:
    print("ユーザー名またはパスワードが間違っています！") 

conn.close()