import tkinter as tk
import random  # 状態をシミュレートするために使用

def mock_unlock():
    global door_state
    door_state = "unlocked"
    status_label.config(text="🟢 シミュレーション：解錠リクエストを送信しました\n現在の状態：開いています")

def mock_lock():
    global door_state
    door_state = "locked"
    status_label.config(text="🔴 シミュレーション：施錠リクエストを送信しました\n現在の状態：施錠されています")

def mock_check():
    if door_state == "locked":
        status_label.config(text="🟡 現在の状態：ドアは【施錠中】です")
    elif door_state == "unlocked":
        status_label.config(text="🟡 現在の状態：ドアは【開いています】")


# ドア状態の初期値
door_state = "locked"

root = tk.Tk()
root.title("Sesameコントローラー（シミュレーションモード）")

btn_unlock = tk.Button(root, text="🔓 解錠（シミュ）", font=("Arial", 18), command=mock_unlock)
btn_unlock.pack(padx=20, pady=5)

btn_lock = tk.Button(root, text="🔒 施錠（シミュ）", font=("Arial", 18), command=mock_lock)
btn_lock.pack(padx=20, pady=5)

btn_check = tk.Button(root, text="🟡 状態確認", font=("Arial", 18), command=mock_check)
btn_check.pack(padx=20, pady=5)

status_label = tk.Label(root, text="", font=("Arial", 14))
status_label.pack(pady=20)

root.mainloop()
