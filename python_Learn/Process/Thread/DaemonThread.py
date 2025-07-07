import threading
import time
# deamonthread：主线程结束时会自动一起结束
# deamonthread メインスレッドが終了したら自動的に一緒に終了する
"""
出力
…働く中
…働く中
…働く中
---end---
"""
def threadFoo():
    while True:
        # 虽然是无限循环，但主线程结束后会自动结束
        # 永遠執行ですが、メインスレッドが終了したので終了する
        print("…働く中")
        time.sleep(1)

if __name__ == "__main__":
    # 把daemon设为True，主线程结束时子线程也会一起结束
    # daemonをTrueにすると、メインスレッドと同時に終了できる
    thread = threading.Thread(target=threadFoo, name='thread1',daemon = True)
    thread.start()
    time.sleep(3)
    print("---end---")

