import threading
import time
# 主线程执行2秒 slow_task执行5秒 主线程会强行等到所有的线程结束
# メインスレッドは2秒実行、slow_taskは5秒実行。メインスレッドは全てのスレッドが終了するまで強制的に待つ。
def slow_task():
    for i in range(6):
        print(f"[非デーモンスレッド] 作業中 {i+1}/10")
        time.sleep(1)

t = threading.Thread(target=slow_task)
t.daemon = False   
t.start()

print("メインスレッド実行中... 2秒待機")
time.sleep(2)
print("メインスレッド終了！（ただしプログラムはスレッド終了まで待つ）")
