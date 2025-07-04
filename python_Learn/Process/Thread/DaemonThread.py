import threading
import time
"""
出力
…働く中
…働く中
…働く中
---end---
"""
def threadFoo():
    while True:
        #永遠執行
        print("…働く中")
        time.sleep(1)

if __name__ == "__main__":
    #daemonをTrueにすると、メインスレッドと同時に終了できる
    thread = threading.Thread(target=threadFoo, name='thread1',daemon = True)
    thread.start()
    time.sleep(3)
    print("---end---")

