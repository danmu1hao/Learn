import sqlite3
import os
#sql insert防止?
folder_path = os.path.dirname(__file__)
db_path = os.path.join(folder_path, "CardData.db")

def Connect_DataBase(dbName,command):
    path=folder_path+dbName
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute(command)
    conn.commit()
    conn.close()

def insert_people(name, age):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("INSERT INTO People (name, cardNum) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()

def delete_people(id):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("DELETE FROM People WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def select_people():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM People")
    rows = cur.fetchall()
    conn.close()
    return rows

def reset_ids():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # 一時テーブルを作成（idを自動採番する）
    cur.execute('''
        CREATE TABLE IF NOT EXISTS People_temp (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            cardNum INTEGER
        )
    ''')

    # 元のデータを挿入（idは自動で1から付く）
    cur.execute("INSERT INTO People_temp (name, cardNum) SELECT name, cardNum FROM People")

    # 元のテーブルを削除して置き換える
    cur.execute("DROP TABLE People")
    cur.execute("ALTER TABLE People_temp RENAME TO People")

    conn.commit()
    conn.close()
