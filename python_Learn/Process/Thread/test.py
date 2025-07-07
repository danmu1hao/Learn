import threading
import time

def slow_task():
    for i in range(10):
        print(f"[守护线程] 工作中 {i+1}/10")
        time.sleep(1)

t = threading.Thread(target=slow_task)
t.daemon = True    # 设置为守护线程
t.start()

print("主线程运行中... 等待 2 秒")
time.sleep(2)
print("主线程结束！（线程未完成，但程序强行退出）")
