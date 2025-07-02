import threading, time, random

def cook(id):
    print(f"🍳 厨师{id} 开始炒菜")
    time.sleep(random.uniform(1,3))
    print(f"✅ 厨师{id} 完成")

threads = []
for i in range(5):                       # 5 本起こ す
    t = threading.Thread(args=(i,),target=cook)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
print("全部 OK")
threading.Thread()