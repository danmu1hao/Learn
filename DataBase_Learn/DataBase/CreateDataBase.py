import sqlite3

def create_db():
    conn = sqlite3.connect("CardData.db")
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