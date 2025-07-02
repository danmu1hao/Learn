import tkinter as tk
import sqlite3

# === データベース初期化 ===
def init_db():
    conn = sqlite3.connect("login.db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# === 登録処理 ===
def register():
    username = entry_user.get()
    password = entry_pass.get()
    if not username or not password:
        status_label.config(text="⚠️ ユーザー名とパスワードを入力してください")
        return
    conn = sqlite3.connect("login.db")
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        status_label.config(text="✅ 登録に成功しました")
    except sqlite3.IntegrityError:
        status_label.config(text="❌ ユーザー名は既に存在します")
    conn.close()

# === ログイン処理 ===
def login():
    username = entry_user.get()
    password = entry_pass.get()
    conn = sqlite3.connect("login.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = cur.fetchone()
    if result:
        status_label.config(text="🟢 ログイン成功！ようこそ")
    else:
        status_label.config(text="🔴 ログイン失敗：ユーザー名またはパスワードが間違っています")
    conn.close()

# === GUI 画面 ===
root = tk.Tk()
root.title("ログインシステム")

tk.Label(root, text="ユーザー名:").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="パスワード:").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="登録", command=register).pack(pady=5)
tk.Button(root, text="ログイン", command=login).pack(pady=5)

status_label = tk.Label(root, text="", fg="blue")
status_label.pack(pady=10)

init_db()
root.mainloop()
