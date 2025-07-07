# main_gui.py
import tkinter as tk
from tkinter import ttk
from CreateDataBase import create_db
import DatabaseCommand as db

# 如果没有就会自动作成，有则什么都不做
# なければ自動で作成し、あれば何もしない
create_db()

def register():
    name = name_entry.get()
    card = card_entry.get()
    if name and card.isdigit():
        db.insert_people(name, int(card))
        name_entry.delete(0, tk.END)
        card_entry.delete(0, tk.END)
        refresh_table()

def delect():
    selected = tree.focus()  # Treeviewで選択された項目のIDを取得
    if not selected:
        return  # 選ばれていない場合は何もしない

    values = tree.item(selected, "values")  # 選ばれた行のデータを取得（タプル）
    id = values[0]  # ID列（最初の要素）

    db.delete_people(id)  # DBから削除

    db.reset_ids()
    
    refresh_table()  # 表示を更新

def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
    for r in db.select_people():
        tree.insert('', tk.END, values=r)

root = tk.Tk()
root.title("人員登録 GUI")

tk.Label(root, text="名前").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="カード番号").grid(row=1, column=0)
card_entry = tk.Entry(root)
card_entry.grid(row=1, column=1)

tk.Button(root, text="登録", command=register).grid(row=2, column=0, columnspan=1)
tk.Button(root, text="削除", command=delect).grid(row=2, column=1, columnspan=2)

columns = ("ID", "名前", "カード番号")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=3, column=0, columnspan=2)

refresh_table()

root.mainloop()
