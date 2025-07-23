# 	先入れ先出し
import queue, threading, time

q = queue.Queue(maxsize=3)   # 0=无限长

def producer():
    for i in range(5):
        q.put(i)             # 阻塞直到有空位
        print("生产", i)

def consumer():
    while True:
        val = q.get()        # 阻塞直到有数据
        print("消费", val)
        q.task_done()        # 告诉队列已处理完
        time.sleep(1)

threading.Thread(target=producer).start()
threading.Thread(target=consumer, daemon=True).start()
q.join()                     # 等待所有项目被 task_done
