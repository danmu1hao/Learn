import threading, time

# ─────────────────────────────────────────
# ① 無限ループのワーカー
# ─────────────────────────────────────────
def threadFoo():
    while True:
        print("…働く中 / 工作中")
        time.sleep(1)

# ─────────────────────────────────────────
# ② 監視関数 
# ─────────────────────────────────────────
def checkThread(t: threading.Thread):
    while True:
        print("Check ➔ is_alive =", t.is_alive())
        if not t.is_alive():
            print("⚠️ スレッド終了を検知 / 检测到线程已结束")
            break
        time.sleep(0.5)

# ─────────────────────────────────────────
# ③ メイン
# ─────────────────────────────────────────
if __name__ == "__main__":
    # daemon=True なのでメイン終了と同時に巻き添え終了
    worker = threading.Thread(target=threadFoo, name="worker", daemon=True)
    monitor = threading.Thread(target=checkThread, args=(worker,), name="monitor")

    worker.start()
    monitor.start()

    time.sleep(5)   # 5 秒後にメインスレッドを終了してみる
    print("--- main end ---")
    # join しないが daemon=True のためプロセス終了と同時に両方の子も終わる
