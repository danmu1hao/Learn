import sqlite3

# 连接数据库（没有会自动创建）
conn = sqlite3.connect('login.db')
cursor = conn.cursor()

# 创建表
cursor.execute('''
CREATE TABLE IF NOT EXISTS login (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
''')

# 插入测试数据
cursor.execute("INSERT INTO login (username, password) VALUES ('admin', '123456')")
cursor.execute("INSERT INTO login (username, password) VALUES ('user', 'password')")

conn.commit()
conn.close()

print("表创建完成，数据已插入！")