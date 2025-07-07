import sqlite3
import os

def create_db():
    # 获取当前脚本所在目录
    # スクリプトが存在するディレクトリを取得
    folder_path = os.path.dirname(__file__)
    db_path = os.path.join(folder_path, "CardData.db")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS People (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            cardNum INTEGER
        )
    ''')
    conn.commit()
    conn.close()

create_db()