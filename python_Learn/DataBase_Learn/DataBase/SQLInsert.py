import sqlite3

# 连接数据库
conn = sqlite3.connect('login.db')
cursor = conn.cursor()

# 用户输入（模拟）
username = input("请输入用户名：")
password = input("请输入密码：")

# 不安全的SQL拼接（容易被注入）
sql = f"SELECT * FROM login WHERE username = '{username}' AND password = '{password}'"
print("执行的SQL语句：", sql)
cursor.execute(sql)

result = cursor.fetchone()
if result:
    print("登录成功！当前用户：", result[1])
else:
    print("用户名或密码错误！")

conn.close()