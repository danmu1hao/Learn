import threading, weakref, time, gc, sys

def worker():
    time.sleep(0.1)
    print("worker任務終了")

def make_thread():
    t = threading.Thread(target=worker)
    weakref.finalize(t, lambda: print("🗑 Thread 对象回収された！"))
    t.start()
    return t

t = make_thread()
t.join()                      
print("refcnt =", sys.getrefcount(t)-1) 

del t                         
gc.collect()                   
time.sleep(0.1)                
