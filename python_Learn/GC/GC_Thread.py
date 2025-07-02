import threading, weakref, time, gc, sys

def worker():
    time.sleep(0.1)
    print("[子] 仕事おわり")

def make_thread():
    t = threading.Thread(target=worker)
    # ❶ finalize：t が GC された瞬間にコールバック実行
    weakref.finalize(t, lambda: print("🗑 Thread オブジェクト回収！"))
    t.start()
    return t

t = make_thread()
t.join()      # OS スレッド終了 (is_alive → False)
print("refcnt =", sys.getrefcount(t)-1)  # 参照数を見る

del t        # ❷ Python 参照を全て削除
gc.collect() # ❸ 明示的に GC 発動してみる
time.sleep(0.1)  # finalize のメッセージ待ち
