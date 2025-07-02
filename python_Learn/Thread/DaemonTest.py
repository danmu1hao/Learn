# daemon_test.py
import threading
import time

# ────────── 守護スレッド用関数 / 守护线程 ──────────
def daemon_task(name: str):
    count = 0
    while True:
        print(f"[{name}] alive → {count}")
        count += 1
        time.sleep(1)

# ────────── 非守護スレッド用関数 / 非守护线程 ──────────
def non_daemon_task():
    for i in range(6):          # 5 秒で自分だけ終了
        print(f"[worker] step {i}")
        time.sleep(1)
    print("[worker] finished")  # ここでスレッド終了 / 线程结束

# ────────── メイン / 主线程 ──────────
if __name__ == "__main__":
    # 2 本の守護スレッド
    d1 = threading.Thread(target=daemon_task, args=("daemon-1",), daemon=True)
    d2 = threading.Thread(target=daemon_task, args=("daemon-2",), daemon=True)
    # 1 本の非守護スレッド（既定で daemon=False）
    nd = threading.Thread(target=non_daemon_task)

    d1.start()
    d2.start()
    nd.start()

    nd.join()                   # 非守護が終わるまで待つ
    print("=== main thread exit ===")  # ここを出たらプロセス終了
